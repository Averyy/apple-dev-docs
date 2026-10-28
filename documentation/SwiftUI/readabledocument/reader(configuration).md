# reader(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a reader to load this document from disk.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func reader(configuration: sending Self.ReadConfiguration) -> sending Self.Reader
```

## Discussion

SwiftUI calls this method each time it needs to read or re-read the document (on open, or when another process changes the file). Return a [`FileWrapperDocumentReader`](../filewrapperdocumentreader.md) for cases that don’t require custom reading logic, or a [`DocumentReader`](../documentreader.md) for direct URL access.

## Parameters

- `configuration`: The content type of the file being read.

## See Also

### Reading a document
- [static var readableContentTypes: [UTType]](./readablecontenttypes.md)
  The content types this document can open.
- [ReadableDocument.ReadConfiguration](./readconfiguration.md)
  The configuration for reading document contents.
- [associatedtype Reader : DocumentReader](./reader.md)
  A type that implements reading from disk.
- [func apply(snapshot: sending Self.Reader.Snapshot, previous: sending Self.Reader.Snapshot?) async throws](./apply%28snapshot,previous%29.md)
  Applies a loaded snapshot to the document model.
- [static var writableContentTypes: [UTType]](./writablecontenttypes.md)
  By default, a document that supports reading also supports writing the same content types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/readabledocument/reader(configuration:))*