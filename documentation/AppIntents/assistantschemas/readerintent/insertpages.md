# insertPages

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for inserting a page.

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
var insertPages: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.reader.insertPages` schema:

```swift
@AppIntent(schema: .reader.insertPages)
struct ReaderInsertPagesIntent: AppIntent {
    @Parameter
    var files: [IntentFile]

    @Parameter
    var isAfter: Bool

    @Parameter
    var page: ReaderPageEntity

    func perform() async throws -> some IntentResult {
        return .result()
    }
}
```

For more information about the `.reader` app intent domain, see [`Reader`](app-schema-domain-reader.md). For general information about app intent domains, see [`Making actions and content discoverable by Apple Intelligence`](making-actions-and-content-discoverable-by-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/readerintent/insertpages)*