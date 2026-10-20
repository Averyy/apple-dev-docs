# apply(snapshot:previous:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Applies a loaded snapshot to the document model.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
func apply(snapshot: sending Self.Reader.Snapshot, previous: sending Self.Reader.Snapshot?) async throws
```

#### Discussion

SwiftUI calls this on the main actor after the reader’s [`read(from:progress:)`](../documentreader/read%28from,progress%29.md) completes. Update your model properties here. Keep this method lightweight — all deserialization should happen in the reader.

## Parameters

- `snapshot`: The content loaded from disk.
- `previous`: The previously loaded snapshot, or `nil` on the first read. Use it to apply incremental updates.

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
- [static var writableContentTypes: [UTType]](./writablecontenttypes.md)
  By default, a document that supports reading also supports writing the same content types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/readabledocument/apply(snapshot:previous:))*