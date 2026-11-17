# createItem

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that adds an item to a board.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var createItem: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `whiteboard` domain and one of your app’s actions matches the `createItem` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .whiteboard.createItem)` Swift macro.

The following example shows an intent that conforms to the `createItem` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `whiteboard_createItem` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .whiteboard.createItem)
struct CreateCanvasItemIntent {
    /// Board to add the item to.
    var target: <#CanvasEntity#>

    /// Type of the added item.
    var itemType: <#CanvasItemType#>?

    /// Text to add.
    var text: AttributedString?

    /// Media to add.
    var mediaItems: [IntentFile]

    /// URL to add.
    var url: URL?

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the create-item intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `target` | `@AppEntity(schema: .whiteboard.board)` | Your app | Board to add the item to. `CanvasEntity` is a placeholder name for a type that conforms to the [`board`](../whiteboardentity/board.md) entity schema, which your app defines and implements. |
| `itemType` | `@AppEnum(schema: .whiteboard.itemType)?` | Your app | Type of the added item. `CanvasItemType` is a placeholder name for a type that conforms to the [`itemType`](../whiteboardenum/itemtype.md) enum schema, which your app defines and implements. |
| `text` | `AttributedString?` | Foundation | Text to add. |
| `mediaItems` | `[IntentFile]` | App Intents | Media to add. |
| `url` | `URL?` | Foundation | URL to add. |

## See Also

### Actions
- [var createBoard: some AppSchemaIntent](./createboard.md)
  An intent schema that creates a new board.
- [var deleteBoard: some AppSchemaIntent](./deleteboard.md)
  An intent schema that deletes one or more boards.
- [var deleteItem: some AppSchemaIntent](./deleteitem.md)
  An intent schema that deletes the selected canvas items.
- [var openBoard: some AppSchemaIntent](./openboard.md)
  An intent schema that opens an existing board.
- [var updateBoard: some AppSchemaIntent](./updateboard.md)
  An intent schema that renames a board.
- [var updateItem: some AppSchemaIntent](./updateitem.md)
  An intent schema that updates a board item.
- [AppSchema.WhiteboardIntent](../whiteboardintent.md)
  Identifies intent schemas in the whiteboard domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/whiteboardintent/createitem)*