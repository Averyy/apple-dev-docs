# rotateDocuments

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for rotating a document.

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
var rotateDocuments: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.reader.rotateDocuments` schema:

```swift
@AssistantIntent(schema: .reader.rotateDocuments)
struct ReaderRotateDocumentsIntent: AppIntent {
    @Parameter
    var documents: [ReaderDocumentEntity]

    @Parameter
    var isClockwise: Bool

    func perform() async throws -> some IntentResult & ReturnsValue<[ReaderDocumentEntity]> {
        return .result(value: [ReaderDocumentEntity()])
    }
}
```

For more information about the `.reader` app intent domain, see [`Making document reader actions available to Siri and Apple Intelligence`](making-document-reader-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschema/intentschema/rotatedocuments)*