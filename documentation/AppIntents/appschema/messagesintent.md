# AppSchema.MessagesIntent

**Framework**: App Intents  
**Kind**: protocol

Identifies intent schemas in the messages domain.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol MessagesIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var draftMessage: some AppSchemaIntent](appschema/messagesintent/draftmessage.md)
  An intent schema that opens app to start or continue composing a message via touch.
- [var editSentMessage: some AppSchemaIntent](appschema/messagesintent/editsentmessage.md)
  An intent schema that edits an already sent message with new content.
- [var sendMessage: some AppSchemaIntent](appschema/messagesintent/sendmessage.md)
  An intent schema that sends a message with the associated parameters.
- [var setMessageReadStatus: some AppSchemaIntent](appschema/messagesintent/setmessagereadstatus.md)
  An intent schema that changes the message read status to a given value.
- [var unsendMessage: some AppSchemaIntent](appschema/messagesintent/unsendmessage.md)
  An intent schema that unsends a sent message.

## Relationships

### Inherits From
- [AppSchema.Kind](appschema/kind.md)
### Conforming Types
- [AppSchema.Intent](appschema/intent.md)

## See Also

- [var draftMessage: some AppSchemaIntent](appschema/messagesintent/draftmessage.md)
  An intent schema that opens app to start or continue composing a message via touch.
- [var editSentMessage: some AppSchemaIntent](appschema/messagesintent/editsentmessage.md)
  An intent schema that edits an already sent message with new content.
- [var sendMessage: some AppSchemaIntent](appschema/messagesintent/sendmessage.md)
  An intent schema that sends a message with the associated parameters.
- [var setMessageReadStatus: some AppSchemaIntent](appschema/messagesintent/setmessagereadstatus.md)
  An intent schema that changes the message read status to a given value.
- [var unsendMessage: some AppSchemaIntent](appschema/messagesintent/unsendmessage.md)
  An intent schema that unsends a sent message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/messagesintent)*