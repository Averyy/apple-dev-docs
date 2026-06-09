# reader(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates a value that reads a document from disk.

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

## Parameters

- `configuration`: Additional context for reading.

## See Also

- [static var readableContentTypes: [UTType]](readabledocument/readablecontenttypes.md)
  The file and data types that the document reads from.
- [ReadableDocument.ReadConfiguration](readabledocument/readconfiguration.md)
  The configuration for reading document contents.
- [associatedtype Reader : DocumentReader](readabledocument/reader.md)
  A type that implements reading from disk logic.
- [func apply(snapshot: sending Self.Reader.Snapshot, previous: sending Self.Reader.Snapshot?) async throws](readabledocument/apply(snapshot:previous:).md)
  Applies loaded content to the document model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/readabledocument/reader(configuration:))*