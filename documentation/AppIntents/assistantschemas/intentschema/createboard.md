# createBoard

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for creating a new whiteboard canvas.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var createBoard: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.whiteboard.createBoard` schema:

```swift
@AssistantIntent(schema: .whiteboard.createBoard)
struct CreateCanvasBoardIntent: AppIntent {
    @Parameter
    var title: String?

    func perform() async throws -> some ReturnsValue<CanvasEntity> {
        .result(value: CanvasEntity())
    }
}
```

For more information about the `.whiteboard` app intent domain, see [`Making whiteboard actions available to Siri and Apple Intelligence`](making-whiteboard-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/intentschema/createboard)*