# AssistantSchemas.WhiteboardIntent

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app intents that offer whiteboard functionality.

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
protocol WhiteboardIntent : AssistantSchemas.Model
```

## Mentions

- [Making whiteboard actions available to Siri and Apple Intelligence](making-whiteboard-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var createBoard: some AssistantSchemas.Intent](assistantschemas/whiteboardintent/createboard.md)
  The app intent conforms to the schema for creating a new whiteboard canvas.
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

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.IntentSchema](assistantschema/intentschema.md)
- [AssistantSchemas.IntentSchema](assistantschemas/intentschema.md)

## See Also

- [Making whiteboard actions available to Siri and Apple Intelligence](making-whiteboard-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities that make your app’s whiteboard functionality available to Siri and Apple Intelligence.
- [AssistantSchemas.WhiteboardEntity](assistantschemas/whiteboardentity.md)
  Assistant schema conformance for app entities that describe data for whiteboard functionality.
- [AssistantSchemas.WhiteboardEnum](assistantschemas/whiteboardenum.md)
  Assistant schema conformance for whiteboard types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/whiteboardintent)*