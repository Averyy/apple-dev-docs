# bookmarkURL

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for creating a bookmark for a URL.

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
var bookmarkURL: some AssistantSchemas.Intent { get }
```

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent implementation.

For more information about the `.browser` app intent domain, see [`Making browser actions available to Siri and Apple Intelligence`](making-browser-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

The following example shows an app intent that conforms to the `.browser.bookmarkURL` schema:

```swift
@AssistantIntent(schema: .browser.bookmarkURL)
struct BookmarkURLIntent: AppIntent {
    @Parameter
    var name: String?

    @Parameter
    var url: URL

    func perform() async throws -> some ReturnsValue<BookmarkEntity> {
        .result(value: BookmarkEntity())
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/browserintent/bookmarkurl)*