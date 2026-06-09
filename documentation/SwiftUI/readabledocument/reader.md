# Reader

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Required**: Yes

A type that implements reading from disk logic.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
associatedtype Reader : DocumentReader
```

## See Also

- [static var readableContentTypes: [UTType]](readabledocument/readablecontenttypes.md)
  The file and data types that the document reads from.
- [ReadableDocument.ReadConfiguration](readabledocument/readconfiguration.md)
  The configuration for reading document contents.
- [func reader(configuration: sending Self.ReadConfiguration) -> sending Self.Reader](readabledocument/reader(configuration:).md)
  Creates a value that reads a document from disk.
- [func apply(snapshot: sending Self.Reader.Snapshot, previous: sending Self.Reader.Snapshot?) async throws](readabledocument/apply(snapshot:previous:).md)
  Applies loaded content to the document model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/readabledocument/reader)*