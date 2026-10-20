# AppSchema.MessagesIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies intent schemas in the messages domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol MessagesIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var draftMessage: some AppSchemaIntent](./messagesintent/draftmessage.md)
  An intent schema that opens app to start or continue composing a message via touch.
- [var editSentMessage: some AppSchemaIntent](./messagesintent/editsentmessage.md)
  An intent schema that edits an already sent message with new content.
- [var sendMessage: some AppSchemaIntent](./messagesintent/sendmessage.md)
  An intent schema that sends a message with the associated parameters.
- [var setMessageReadStatus: some AppSchemaIntent](./messagesintent/setmessagereadstatus.md)
  An intent schema that changes the message read status to a given value.
- [var unsendMessage: some AppSchemaIntent](./messagesintent/unsendmessage.md)
  An intent schema that unsends a sent message.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Intent](./intent.md)

## See Also

### Actions
- [var draftMessage: some AppSchemaIntent](./messagesintent/draftmessage.md)
  An intent schema that opens app to start or continue composing a message via touch.
- [var editSentMessage: some AppSchemaIntent](./messagesintent/editsentmessage.md)
  An intent schema that edits an already sent message with new content.
- [var sendMessage: some AppSchemaIntent](./messagesintent/sendmessage.md)
  An intent schema that sends a message with the associated parameters.
- [var setMessageReadStatus: some AppSchemaIntent](./messagesintent/setmessagereadstatus.md)
  An intent schema that changes the message read status to a given value.
- [var unsendMessage: some AppSchemaIntent](./messagesintent/unsendmessage.md)
  An intent schema that unsends a sent message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/messagesintent)*