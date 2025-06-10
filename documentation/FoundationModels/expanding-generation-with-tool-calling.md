# Expanding generation with tool calling

**Framework**: Foundation Models

Build tools that enable the model to perform tasks that are specific to your use case.

#### Overview

Tools provide a way to extend the functionality of the model for your own use cases. Tool-calling allows the model to interact with external code you create to fetch up-to-date information, ground responses in sources of truth that you provide, and perform side effects, like turning on dark mode.

You can create tools that enable the model to:

- Query entries from your app’s database and reference them in its answer.
- Perform actions within your app, like adjusting the difficulty in a game or making a web request to get additional information.
- Integrate with other frameworks, like [`Contacts`](https://developer.apple.com/documentation/Contacts) or [`HealthKit`](https://developer.apple.com/documentation/HealthKit), that use existing privacy and security mechanisms.

#### Create a Custom Tool for Your Task

When you prompt the model with a question or make a request, the model decides whether it can provide an answer or if it needs the help of a tool. When the model determines that a tool can help, it calls the tool with additional arguments that the tool can use. After the tool completes the task, it returns control back to the model with information about what the tool did. The model can then use the output of the tool when it provides the final response.

Before creating a tool, it’s helpful to understand the pattern the framework follows when using the tool you provide. The framework processes a request in six phases:

1. You present a list of available tools and their parameters to the model.
2. You submit your prompt to the model.
3. The model generates arguments to the tool(s) it wants to invoke.
4. Your tool runs code on behalf of the model, using the model’s generated arguments.
5. Your tool passes its output back to the model.
6. The model produces a final response to the prompt, based on the tool output.

A tool conforms to [`Tool`](tool.md) and contains the arguments that the tool accepts, and a method that the model calls when it wants to use the tool. You can call [`call(arguments:)`](tool/call(arguments:).md) concurrently with itself or with other tools. The following example shows a tool that accepts a search term and a number of recipes to retrieve:

```swift
struct BreadDatabaseTool: Tool {
    let name = "searchBreadDatabase"
    let description = "Searches a local database for bread recipes."

    @Generable
    struct Arguments {
        @Guide(description: "The type of bread to search for")
        var searchTerm: String
        @Guide(description: "The number of recipes to get", .range(1...6))
        var limit: Int
    }

    struct Recipe {
        var name: String
        var description: String
        var link: URL
    }
    
    func call(arguments: Arguments) async throws -> ToolOutput {
        var recipes: [Recipe] = []
        // Get a list of recipes from your local database.
        let formattedRecipes = recipes.map {
            "Recipe for '\($0.name)': \($0.description) Link: \($0.link)"
        }
        return ToolOutput(GeneratedContent(properties: ["recipes": formattedRecipes]))
    }
}
```

When you provide descriptions to generable properties, you help the model understand the semantics of the arguments. Keep descriptions as short as possible because long descriptions take up context size and can introduce latency.

Tools use guided generation for the [`Arguments`](tool/arguments.md) property. For more information about guided generation, see [`Generating Swift data structures with guided generation`](generating-swift-data-structures-with-guided-generation.md).

#### Provide a Session with the Tool You Create

When you create a session, you can provide a list of tools that are relevant to the task you want to complete. The tools you provide are available for all future interactions with the session. The following example initializes a session with a tool that the model can call when it determines that it would help satisfy the prompt:

```swift
let session = LanguageModelSession(
    tools: [BreadDatabaseTool()]
)

let response = try await session.respond(
    to: "Find three sourdough bread recipes"
)
```

Tool output can be a string, or a [`GeneratedContent`](generatedcontent.md) object. The model can call a tool multiple times in parallel to satisfy the request, like when retrieving weather details for several cities:

```swift
struct WeatherTool: Tool {
  let name = "getWeather"
  let description = "Retrieve the latest weather information for a city"

  @Generable
  struct Arguments {
      @Guide(description: "The city to get weather information for")
      var city: String
  }

  struct Forecast: Encodable {
      var city: String
      var temperature: Int
  }

  func call(arguments: Arguments) async throws -> ToolOutput {
      var temperature = "unknown"
      // Get the temperature for the city by using `WeatherKit`.
      let forecast = GeneratedContent(properties: [
          "city": arguments.city,
          "temperature": temperature,
      ])
      return ToolOutput(forecast)
  }
}

// Create a session with default instructions that guide the requests.
let session = LanguageModelSession(
    tools: [WeatherTool()],
    instructions: "Help the person with getting weather information"
)

// Make a request that compares the temperature between several locations.
let response = try await session.respond(
    to: "Is it hotter in Boston, Wichita, or Pittsburgh?"
)
```

#### Handle Errors Thrown By a Tool

When an error happens during tool calling, the session throws a [`LanguageModelSession.ToolCallError`](languagemodelsession/toolcallerror.md) with the underlying error and includes the tool that throws the error. This helps you understand the error that happened during the tool call, and any custom error types that your tool produces. You can throw errors from your tools to escape calls when you detect something is wrong, like when the person using your app doesn’t allow access to the required data or a network call is taking longer than expected. Alternatively, your tool can return a string [`ToolOutput`](tooloutput.md) that briefly tells the model what didn’t work, like “Cannot access the database.”

```swift
do {
    let answer = try await session.respond("Find a recipe for tomato soup.")
} catch let error as LanguageModelSession.ToolCallError {
        
    // Access the name of the tool, like BreadDatabaseTool.
    print(error.tool.name) 
        
    // Access an underlying error that your tool throws and check if the tool 
    // encounters a specific condition.
    if case .databaseIsEmpty = error.underlyingError as? SearchBreadDatabaseToolError {
        // Display an error in the UI.
    }

} catch {
    print("Some other error: \(error)")
}
```

#### Inspect the Call Graph

A session contains an observable [`transcript`](languagemodelsession/transcript.md) property that allows you to track when, and how many times, the model calls your tools. A transcript also provides the ability to construct a representation of the call graph for debugging purposes and pairs well with [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI) to visualize session history.

```swift
struct MyHistoryView: View {

    @State
    var session = LanguageModelSession(
        tools: [BreadDatabaseTool()]
    )
    
    var body: some View {
        List(session.transcript) { entry in
            switch entry {       
            case .instructions(let instructions):
                // Display the instructions the model uses.
            case .prompt(let prompt):
                // Display the prompt made to the model.
            case .toolCall(let call):
                // Display the call details for a tool, like the tool name and arguments.        
            case .toolOutput(let output):
                // Display the output that a tool provides back to the model.        
            case .response(let response):
                // Display the response from the model.
            }
        }.task {
            do {
                try await session.respond(to: "Find a milk bread recipe.")
            } catch let error {
                // Handle the error.
            }
        }
    }
    
}
```

## See Also

- [Generate dynamic game content with guided generation and tools](generate-dynamic-game-content-with-guided-generation-and-tools.md)
  Make gameplay more lively with AI generated dialog and encounters personalized to the player.
- [protocol Tool](tool.md)
  A tool that a model can call to gather information at runtime or perform side effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/expanding-generation-with-tool-calling)*