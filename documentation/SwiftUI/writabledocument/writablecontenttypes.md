# writableContentTypes

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

The file types that the document supports saving or exporting to.

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

- [WritableDocument.WriteConfiguration](writabledocument/writeconfiguration.md)
  The configuration for writing document contents.
- [associatedtype Writer : DocumentWriter](writabledocument/writer.md)
  A type that implements writing to disk logic.
- [func writer(configuration: sending Self.WriteConfiguration) -> sending Self.Writer](writabledocument/writer(configuration:).md)
  Creates a value that writes a document to disk.
- [func snapshot(contentType: UTType) async throws -> sending Self.Writer.Snapshot](writabledocument/snapshot(contenttype:).md)
  Creates a snapshot of the document’s current state to be saved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/writabledocument/writablecontenttypes)*