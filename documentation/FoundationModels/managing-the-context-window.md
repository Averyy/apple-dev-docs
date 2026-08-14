# Managing the context window

**Framework**: Foundation Models

Optimize your app’s token usage when prompting a model with the Foundation Models framework.

#### Overview

When working with a model — like the default on-device foundation model — you have a fixed *context window* that limits the number of tokens the model can process in a single *session*. Apple’s on-device foundation model has a context window of 4096 tokens per session, with a token representing each word, or partial word.

The size of the context window matters, because every session interaction with the model consumes input and output tokens from this window. This includes all prompts, instructions, tool definitions and their input and output, generable type schemas, and all of the model’s responses.

Understanding and managing the context window is essential for building reliable AI features in your app. This article covers several strategies for staying within a token budget, along with how to recover from exceeding the budget.

#### Understand Tokens and the Context Window

In Latin alphabet languages such as English, a token typically represents three to four characters. For multibyte languages such as Chinese, Japanese, Korean, and Vietnamese a token typically represents one character.

The context window defines the maximum number of tokens the model can process in a [`LanguageModelSession`](languagemodelsession.md) instance. When you prompt the model using the same session, you consume more of the context window. Use [`tokenCount(for:)`](systemlanguagemodel/tokencount(for:).md) to understand how many tokens your prompt, instruction, or tool uses. You can also call [`contextSize`](systemlanguagemodel/contextsize.md) to retrieve the maximum size (in tokens) that the model supports.

The following diagram shows the context window filling over a number of turns of a conversation. In a later turn, the context window is nearly full with the accumulated content from the previous turns, and eventually appears with a dashed red border to indicate that the session exceeded the content size:

![A diagram showing how the context window fills over a number of turns of a conversation.](/images/com.apple.foundationmodels/managing-the-context-window-context-window@2x.png)

After reaching the context size, the session can no longer process additional requests and throws an [`LanguageModelError.contextSizeExceeded(_:)`](languagemodelerror/contextsizeexceeded(_:).md) error. When this happens, trim the session history or create a new session to get a fresh context window. Use [`init(model:tools:transcript:)`](languagemodelsession/init(model:tools:transcript:).md) and include any state from the original session that’s necessary for the request, then retry:

![A diagram showing a new session with a fresh context window. The session](/images/com.apple.foundationmodels/managing-the-context-window-new-context-window@2x.png)

#### Profile Token Usage in Xcode

Before optimizing your token usage, it’s important to understand how your interaction with the model impacts token growth. The Foundation Models instrument in Xcode provides real-time visibility into token usage. To profile your app in Xcode:

1. Choose Product > Profile to launch Instruments.
2. Select the Foundation Models template, then click Choose.
3. Click the Record button and interact with your app’s AI features.
4. Observe the token count as your app interacts with the model.

![A screenshot of Instruments displaying the Foundation Models instrument track](/images/com.apple.foundationmodels/analyzing-the-runtime-performance-of-your-foundation-models-app-record-analysis@2x.png)

The instrument shows you exactly how many tokens each interaction uses for your app’s input and output tokens the model generates. It provides a detailed breakdown of your session requests, prompts, responses, and tool calls to help you identify opportunities for optimization, like:

- Reducing the amount of tokens necessary for the prompts and instructions.
- Limiting model responses to what your app needs.
- Managing the amount of context your generable types and tools use.
- Identifying areas of opportunity to break a task into separate sessions with a fresh context window.

For more information about profiling, see [`Analyzing the runtime performance of your Foundation Models app`](analyzing-the-runtime-performance-of-your-foundation-models-app.md).

#### Write Concise Prompts and Instructions

Prompts and instructions often consume the most tokens, especially in multiturn conversations. Shorter, clearer prompts not only save tokens but they often produce better results. Focus on clarity and brevity, along with:

