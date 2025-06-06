# updateMail

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for updating email messages.

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
var updateMail: some AssistantSchemas.Intent { get }
```

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent implementation.

For more information about the `.mail` app intent domain, see [`Making email actions available to Siri and Apple Intelligence`](making-email-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

The following example shows an app intent that conforms to the `.mail.updateMail` schema:

```swift
@AssistantIntent(schema: .mail.updateMail)
struct UpdateMailIntent: AppIntent {
    @Parameter
    var target: [MailMessageEntity]

    @Parameter
    var isRead: Bool?

    @Parameter
    var isFlagged: Bool?

    @Parameter
    var isJunk: Bool?

    @Parameter
    var mailbox: MailboxEntity?

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/intentschema/updatemail)*