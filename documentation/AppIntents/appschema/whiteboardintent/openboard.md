# openBoard

**Framework**: App Intents  
**Kind**: property

An intent schema that opens an existing board.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var openBoard: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `whiteboard` domain and one of your app’s actions matches the `openBoard` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .whiteboard.openBoard)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `openBoard` schema:

```swift
@AppIntent(schema: .whiteboard.openBoard)
struct OpenCanvasBoardIntent: OpenIntent {
    var target: <#CanvasEntity#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var createBoard: some AppSchemaIntent](appschema/whiteboardintent/createboard.md)
  An intent schema that creates a new board.
- [var createItem: some AppSchemaIntent](appschema/whiteboardintent/createitem.md)
  An intent schema that adds an item to a board.
- [var deleteBoard: some AppSchemaIntent](appschema/whiteboardintent/deleteboard.md)
  An intent schema that deletes one or more boards.
- [var deleteItem: some AppSchemaIntent](appschema/whiteboardintent/deleteitem.md)
  An intent schema that deletes the selected canvas items.
- [var updateBoard: some AppSchemaIntent](appschema/whiteboardintent/updateboard.md)
  An intent schema that renames a board.
- [var updateItem: some AppSchemaIntent](appschema/whiteboardintent/updateitem.md)
  An intent schema that updates a board item.
- [AppSchema.WhiteboardIntent](appschema/whiteboardintent.md)
  Identifies intent schemas in the whiteboard domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/whiteboardintent/openboard)*