# openBoard

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for opening a new whiteboard canvas.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var openBoard: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.whiteboard.openBoard` schema:

```swift
@AppIntent(schema: .whiteboard.openBoard)
struct OpenCanvasBoardIntent: OpenIntent {
    @Parameter
    var target: CanvasEntity

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

For more information about the `.whiteboard` app intent domain, see doc:Making-whiteboard-actions-available-to-siri-and-apple-intelligence. For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/whiteboardintent/openboard)*