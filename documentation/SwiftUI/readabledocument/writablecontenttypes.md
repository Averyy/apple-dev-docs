# writableContentTypes

**Framework**: SwiftUI  
**Kind**: property

By default, a document that supports reading also supports writing the same content types.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var writableContentTypes: [UTType] { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/readabledocument/writablecontenttypes)*