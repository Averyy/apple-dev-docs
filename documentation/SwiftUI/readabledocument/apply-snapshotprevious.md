# apply(snapshot:previous:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Applies loaded content to the document model.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
func apply(snapshot: sending Self.Reader.Snapshot, previous: sending Self.Reader.Snapshot?) async throws
```

#### Discussion

SwiftUI calls this method on the main actor after reading completes.

## Parameters

- `snapshot`: The snapshot loaded from disk.
- `previous`: The previously loaded snapshot. Compare to `snapshot` to update only what changed.

## See Also

- [static var readableContentTypes: [UTType]](readabledocument/readablecontenttypes.md)
  The file and data types that the document reads from.
- [ReadableDocument.ReadConfiguration](readabledocument/readconfiguration.md)
  The configuration for reading document contents.
- [associatedtype Reader : DocumentReader](readabledocument/reader.md)
  A type that implements reading from disk logic.
- [func reader(configuration: sending Self.ReadConfiguration) -> sending Self.Reader](readabledocument/reader(configuration:).md)
  Creates a value that reads a document from disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/readabledocument/apply(snapshot:previous:))*