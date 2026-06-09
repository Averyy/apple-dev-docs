# writer(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates a value that writes a document to disk.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func writer(configuration: sending Self.WriteConfiguration) -> sending Self.Writer
```

## Parameters

- `configuration`: Additional context for writing.

## See Also

- [static var writableContentTypes: [UTType]](writabledocument/writablecontenttypes.md)
  The file types that the document supports saving or exporting to.
- [WritableDocument.WriteConfiguration](writabledocument/writeconfiguration.md)
  The configuration for writing document contents.
- [associatedtype Writer : DocumentWriter](writabledocument/writer.md)
  A type that implements writing to disk logic.
- [func snapshot(contentType: UTType) async throws -> sending Self.Writer.Snapshot](writabledocument/snapshot(contenttype:).md)
  Creates a snapshot of the document’s current state to be saved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/writabledocument/writer(configuration:))*