- Use imperative verbs that clearly state what you want the model to do: “Generate a story about…,” or “List five reasons why…”.
- Provide only the information the model needs for the specific task.
- Avoid lengthy background information, policies, or unnecessary context.
- Reduce prompts to no more than three paragraphs in length.
- Eliminate indirect language, excessive formality, and ambiguous jargon.

For more information on prompting a model, see [`Prompting an on-device foundation model`](prompting-an-on-device-foundation-model.md).

#### Ask the Model for Less Content

If you notice the model produces long, detailed responses, try limiting how many tokens the model uses in its responses:

- Specify the desired response length in your prompt, by starting the prompt with text like “In three sentences…,” or “List three reasons…”.
- For [`Generable`](generable.md) arrays, add an `@Guide` macro that specifies a [`maximumCount(_:)`](generationguide/maximumcount(_:).md) to limit the number of items the model produces.

```swift
@Generable 
struct GameSettings {
    @Guide(.minimumCount(1), .maximumCount(20))
    @Guide(description: "Keyboard shortcuts for desktop")
    var keyboardShortcuts: [String]
}
```

> ❗ **Important**: Only use [`maximumResponseTokens`](generationoptions/maximumresponsetokens.md) to prevent verbose responses. Limiting tokens can cause the model to generate incomplete or grammatically incorrect responses, like “A cat is a small.”

#### Simplify Generable Types

Generable types consume tokens in multiple ways. The framework converts each type’s structure into a JSON schema and sends that to the model.

Any `@Guide` descriptions you add also consume tokens because they become part of the schema that’s sent to the model. Similar to the instructions you provide the model, these descriptions help the model understand more about your custom type but uses context to do so. To minimize token usage:

- Keep your types simple and focused — complex type definitions consume more tokens.
- Use short, descriptive property names.
- Use `@Guide` only where necessary. If your property names are clear, the model may not need additional guidance.

The following example shows a custom type with only the properties necessary for the task and clear names that the model can infer:

```swift
@Generable
struct ContentAnalysis {
    // Clear property names that the model can infer won't need an `@Guide`.
    var title: String
    var summary: String
            
    // A minimum and maximum to a rating provides details to the model that it
    // otherwise wouldn't know. There is no need for a description because the 
    // property name is clear.
    @Guide(.minimum(1), .maximum(10))
    var rating: Int
}
```

Test Generable types without an `@Guide` macro first, then add guide annotations to the properties that need more clarity to help the model improve the response quality. If you have an unclear property name, it won’t convey the right intent to the model. Instead, consider renaming the property so it’s easier to interpret, or apply an `@Guide` macro to provide a description that the model uses when generating a response.

#### Use Tool Calling Efficiently

Like `@Generable` types, each tool call and its output consume tokens. The framework sends tool definitions — including names, descriptions, and parameters — to the model so it can decide when to call them. To use tools efficiently:

- Limit tool descriptions and `@Guide` annotations to short phrases.
- Provide no more than three to five tools per request.
- Skip tool calling when you don’t need the model to make decisions. If the model always needs specific information, retrieve it directly and include it in your prompt rather than relying on tool calling.

The following shows a tool with a clear description and provides the model with additional context about the parameters it fills in when performing a tool call:

```swift
@Observable
final class FindPointsOfInterestTool: Tool {
    let name = "findPointsOfInterest"
    let description = "Finds points of interest for a landmark."
    
    @Generable
    enum Category: String, CaseIterable {
        case campground
        case hotel
        case cafe
        case museum
        case marina
        case restaurant
        case nationalMonument
    }

    @Generable
    struct Arguments {
        @Guide(description: "The type of destination to look up.")
        let pointOfInterest: Category

        @Guide(description: "The natural language query of what to search for.")
        let naturalLanguageQuery: String
    }
    
    func call(arguments: Arguments) async throws -> String {
        // Implement the logic your app needs when the model calls this tool.
    }
}
```

