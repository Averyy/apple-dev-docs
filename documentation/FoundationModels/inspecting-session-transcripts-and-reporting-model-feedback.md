# Inspecting session transcripts and reporting model feedback

**Framework**: Foundation Models

Review session history to display the conversation in your app’s UI, manage the context window, or diagnose and report unexpected model output.

#### Overview

Every conversation your app has with a language model is recorded in a transcript. It’s a record of everything that happens in a session: the instructions you set, the prompts a person enters, the responses the language model returns, and any tools it calls along the way. You can read through it at any time to see exactly what the language model receives and produces.

Session history is useful in many ways, such as:

- When a long conversation fills up and the language model runs out of room to continue, inspect the transcript, keep the relevant parts, and update the transcript.
- When you want to understand how a feature behaves as the model updates or as people change how they use it, record the transcript so you can compare the same input over time and across model versions.
- When the language model returns a response that you believe isn’t being properly handled, like with a safety guardrail incorrectly activating, package the transcript as feedback and send it to the model provider to help improve it.

#### Inspect the Entries in a Transcript

To read what happened during a session, iterate [`transcript`](languagemodelsession/transcript.md) and handle each [`Transcript.Entry`](transcript/entry.md) according to its case. Each case carries an associated value that holds the details for that kind of entry. The following fragment reads a few of the entries:

```swift
for entry in session.transcript {
    switch entry {
    case .instructions(let instructions):
        // The guidance you gave the language model.
    case .prompt(let prompt):
        // A request from a person using your app.
    case .response(let response):
        // A response the language model generated.
    default:
        // Other entries, like reasoning, tool calls, and tool output.
    }
}
```

A [`Transcript.Entry`](transcript/entry.md) also represents [`Transcript.Entry.reasoning(_:)`](transcript/entry/reasoning(_:).md), [`Transcript.Entry.toolCalls(_:)`](transcript/entry/toolcalls(_:).md), and [`Transcript.Entry.toolOutput(_:)`](transcript/entry/tooloutput(_:).md), which you handle the same way when your app uses reasoning or tool calling.

To work with just the conversation *turns* — the prompts and responses a person typically recognizes — read [`history`](transcript/history.md). It returns the same entries but omits the leading instructions entry, which is convenient when you display the conversation in your app’s UI and don’t want to surface the instructions you configured.

#### Recover From a Full Context Window

