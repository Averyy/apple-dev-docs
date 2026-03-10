# rotatePages

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for rotating a page.

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
var rotatePages: some AssistantSchemas.Intent { get }
```

## Mentions

- [Making document reader actions available to Siri and Apple Intelligence](making-document-reader-actions-available-to-siri-and-apple-intelligence.md)

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.reader.rotatePages` schema:

```swift
@AppIntent(schema: .reader.rotatePages)
struct ReaderRotatePagesIntent: AppIntent {
    @Parameter
    var pages: [ReaderPageEntity]

    @Parameter
    var isClockwise: Bool

    func perform() async throws -> some IntentResult & ReturnsValue<[ReaderPageEntity]> {
        return .result(value: [ReaderPageEntity()])
    }
}
```

For more information about the `.reader` app intent domain, see [`Making document reader actions available to Siri and Apple Intelligence`](making-document-reader-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

## See Also

- [var deletePages: some AssistantSchemas.Intent](assistantschemas/readerintent/deletepages.md)
  The app intent conforms to the schema for deleting a page.
- [var enhanceDocuments: some AssistantSchemas.Intent](assistantschemas/readerintent/enhancedocuments.md)
  The app intent conforms to the schema for enhancing a document.
- [var insertPages: some AssistantSchemas.Intent](assistantschemas/readerintent/insertpages.md)
  The app intent conforms to the schema for inserting a page.
- [var openDocument: some AssistantSchemas.Intent](assistantschemas/readerintent/opendocument.md)
  The app intent conforms to the schema for opening a text document.
- [var openPage: some AssistantSchemas.Intent](assistantschemas/readerintent/openpage.md)
  The app intent conforms to the schema for opening a document.
- [var resizeDocuments: some AssistantSchemas.Intent](assistantschemas/readerintent/resizedocuments.md)
  The app intent conforms to the schema for resizing a document.
- [var rotateDocuments: some AssistantSchemas.Intent](assistantschemas/readerintent/rotatedocuments.md)
  The app intent conforms to the schema for rotating a document.
- [var searchDocuments: some AssistantSchemas.Intent](assistantschemas/readerintent/searchdocuments.md)
  The app intent conforms to the schema for searching in a document.
- [AssistantSchemas.ReaderIntent](assistantschemas/readerintent.md)
  Assistant schema conformance for app intents that offer document viewing and editing functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/readerintent/rotatepages)*