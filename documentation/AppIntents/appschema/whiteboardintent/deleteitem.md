# deleteItem

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that deletes the selected canvas items.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var deleteItem: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `whiteboard` domain and one of your app’s actions matches the `deleteItem` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .whiteboard.deleteItem)` Swift macro.

The following example shows an intent that conforms to the `deleteItem` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `whiteboard_deleteItem` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .whiteboard.deleteItem)
struct DeleteCanvasItemIntent: DeleteIntent {
    /// Board items to delete.
    var entities: [<#CanvasItemEntity#>]

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the delete-item intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `entities` | `[@AppEntity(schema: .whiteboard.item)]` | Your app | Board items to delete. `CanvasItemEntity` is a placeholder name for a type that conforms to the [`item`](../whiteboardentity/item.md) entity schema, which your app defines and implements. |

## See Also

### Actions
- [var createBoard: some AppSchemaIntent](./createboard.md)
  An intent schema that creates a new board.
- [var createItem: some AppSchemaIntent](./createitem.md)
  An intent schema that adds an item to a board.
- [var deleteBoard: some AppSchemaIntent](./deleteboard.md)
  An intent schema that deletes one or more boards.
- [var openBoard: some AppSchemaIntent](./openboard.md)
  An intent schema that opens an existing board.
- [var updateBoard: some AppSchemaIntent](./updateboard.md)
  An intent schema that renames a board.
- [var updateItem: some AppSchemaIntent](./updateitem.md)
  An intent schema that updates a board item.
- [AppSchema.WhiteboardIntent](../whiteboardintent.md)
  Identifies intent schemas in the whiteboard domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/whiteboardintent/deleteitem)*