# replyMail

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for replying to an email message.

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
var replyMail: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.mail.replyMail` schema:

```swift
@AppIntent(schema: .mail.replyMail)
struct ReplyMailIntent: AppIntent {
    @Parameter
    var to: [IntentPerson]

    @Parameter
    var cc: [IntentPerson]

    @Parameter
    var bcc: [IntentPerson]

    @Parameter
    var subject: String?

    @Parameter
    var body: AttributedString?

    @Parameter
    var account: MailAccountEntity?

    @Parameter
    var attachments: [IntentFile]

    @Parameter
    var isReplyAll: Bool

    @Parameter
    var target: MailMessageEntity

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

For more information about the `.mail` app intent domain, see doc:Making-email-actions-available-to-siri-and-apple-intelligence. For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/mailintent/replymail)*