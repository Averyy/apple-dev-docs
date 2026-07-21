# activate

**Framework**: App Intents  
**Kind**: property

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
var activate: some AssistantSchemas.Intent { get }
```

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent implementation.

For general information about app intent domains, see [`Making actions and content discoverable by Apple Intelligence`](making-actions-and-content-discoverable-by-apple-intelligence.md).

The following example shows an app intent that conforms to the `assistant.activate` schema:

```swift
@AppIntent(schema: .assistant.activate)
struct ActivateAssistantIntent {
    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/assistantintent/activate)*