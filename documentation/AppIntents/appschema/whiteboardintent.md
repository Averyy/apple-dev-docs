# AppSchema.WhiteboardIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies intent schemas in the whiteboard domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol WhiteboardIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var createBoard: some AppSchemaIntent](./whiteboardintent/createboard.md)
  An intent schema that creates a new board.
- [var createItem: some AppSchemaIntent](./whiteboardintent/createitem.md)
  An intent schema that adds an item to a board.
- [var deleteBoard: some AppSchemaIntent](./whiteboardintent/deleteboard.md)
  An intent schema that deletes one or more boards.
- [var deleteItem: some AppSchemaIntent](./whiteboardintent/deleteitem.md)
  An intent schema that deletes the selected canvas items.
- [var openBoard: some AppSchemaIntent](./whiteboardintent/openboard.md)
  An intent schema that opens an existing board.
- [var updateBoard: some AppSchemaIntent](./whiteboardintent/updateboard.md)
  An intent schema that renames a board.
- [var updateItem: some AppSchemaIntent](./whiteboardintent/updateitem.md)
  An intent schema that updates a board item.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Intent](./intent.md)

## See Also

### Actions
- [var createBoard: some AppSchemaIntent](./whiteboardintent/createboard.md)
  An intent schema that creates a new board.
- [var createItem: some AppSchemaIntent](./whiteboardintent/createitem.md)
  An intent schema that adds an item to a board.
- [var deleteBoard: some AppSchemaIntent](./whiteboardintent/deleteboard.md)
  An intent schema that deletes one or more boards.
- [var deleteItem: some AppSchemaIntent](./whiteboardintent/deleteitem.md)
  An intent schema that deletes the selected canvas items.
- [var openBoard: some AppSchemaIntent](./whiteboardintent/openboard.md)
  An intent schema that opens an existing board.
- [var updateBoard: some AppSchemaIntent](./whiteboardintent/updateboard.md)
  An intent schema that renames a board.
- [var updateItem: some AppSchemaIntent](./whiteboardintent/updateitem.md)
  An intent schema that updates a board item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/whiteboardintent)*