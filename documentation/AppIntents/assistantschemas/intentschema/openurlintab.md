# openURLInTab

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the Assistant schema for loading a URL in a browser tab.

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
var openURLInTab: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.browser.openURLInTab` schema:

```swift
@AssistantIntent(schema: .browser.openURLInTab)
struct LoadURLInTabIntent: AppIntent {
    @Parameter
    var tab: TabEntity

    @Parameter
    var url: URL

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

For more information about the `.browser` app intent domain, see [`Making browser actions available to Siri and Apple Intelligence`](making-browser-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/intentschema/openurlintab)*