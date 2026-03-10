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

## Mentions

- [Making whiteboard actions available to Siri and Apple Intelligence](making-whiteboard-actions-available-to-siri-and-apple-intelligence.md)

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.whiteboard.createBoard` schema:

```swift
@AppIntent(schema: .whiteboard.createBoard)
struct CreateCanvasBoardIntent: AppIntent {
    @Parameter
    var title: String?

    func perform() async throws -> some ReturnsValue<CanvasEntity> {
        .result(value: CanvasEntity())
    }
}
```

For more information about the `.whiteboard` app intent domain, see [`Making whiteboard actions available to Siri and Apple Intelligence`](making-whiteboard-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

## See Also

- [var createItem: some AssistantSchemas.Intent](assistantschemas/whiteboardintent/createitem.md)
  The app intent conforms to the schema for creating an item on a whiteboard canvas.
- [var deleteBoard: some AssistantSchemas.Intent](assistantschemas/whiteboardintent/deleteboard.md)
  The app intent conforms to the schema for deleting a whiteboard canvas.
- [var deleteItem: some AssistantSchemas.Intent](assistantschemas/whiteboardintent/deleteitem.md)
  The app intent conforms to the schema for deleting an item on a whiteboard canvas.
- [var openBoard: some AssistantSchemas.Intent](assistantschemas/whiteboardintent/openboard.md)
  The app intent conforms to the schema for opening a new whiteboard canvas.
- [var updateBoard: some AssistantSchemas.Intent](assistantschemas/whiteboardintent/updateboard.md)
  The app intent conforms to the schema for updating a whiteboard canvas.
- [var updateItem: some AssistantSchemas.Intent](assistantschemas/whiteboardintent/updateitem.md)
  The app intent conforms to the schema for updating an item on a whiteboard canvas.
- [AssistantSchemas.WhiteboardIntent](assistantschemas/whiteboardintent.md)
  Assistant schema conformance for app intents that offer whiteboard functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/whiteboardintent/createboard)*