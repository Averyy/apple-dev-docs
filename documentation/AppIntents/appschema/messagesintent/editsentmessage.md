# editSentMessage

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that edits an already sent message with new content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var editSentMessage: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `messages` domain and one of your app’s actions matches the `editSentMessage` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .messages.editSentMessage)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `editSentMessage` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `messages_editSentMessage` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .messages.editSentMessage)
struct EditSentMessageIntent {
    /// The message to edit.
    var message: <#MessageEntity#>

    /// The new content to replace the original content with.
    var content: AttributedString

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the edit-sent-message intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `message` | `@AppEntity(schema: .messages.message)` | Your app | The message to edit. `MessageEntity` is a placeholder name for a type that conforms to the [`message`](../messagesentity/message.md) entity schema, which your app defines and implements. |
| `content` | `AttributedString` | Foundation | The new content to replace the original content with. |

## See Also

### Actions
- [var draftMessage: some AppSchemaIntent](./draftmessage.md)
  An intent schema that opens app to start or continue composing a message via touch.
- [var sendMessage: some AppSchemaIntent](./sendmessage.md)
  An intent schema that sends a message with the associated parameters.
- [var setMessageReadStatus: some AppSchemaIntent](./setmessagereadstatus.md)
  An intent schema that changes the message read status to a given value.
- [var unsendMessage: some AppSchemaIntent](./unsendmessage.md)
  An intent schema that unsends a sent message.
- [AppSchema.MessagesIntent](../messagesintent.md)
  Identifies intent schemas in the messages domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/messagesintent/editsentmessage)*