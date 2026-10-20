# AssistantSchemas.WhiteboardIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Assistant schema conformance for app intents that offer whiteboard functionality.

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
protocol WhiteboardIntent : AssistantSchemas.Model
```

## Topics

### Instance Properties
- [var createBoard: some AssistantSchemas.Intent](./whiteboardintent/createboard.md)
  The app intent conforms to the schema for creating a new whiteboard canvas.
- [var createItem: some AssistantSchemas.Intent](./whiteboardintent/createitem.md)
  The app intent conforms to the schema for creating an item on a whiteboard canvas.
- [var deleteBoard: some AssistantSchemas.Intent](./whiteboardintent/deleteboard.md)
  The app intent conforms to the schema for deleting a whiteboard canvas.
- [var deleteItem: some AssistantSchemas.Intent](./whiteboardintent/deleteitem.md)
  The app intent conforms to the schema for deleting an item on a whiteboard canvas.
- [var openBoard: some AssistantSchemas.Intent](./whiteboardintent/openboard.md)
  The app intent conforms to the schema for opening a new whiteboard canvas.
- [var updateBoard: some AssistantSchemas.Intent](./whiteboardintent/updateboard.md)
  The app intent conforms to the schema for updating a whiteboard canvas.
- [var updateItem: some AssistantSchemas.Intent](./whiteboardintent/updateitem.md)
  The app intent conforms to the schema for updating an item on a whiteboard canvas.

## Relationships

### Inherits From
- [AssistantSchemas.Model](./model.md)
### Conforming Types
- [AssistantSchema.IntentSchema](../assistantschema/intentschema.md)
- [AssistantSchemas.IntentSchema](./intentschema.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/whiteboardintent)*