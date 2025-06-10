# navigatePage

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for navigating to a specific page of an ebook.

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
var navigatePage: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.books.navigatePage` schema:

```swift
@AssistantIntent(schema: .books.navigatePage)
struct NavigateBookPageIntent: AppIntent {
    @Parameter
    var target: BookEntity

    @Parameter
    var direction: BookNavigationDirection

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

For more information about the `.books` app intent domain, see [`Making ebook actions available to Siri and Apple Intelligence`](making-ebook-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/booksintent/navigatepage)*