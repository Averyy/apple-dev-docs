# AppSchema.WhiteboardIntent

**Framework**: App Intents  
**Kind**: protocol

Identifies intent schemas in the whiteboard domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol WhiteboardIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var createBoard: some AppSchemaIntent](appschema/whiteboardintent/createboard.md)
  An intent schema that creates a new board.
- [var createItem: some AppSchemaIntent](appschema/whiteboardintent/createitem.md)
  An intent schema that adds an item to a board.
- [var deleteBoard: some AppSchemaIntent](appschema/whiteboardintent/deleteboard.md)
  An intent schema that deletes one or more boards.
- [var deleteItem: some AppSchemaIntent](appschema/whiteboardintent/deleteitem.md)
  An intent schema that deletes the selected canvas items.
- [var openBoard: some AppSchemaIntent](appschema/whiteboardintent/openboard.md)
  An intent schema that opens an existing board.
- [var updateBoard: some AppSchemaIntent](appschema/whiteboardintent/updateboard.md)
  An intent schema that renames a board.
- [var updateItem: some AppSchemaIntent](appschema/whiteboardintent/updateitem.md)
  An intent schema that updates a board item.

## Relationships

### Inherits From
- [AppSchema.Kind](appschema/kind.md)
### Conforming Types
- [AppSchema.Intent](appschema/intent.md)

## See Also

- [var createBoard: some AppSchemaIntent](appschema/whiteboardintent/createboard.md)
  An intent schema that creates a new board.
- [var createItem: some AppSchemaIntent](appschema/whiteboardintent/createitem.md)
  An intent schema that adds an item to a board.
- [var deleteBoard: some AppSchemaIntent](appschema/whiteboardintent/deleteboard.md)
  An intent schema that deletes one or more boards.
- [var deleteItem: some AppSchemaIntent](appschema/whiteboardintent/deleteitem.md)
  An intent schema that deletes the selected canvas items.
- [var openBoard: some AppSchemaIntent](appschema/whiteboardintent/openboard.md)
  An intent schema that opens an existing board.
- [var updateBoard: some AppSchemaIntent](appschema/whiteboardintent/updateboard.md)
  An intent schema that renames a board.
- [var updateItem: some AppSchemaIntent](appschema/whiteboardintent/updateitem.md)
  An intent schema that updates a board item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/whiteboardintent)*