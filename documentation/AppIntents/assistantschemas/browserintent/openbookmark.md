# openBookmark

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the Assistant schema for opening a bookmarked URL.

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
var openBookmark: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.browser.openBookmark` schema:

```swift
@AssistantIntent(schema: .browser.openBookmark)
struct OpenBookmarkIntent: OpenIntent {
    @Parameter
    var tab: TabEntity?

    @Parameter
    var target: BookmarkEntity

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/browserintent/openbookmark)*