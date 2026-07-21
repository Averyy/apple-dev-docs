# ReadableDocument

**Framework**: SwiftUI  
**Kind**: protocol

A document type that supports reading from file.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol ReadableDocument : AnyObject
```

#### Overview

Conform to `ReadableDocument` to build a read-only document viewer, or combine with [`WritableDocument`](writabledocument.md) (via the [`Document`](document.md) protocol) for full read-write support.

A readable document is a reference type so that SwiftUI can maintain a stable identity across updates. Use `@Observable` to enable per-property change tracking:

```swift
@Observable
final class MarkdownViewer: ReadableDocument {
    static let readableContentTypes: [UTType] = [.markdown]

    var attributedText = AttributedString()

    func reader(configuration: sending ReadConfiguration) -> sending FileWrapperDocumentReader<String> {
        FileWrapperDocumentReader(configuration) { fileWrapper in
            guard let data =
                fileWrapper.regularFileContents else {
                throw CocoaError(.fileReadCorruptFile)
            }
            return String(decoding: data, as: UTF8.self)
        }
    }

    @MainActor
    func apply(snapshot: sending String, previous: sending String?) async throws {
        attributedText = try AttributedString(
            markdown: snapshot
        )
    }
}
```

Present a read-only document with [`DocumentGroup`](documentgroup.md) using the viewer initializer:

```swift
DocumentGroup { document in
    MarkdownView(document: document)
} makeReadableDocument: { configuration, context in
    MarkdownViewer()
}
```

Set `CFBundleTypeRole` to `Viewer` in your Info.plist for read-only document types.

## Topics

### Reading a document
- [static var readableContentTypes: [UTType]](readabledocument/readablecontenttypes.md)
  The content types this document can open.
- [ReadableDocument.ReadConfiguration](readabledocument/readconfiguration.md)
  The configuration for reading document contents.
- [associatedtype Reader : DocumentReader](readabledocument/reader.md)
  A type that implements reading from disk.
- [func reader(configuration: sending Self.ReadConfiguration) -> sending Self.Reader](readabledocument/reader(configuration:).md)
  Creates a reader to load this document from disk.
- [func apply(snapshot: sending Self.Reader.Snapshot, previous: sending Self.Reader.Snapshot?) async throws](readabledocument/apply(snapshot:previous:).md)
  Applies a loaded snapshot to the document model.
- [static var writableContentTypes: [UTType]](readabledocument/writablecontenttypes.md)
  By default, a document that supports reading also supports writing the same content types.

## Relationships

### Inherited By
- [Document](document.md)

## See Also

- [protocol Document](document.md)
  A document that supports both reading and writing.
- [protocol WritableDocument](writabledocument.md)
  A document type that supports writing to file.
- [class URLDocumentConfiguration](urldocumentconfiguration.md)
  The configuration of an open document that stores its file URL, last modification date, and related metadata.
- [struct DocumentCreationContext](documentcreationcontext.md)
  Context about how a document was created.
- [protocol DocumentBaseBox](documentbasebox.md)
  A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/readabledocument)*