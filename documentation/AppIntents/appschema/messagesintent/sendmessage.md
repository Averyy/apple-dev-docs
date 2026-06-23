# sendMessage

**Framework**: App Intents  
**Kind**: property

An intent schema that sends a message with the associated parameters.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var sendMessage: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `messages` domain and one of your app’s actions matches the `sendMessage` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .messages.sendMessage)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `sendMessage` schema:

```swift
@AppIntent(schema: .messages.sendMessage)
struct SendMessageIntent {
    var content: AttributedString?
    var destination: <#MessageDestination#>
    var subject: AttributedString?
    var attachments: [IntentFile]
    var audioMessage: IntentFile?
    var locations: [GeoToolbox.PlaceDescriptor]
    var links: [URL]
    var scheduledDate: Date?

    func perform() async throws -> some ReturnsValue<[<#MessageEntity#>]> {
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
- [var editSentMessage: some AppSchemaIntent](appschema/messagesintent/editsentmessage.md)
  An intent schema that edits an already sent message with new content.
- [var setMessageReadStatus: some AppSchemaIntent](appschema/messagesintent/setmessagereadstatus.md)
  An intent schema that changes the message read status to a given value.
- [var unsendMessage: some AppSchemaIntent](appschema/messagesintent/unsendmessage.md)
  An intent schema that unsends a sent message.
- [AppSchema.MessagesIntent](appschema/messagesintent.md)
  Identifies intent schemas in the messages domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/messagesintent/sendmessage)*