Every language model has a fixed context window. To check the context size of Apple Intelligence models, use [`SystemLanguageModel.contextSize`](https://developer.apple.com``SystemLanguageModel/contextSize``) or [`PrivateCloudComputeLanguageModel.contextSize`](https://developer.apple.com``PrivateCloudComputeLanguageModel/contextSize``). When a session exceeds the window, the framework throws [`LanguageModelError.contextSizeExceeded(_:)`](languagemodelerror/contextsizeexceeded(_:).md) and the session stops responding. Recover by reducing the transcript to only the entries that still matter and retry the request.

Because [`transcript`](languagemodelsession/transcript.md) is mutable, trim it in place before reaching the context size. Build a condensed [`Transcript`](transcript.md) from a selection of the original entries. For example, the first and last entries are a good choice because you carry forward your instructions and the latest context. Assign the result back to the session, as shown here:

```swift
let entries = session.transcript
let kept = [entries.first, entries.last].compactMap { $0 }
session.transcript = Transcript(entries: kept)
```

If your app persists a conversation between app launches, restore it by using [`init(model:tools:transcript:)`](languagemodelsession/init(model:tools:transcript:).md) with an existing transcript.

For more information about context management, see [`Managing the context window`](managing-the-context-window.md).

#### Record Transcripts to Monitor Output Over Time

A feature powered by a language model can behave differently over time as the underlying model updates or as people change how they interact with it. To keep track of that behavior, record the [`Transcript`](transcript.md) from a session so you can compare how the same input performs across model versions and spot changes you didn’t expect.

Because everything you send and receive is already captured in [`transcript`](languagemodelsession/transcript.md), and a [`Transcript`](transcript.md) conforms to [`Codable`](https://developer.apple.com/documentation/Swift/Codable), serialize it to JSON and store it alongside a version identifier, like this:

```swift
let session = LanguageModelSession()
let response = try await session.respond(to: "Help me plan a trip to Tokyo")

// Encode the transcript that now holds both the prompt and the response.
let data = try JSONEncoder().encode(session.transcript)
```

For more information about handling new model versions, see [`Updating prompts for new model versions`](updating-prompts-for-new-model-versions.md).

> ❗ **Important**: Because a session transcript includes all prompts, model responses, and tool data, review what it contains before storing or submitting it. Avoid sending sensitive or personal information about the people using your app, and only capture and submit feedback with the person’s knowledge and consent. For more information about privacy, see [`App privacy details on the App Store`](https://developer.apple.comhttps://developer.apple.com/app-store/app-privacy-details/).

#### Report a Response to Improve the Model

When a language model returns a response that’s factually incorrect or shows problematic guardrail behavior, capture the response for a bug report. Call [`logFeedbackAttachment(sentiment:issues:desiredOutput:)`](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredoutput:).md) on the session to serialize the current transcript, together with your assessment, into JSON and return it as [`Data`](https://developer.apple.com/documentation/Foundation/Data).

Describe your assessment with two specifics:

- Include a [`LanguageModelFeedback.Sentiment`](languagemodelfeedback/sentiment.md) for your overall reaction, using either [`LanguageModelFeedback.Sentiment.negative`](languagemodelfeedback/sentiment/negative.md), [`LanguageModelFeedback.Sentiment.neutral`](languagemodelfeedback/sentiment/neutral.md), or [`LanguageModelFeedback.Sentiment.positive`](languagemodelfeedback/sentiment/positive.md).
- Add one or more [`LanguageModelFeedback.Issue`](languagemodelfeedback/issue.md) values. Give each a [`LanguageModelFeedback.Issue.Category`](languagemodelfeedback/issue/category.md), such as [`LanguageModelFeedback.Issue.Category.incorrect`](languagemodelfeedback/issue/category/incorrect.md), [`LanguageModelFeedback.Issue.Category.unhelpful`](languagemodelfeedback/issue/category/unhelpful.md), or [`LanguageModelFeedback.Issue.Category.tooVerbose`](languagemodelfeedback/issue/category/tooverbose.md), and an optional explanation in your own words.

The following reports an incorrect response, explains the problem, and includes the text you expected instead:

```swift
let issue = LanguageModelFeedback.Issue(
    category: .incorrect,
    explanation: "The response named the wrong capital city."
)

let data = session.logFeedbackAttachment(
    sentiment: .negative,
    issues: [issue],
    desiredResponseText: "The capital of Australia is Canberra."
)
```

To supply the output you expected, pick the variant that matches your data. Pass plain text with [`logFeedbackAttachment(sentiment:issues:desiredResponseText:)`](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredresponsetext:).md), structured content with [`logFeedbackAttachment(sentiment:issues:desiredResponseContent:)`](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredresponsecontent:).md), or a full [`Transcript.Entry`](transcript/entry.md) with [`logFeedbackAttachment(sentiment:issues:desiredOutput:)`](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredoutput:).md).

Save the returned `Data` to disk and attach it to a bug report. When reporting an issue with an Apple Intelligence model, use [`Feedback Assistant`](https://developer.apple.comhttps://feedbackassistant.apple.com/). For other model providers, see their documentation to understand how to provide feedback.

#### Annotate a Transcript with the App Context

When a prompt depends on your app’s state, record that state alongside the transcript so you can reconstruct why the model produced a given output, like this:

```swift
struct AnnotatedTranscript: Encodable {
    var transcript: Transcript
    var annotations: [String: String]
}

let playerName = // The player's name.
let inventoryDescription = // Information related to the player's inventory.
let annotated = AnnotatedTranscript(
    transcript: session.transcript,
    annotations: ["player": playerName, 
                  "inventory": inventoryDescription]
)
```

Encode and store the annotated record as before, adding any details that help you reproduce the behavior, such as your app’s version.

To carry that same context into a bug report, include it in the feedback attachment [`logFeedbackAttachment(sentiment:issues:desiredOutput:)`](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredoutput:).md) produces. Use [`LanguageModelFeedback.Issue`](languagemodelfeedback/issue.md) to provide a free-form explanation that the framework serializes into the attachment alongside the transcript. Format your annotations into that explanation:

```swift
let context = "player: \(playerName), inventory: \(inventoryDescription)"

let issue = LanguageModelFeedback.Issue(
    category: .incorrect,
    explanation: "Unexpected trade offer. App context — \(context)"
)

let data = session.logFeedbackAttachment(sentiment: .negative, 
                                         issues: [issue])
```

Your app context now travels inside the attachment you submit, so whoever reviews the report sees the state the model produced its output in.

## See Also

- [struct Transcript](transcript.md)
  A linear history of entries that reflect an interaction with a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/inspecting-session-transcripts-and-reporting-model-feedback)*