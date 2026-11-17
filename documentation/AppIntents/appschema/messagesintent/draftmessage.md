# draftMessage

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that opens app to start or continue composing a message via touch.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var draftMessage: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `messages` domain and one of your app’s actions matches the `draftMessage` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .messages.draftMessage)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `draftMessage` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `messages_draftMessage` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .messages.draftMessage)
struct DraftMessageIntent {
    /// The destination of the message. Can be recipients, or a specific conversation.
    var destination: <#MessageDestination#>?

    /// The subject of the message.
    var subject: AttributedString?

    /// The primary body of the message.
    var content: AttributedString?

    /// Files such as images to be sent with the message.
    var attachments: [IntentFile]

    /// The audio message to send with the message.
    var audioMessage: IntentFile?

    /// Locations to include in the message.
    var locations: [GeoToolbox.PlaceDescriptor]

    /// URLs to include in the message.
    var links: [URL]

    /// The date to send the message, if sent at a later time.
    var scheduledDate: Date?

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

Define a `@UnionValue` enumeration for the `destination` parameter, as in the following example, by typing the first few characters of `messages_destination` in Xcode and selecting it from the code-completion suggestions.

```swift
@UnionValue
enum MessageDestination {
    case people([IntentPerson])
    case messagePerson(<#MessagePerson#>)
    case messagePeople([<#MessagePerson#>])
    case conversation(<#ConversationEntity#>)
}
```

> 💡 **Tip**: Keep the cases that your app supports and remove the rest.

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the draft-message intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `destination` | `@UnionValue?` | Your app | The destination of the message. Can be recipients, or a specific conversation. `MessageDestination` is a placeholder name for the `@UnionValue` type your app defines, as shown in the example above the table. |
| `subject` | `AttributedString?` | Foundation | The subject of the message. |
| `content` | `AttributedString?` | Foundation | The primary body of the message. |
| `attachments` | `[IntentFile]` | App Intents | Files such as images to be sent with the message. |
| `audioMessage` | `IntentFile?` | App Intents | The audio message to send with the message. |
| `locations` | `[GeoToolbox.PlaceDescriptor]` | GeoToolbox | Locations to include in the message. |
| `links` | `[URL]` | Foundation | URLs to include in the message. |
| `scheduledDate` | `Date?` | Foundation | The date to send the message, if sent at a later time. |

## See Also

### Actions
- [var editSentMessage: some AppSchemaIntent](./editsentmessage.md)
  An intent schema that edits an already sent message with new content.
- [var sendMessage: some AppSchemaIntent](./sendmessage.md)
  An intent schema that sends a message with the associated parameters.
- [var setMessageReadStatus: some AppSchemaIntent](./setmessagereadstatus.md)
  An intent schema that changes the message read status to a given value.
- [var unsendMessage: some AppSchemaIntent](./unsendmessage.md)
  An intent schema that unsends a sent message.
- [AppSchema.MessagesIntent](../messagesintent.md)
  Identifies intent schemas in the messages domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/messagesintent/draftmessage)*