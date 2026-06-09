# open

**Framework**: App Intents  
**Kind**: property

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var open: some AssistantSchemas.Intent { get }
```

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent implementation.

For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.

The following example shows an app intent that conforms to the `system.open` schema:

```swift
@AppIntent(schema: .system.open)
struct OpenIntent: OpenIntent {
    var target: <#any AppEntity#>
    
    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/systemintent/open)*