# readableContentTypes

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

The file and data types that the document reads from.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var readableContentTypes: [UTType] { get }
```

## See Also

- [ReadableDocument.ReadConfiguration](readabledocument/readconfiguration.md)
  The configuration for reading document contents.
- [associatedtype Reader : DocumentReader](readabledocument/reader.md)
  A type that implements reading from disk logic.
- [func reader(configuration: sending Self.ReadConfiguration) -> sending Self.Reader](readabledocument/reader(configuration:).md)
  Creates a value that reads a document from disk.
- [func apply(snapshot: sending Self.Reader.Snapshot, previous: sending Self.Reader.Snapshot?) async throws](readabledocument/apply(snapshot:previous:).md)
  Applies loaded content to the document model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/readabledocument/readablecontenttypes)*