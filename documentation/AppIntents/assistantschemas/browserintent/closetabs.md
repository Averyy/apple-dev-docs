# closeTabs

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for closing a browser tab.

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
var closeTabs: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.browser.closeTabs` schema:

```swift
@AppIntent(schema: .browser.closeTabs)
struct CloseTabsIntent: AppIntent {
    @Parameter
    var target: [TabEntity]

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

For more information about the `.browser` app intent domain, see doc:Making-browser-actions-available-to-siri-and-apple-intelligence. For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/browserintent/closetabs)*