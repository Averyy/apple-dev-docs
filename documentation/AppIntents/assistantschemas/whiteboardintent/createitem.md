# createItem

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for creating an item on a whiteboard canvas.

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
var createItem: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.whiteboard.createItem` schema:

```swift
@AppIntent(schema: .whiteboard.createItem)
struct CreateCanvasItemIntent: AppIntent {
    @Parameter
    var target: CanvasEntity

    @Parameter
    var itemType: CanvasItemType?

    @Parameter
    var text: String?

    @Parameter
    var mediaItems: [IntentFile]

    @Parameter
    var url: URL?

    func perform() async throws -> some ReturnsValue<CanvasItemEntity> {
        .result(value: CanvasItemEntity())
    }
}
```

For more information about the `.whiteboard` app intent domain, see [`Whiteboard`](app-schema-domain-whiteboard.md). For general information about app intent domains, see [`Making actions and content discoverable by Apple Intelligence`](making-actions-and-content-discoverable-by-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/whiteboardintent/createitem)*