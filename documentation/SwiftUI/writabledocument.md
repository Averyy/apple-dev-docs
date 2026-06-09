# WritableDocument

**Framework**: SwiftUI  
**Kind**: protocol

A type that you use to write documents to file.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol WritableDocument : AnyObject
```

#### Overview

Conform to `WritableDocument` in addition to [`ReadableDocument`](readabledocument.md) to support saving. You can also conform your type to `Document` protocol which conforms both to `WritableDocument` and `ReadableDocument`.

Your implementation:

- Provides writable content types via [`writableContentTypes`](writabledocument/writablecontenttypes.md).
- Provides a snapshot of the current document state via [`snapshot(contentType:)`](writabledocument/snapshot(contenttype:).md).
- Writes the snapshot to disk using a [`DocumentWriter`](documentwriter.md) returned by [`writer(configuration:)`](writabledocument/writer(configuration:).md).

## Topics

### Writing a document
- [static var writableContentTypes: [UTType]](writabledocument/writablecontenttypes.md)
  The file types that the document supports saving or exporting to.
- [WritableDocument.WriteConfiguration](writabledocument/writeconfiguration.md)
  The configuration for writing document contents.
- [associatedtype Writer : DocumentWriter](writabledocument/writer.md)
  A type that implements writing to disk logic.
- [func writer(configuration: sending Self.WriteConfiguration) -> sending Self.Writer](writabledocument/writer(configuration:).md)
  Creates a value that writes a document to disk.
- [func snapshot(contentType: UTType) async throws -> sending Self.Writer.Snapshot](writabledocument/snapshot(contenttype:).md)
  Creates a snapshot of the document’s current state to be saved.

## See Also

- [protocol ReadableDocument](readabledocument.md)
  A type that you use to read documents from file.
- [class URLDocumentConfiguration](urldocumentconfiguration.md)
  A set of settings and properties of an open document.
- [struct DocumentCreationContext](documentcreationcontext.md)
  Provides context about how a document was created or opened.
- [protocol DocumentBaseBox](documentbasebox.md)
  A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/writabledocument)*