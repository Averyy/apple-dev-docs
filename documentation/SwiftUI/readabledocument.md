# ReadableDocument

**Framework**: SwiftUI  
**Kind**: protocol

A type that you use to read documents from file.

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

To create a read-only document type, conform to `ReadableDocument` and implement the required methods and properties. For a read-write document, also conform to [`WritableDocument`](writabledocument.md), or use the [`Document`](document.md) typealias.

Your implementation:

- Provides readable content types via [`readableContentTypes`](readabledocument/readablecontenttypes.md).
- Loads documents from file using a [`DocumentReader`](documentreader.md) returned by [`reader(configuration:)`](readabledocument/reader(configuration:).md).
- Applies loaded content to your model via [`apply(snapshot:previous:)`](readabledocument/apply(snapshot:previous:).md).

## Topics

### Reading a document
- [static var readableContentTypes: [UTType]](readabledocument/readablecontenttypes.md)
  The file and data types that the document reads from.
- [ReadableDocument.ReadConfiguration](readabledocument/readconfiguration.md)
  The configuration for reading document contents.
- [associatedtype Reader : DocumentReader](readabledocument/reader.md)
  A type that implements reading from disk logic.
- [func reader(configuration: sending Self.ReadConfiguration) -> sending Self.Reader](readabledocument/reader(configuration:).md)
  Creates a value that reads a document from disk.
- [func apply(snapshot: sending Self.Reader.Snapshot, previous: sending Self.Reader.Snapshot?) async throws](readabledocument/apply(snapshot:previous:).md)
  Applies loaded content to the document model.
### Type Properties
- [static var writableContentTypes: [UTType]](readabledocument/writablecontenttypes.md)
  By default, a document that supports reading also supports writing the same content types.

## Relationships

### Inherited By
- [Document](document.md)

## See Also

- [protocol Document](document.md)
- [protocol WritableDocument](writabledocument.md)
  A type that you use to write documents to file.
- [class URLDocumentConfiguration](urldocumentconfiguration.md)
  A set of settings and properties of an open document.
- [struct DocumentCreationContext](documentcreationcontext.md)
  Provides context about how a document was created or opened.
- [protocol DocumentBaseBox](documentbasebox.md)
  A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/readabledocument)*