# documentKind

**Framework**: App Intents  
**Kind**: property

The file type for a document.

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
var documentKind: some AssistantSchemas.Enum { get }
```

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app enum implementation.

For more information about the `.reader` app intent domain, see [`Making document reader actions available to Siri and Apple Intelligence`](making-document-reader-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

The following example shows an app enum that conforms to the `.reader.documentKind` schema:

```swift
@AssistantEnum(schema: .reader.documentKind)
enum ReaderDocumentKind: AppEnum, Codable {
    case image
    case pdf

    static var caseDisplayRepresentations: [Self: DisplayRepresentation] {
        [
            .image: .init(title: "Image", image: .init(systemName: "photo")),
            .pdf: .init(title: "PDF", image: .init(systemName: "doc.text")),
        ]
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/enumschema/documentkind)*