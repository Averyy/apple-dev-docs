# Tool

**Framework**: Foundation Models  
**Kind**: protocol

A tool that a model can call to gather information at runtime or perform side effects.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol Tool<Arguments, Output> : Sendable
```

## Mentions

- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)
- [Categorizing and organizing data with content tags](categorizing-and-organizing-data-with-content-tags.md)
- [Expanding generation with tool calling](expanding-generation-with-tool-calling.md)

#### Overview

Tool calling gives the model the ability to call your code to incorporate up-to-date information like recent events and data from your app. A tool includes a name and a description that the framework puts in the prompt to let the model decide when and how often to call your tool.

A `Tool` defines a [`call(arguments:)`](tool/call(arguments:).md) method that takes arguments that conforms to [`ConvertibleFromGeneratedContent`](convertiblefromgeneratedcontent.md), and returns an output of any type that conforms to [`PromptRepresentable`](promptrepresentable.md), allowing the model to understand and reason about in subsequent interactions. Typically, [`Output`](tool/output.md) is a `String` or any [`Generable`](generable.md) types.

```swift
struct FindContacts: Tool {
    let name = "findContacts"
    let description = "Find a specific number of contacts"

    @Generable
    struct Arguments {
        @Guide(description: "The number of contacts to get", .range(1...10))
        let count: Int
    }

    func call(arguments: Arguments) async throws -> [String] {
        var contacts: [CNContact] = []
        // Fetch a number of contacts using the arguments.
        let formattedContacts = contacts.map {
            "\($0.givenName) \($0.familyName)"
        }
        return formattedContacts
    }
}
```

Tools must conform to [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable) so the framework can run them concurrently. If the model needs to pass the output of one tool as the input to another, it executes back-to-back tool calls.

You control the life cycle of your tool, so you can track the state of it between calls to the model. For example, you might store a list of database records that you don’t want to reuse between tool calls.

Prompting the model with tools contributes to the available context window size. When you provide a tool in your generation request, the framework puts the tool definitions — name, description, parameter information — in the prompt so the model can decide when and how often to call the tool. After calling your tool, the framework returns the tool’s output back to the model for further processing.

To efficiently use tool calling:

- Reduce [`Guide(description:)`](guide(description:).md) descriptions to a short phrase each.
- Limit the number of tools you use to three to five.
- Include a tool only when its necessary for the task you want to perform.
- Run an essential tool before calling the model and integrate the tool’s output in the prompt directly.

If your session exceeds the available context size, it throws [`LanguageModelSession.GenerationError.exceededContextWindowSize(_:)`](languagemodelsession/generationerror/exceededcontextwindowsize(_:).md). When you encounter the context window limit, consider breaking up tool calls across new [`LanguageModelSession`](languagemodelsession.md) instances. For more information on managing the context window size, see [`TN3193: Managing the on-device foundation model’s context window`](https://developer.apple.com/documentation/Technotes/tn3193-managing-the-on-device-foundation-model-s-context-window).

## Topics

### Invoking a tool
- [func call(arguments: Self.Arguments) async throws -> Self.Output](tool/call(arguments:).md)
  A language model will call this method when it wants to leverage this tool.
- [associatedtype Arguments : ConvertibleFromGeneratedContent](tool/arguments.md)
  The arguments that this tool should accept.
- [associatedtype Output : PromptRepresentable](tool/output.md)
  The output that this tool produces for the language model to reason about in subsequent interactions.
### Getting the tool properties
- [var description: String](tool/description.md)
  A natural language description of when and how to use the tool.
- [var includesSchemaInInstructions: Bool](tool/includesschemaininstructions.md)
  If true, the model’s name, description, and parameters schema will be injected into the instructions of sessions that leverage this tool.
- [var name: String](tool/name.md)
  A unique name for the tool, such as “get_weather”, “toggleDarkMode”, or “search contacts”.
- [var parameters: GenerationSchema](tool/parameters.md)
  A schema for the parameters this tool accepts.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Expanding generation with tool calling](expanding-generation-with-tool-calling.md)
  Build tools that enable the model to perform tasks that are specific to your use case.
- [Generate dynamic game content with guided generation and tools](generate-dynamic-game-content-with-guided-generation-and-tools.md)
  Make gameplay more lively with AI generated dialog and encounters personalized to the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/tool)*