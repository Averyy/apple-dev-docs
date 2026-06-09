# summarizeMessages

**Framework**: App Intents  
**Kind**: property

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var summarizeMessages: some AssistantSchemas.Intent { get }
```

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent implementation.

For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.

The following example shows an app intent that conforms to the `mail.summarizeMessages` schema:

```swift
@AppIntent(schema: .mail.summarizeMessages)
struct MailSummarizeThread {
    var target: <#UnionValue#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/mailintent/summarizemessages)*