# showPresenterNotes

**Framework**: App Intents  
**Kind**: property

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst ?+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
var showPresenterNotes: some AssistantSchemas.Intent { get }
```

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent implementation.

For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.

The following example shows an app intent that conforms to the `presentation.showPresenterNotes` schema:

```swift
@AppIntent(schema: .presentation.showPresenterNotes)
struct ShowPresenterNotesIntent {
var presentation: <#PresentationEntity#>
var isVisible: Bool

func perform() async throws -> some IntentResult {
<#code#>
}
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/presentationintent/showpresenternotes)*