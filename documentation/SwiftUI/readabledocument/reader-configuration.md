# reader(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates a reader to load this document from disk.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func reader(configuration: sending Self.ReadConfiguration) -> sending Self.Reader
```

#### Discussion

SwiftUI calls this method each time it needs to read or re-read the document (on open, or when another process changes the file). Return a [`FileWrapperDocumentReader`](filewrapperdocumentreader.md) for cases that don’t require custom reading logic, or a [`DocumentReader`](documentreader.md) for direct URL access.

## Parameters

- `configuration`: The content type of the file being read.

## See Also

- [static var readableContentTypes: [UTType]](readabledocument/readablecontenttypes.md)
  The content types this document can open.
- [ReadableDocument.ReadConfiguration](readabledocument/readconfiguration.md)
  The configuration for reading document contents.
- [associatedtype Reader : DocumentReader](readabledocument/reader.md)
  A type that implements reading from disk.
- [func apply(snapshot: sending Self.Reader.Snapshot, previous: sending Self.Reader.Snapshot?) async throws](readabledocument/apply(snapshot:previous:).md)
  Applies a loaded snapshot to the document model.
- [static var writableContentTypes: [UTType]](readabledocument/writablecontenttypes.md)
  By default, a document that supports reading also supports writing the same content types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/readabledocument/reader(configuration:))*