For complex workflows that approach the context window limit, split tool usage across multiple sessions. When you need the model to generate tool arguments, consider asking the model to generate those in one session, execute the tool in your code, then have the model process the tool’s output in a new session.

#### Split Large Tasks Across Multiple Sessions

When a task requires more than the size of the context window, divide it into smaller steps that each run in a new language model session. For example, to summarize a long article:

1. Split the article into chunks that fit within the context window.
2. Summarize each chunk in a separate session.
3. Combine the chunk summaries.
4. If needed, summarize the combined summaries in another session.
5. Repeat until you reach your target length.

To maintain context between chunks, include the previous chunk’s summary in the next chunk’s prompt:

```swift
let chunks: [String] = // Split a long article into separate chunks.
var chunkSummaries: [String] = []

// Use a separate session to summarize each chunk.
for (index, chunk) in chunks.enumerated() {
    
    let session = LanguageModelSession()
    var prompt = """
        Summarize this section of an article:
        
        \(chunk)
        """

    // Include the previous summary to maintain continuity.
    if index > 0 {
        prompt = """
        Previous section summary: \(chunkSummaries[index - 1])

        \(prompt)
        """
    }

    // Perform the request and track the response.
    let response = try await session.respond(to: prompt)
    chunkSummaries.append(response.content)
}

// Combine all chunk summaries in a final session.
let finalSession = LanguageModelSession()
let combined = chunkSummaries.joined(separator: "\n")

let prompt = """
    Combine these section summaries into one cohesive summary:

    \(combined)
    """

// Perform the request to get the final summary.
let finalSummary = try await finalSession.respond(to: prompt).content
```

#### Handle Context Window Errors

Even with careful optimization, you may exceed the context window limit. This commonly occurs in open-ended conversations where people continue chatting until they reach the token limit. When your app exceeds the limit, the framework throws an [`LanguageModelError.contextSizeExceeded(_:)`](languagemodelerror/contextsizeexceeded(_:).md) error and the session stops responding. When this occurs, create a new session and evaluate your user experience so people understand what happened. You can catch the error in your code, like the following example shows:

```swift
do {
    // Perform a request that exceeds the context window.
    let response = try await session.respond(to: prompt)
} catch LanguageModelError.contextSizeExceeded(let context) {
    // Handle exceeding the context window size by creating a new session.
} catch {
    // Handle other errors that are thrown.
}
```

When you create a new session, you get a fresh context window that doesn’t retain the state from the original session. To preserve context, either summarize the original session’s transcript and use that summary to initialize the new session, or extract key entries from the original transcript and use them to seed the new session. The following example creates a new session using the first and last entries from the original session:

```swift
func newContextualSession(with originalSession: LanguageModelSession) -> LanguageModelSession {
    let allEntries = originalSession.transcript
    let condensedEntries = [allEntries.first, allEntries.last].compactMap { $0 }
    let condensedTranscript = Transcript(entries: condensedEntries)
    let newSession = LanguageModelSession(transcript: condensedTranscript)
    newSession.prewarm()
    return newSession
}
```

The first transcript entry often contains important instructions and the last entry contains the most recent context. By preserving the first and last entry, you maintain continuity while dramatically reducing token usage.

## See Also

- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)
  Tailor your prompts to get effective results from an on-device model.
- [Updating prompts for new model versions](updating-prompts-for-new-model-versions.md)
  Manage the prompts your app uses by versioning them to make the most out of model improvements.
- [class LanguageModelSession](languagemodelsession.md)
  An object that represents a session that interacts with a language model.
- [struct Instructions](instructions.md)
  Details you provide that define the model’s intended behavior on prompts.
- [struct Prompt](prompt.md)
  A prompt from a person to the model.
- [struct GenerationOptions](generationoptions.md)
  Options that control how the model generates its response to a prompt.
- [struct ContextOptions](contextoptions.md)
  Options that configure details that should appear in the prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/managing-the-context-window)*