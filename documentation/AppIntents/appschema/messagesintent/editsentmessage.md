# editSentMessage

**Framework**: App Intents  
**Kind**: property

An intent schema that edits an already sent message with new content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var editSentMessage: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `messages` domain and one of your app’s actions matches the `editSentMessage` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .messages.editSentMessage)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `editSentMessage` schema:

```swift
@AppIntent(schema: .messages.editSentMessage)
struct EditSentMessageIntent {
    var message: <#MessageEntity#>
    var content: AttributedString

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var draftMessage: some AppSchemaIntent](appschema/messagesintent/draftmessage.md)
  An intent schema that opens app to start or continue composing a message via touch.
- [var sendMessage: some AppSchemaIntent](appschema/messagesintent/sendmessage.md)
  An intent schema that sends a message with the associated parameters.
- [var setMessageReadStatus: some AppSchemaIntent](appschema/messagesintent/setmessagereadstatus.md)
  An intent schema that changes the message read status to a given value.
- [var unsendMessage: some AppSchemaIntent](appschema/messagesintent/unsendmessage.md)
  An intent schema that unsends a sent message.
- [AppSchema.MessagesIntent](appschema/messagesintent.md)
  Identifies intent schemas in the messages domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/messagesintent/editsentmessage)*