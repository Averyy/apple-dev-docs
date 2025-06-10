# Tool

**Framework**: Foundation Models  
**Kind**: protocol

A tool that a model can call to gather information at runtime or perform side effects.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol Tool : Sendable
```

## Mentions

- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)
- [Expanding generation with tool calling](expanding-generation-with-tool-calling.md)

#### Overview

Tool calling gives the model the ability to call your code to incorporate up-to-date information like recent events and data from your app. A tool includes a name and a description that the framework puts in the prompt to let the model decide when and how often to call your tool.

```swift
struct FindContacts: Tool {
    let name = "findContacts"
    let description = "Find a specific number of contacts"

    @Generable
    struct Arguments {
        @Guide(description: "The number of contacts to get", .range(1...10))
        let count: Int
    }

    func call(arguments: Arguments) async throws -> ToolOutput {
        var contacts: [CNContact] = []
        // Fetch a number of contacts using the arguments.
        let formattedContacts = contacts.map {
            "\($0.givenName) \($0.familyName)"
        }
        return ToolOutput(GeneratedContent(properties: ["contactNames": formattedContacts]))
    }
}
```

Tools must conform to [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable) so the framework can run them concurrently. If the model needs to pass the output of one tool as the input to another, it executes back-to-back tool calls.

You control the life cycle of your tool, so you can track the state of it between calls to the model. For example, you might store a list of database records that you don’t want to reuse between tool calls.

## Topics

### Invoking a tool
- [func call(arguments: Self.Arguments) async throws -> ToolOutput](tool/call(arguments:).md)
  A language model will call this method when it wants to leverage this tool.
- [struct ToolOutput](tooloutput.md)
  A structure that contains the output a tool generates.
- [associatedtype Arguments : ConvertibleFromGeneratedContent](tool/arguments.md)
  The arguments that this tool should accept.
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