# writableContentTypes

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

By default, a document that supports reading also supports writing the same content types.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static var writableContentTypes: [UTType] { get }
```

Available when `Self` conforms to `WritableDocument`.

## See Also

### Reading a document
- [static var readableContentTypes: [UTType]](./readablecontenttypes.md)
  The content types this document can open.
- [ReadableDocument.ReadConfiguration](./readconfiguration.md)
  The configuration for reading document contents.
- [associatedtype Reader : DocumentReader](./reader.md)
  A type that implements reading from disk.
- [func reader(configuration: sending Self.ReadConfiguration) -> sending Self.Reader](./reader%28configuration%29.md)
  Creates a reader to load this document from disk.
- [func apply(snapshot: sending Self.Reader.Snapshot, previous: sending Self.Reader.Snapshot?) async throws](./apply%28snapshot,previous%29.md)
  Applies a loaded snapshot to the document model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/readabledocument/writablecontenttypes)*