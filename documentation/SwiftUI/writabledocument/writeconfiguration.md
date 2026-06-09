# WritableDocument.WriteConfiguration

**Framework**: SwiftUI  
**Kind**: typealias

The configuration for writing document contents.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
typealias WriteConfiguration = DocumentWriteConfiguration
```

## See Also

- [static var writableContentTypes: [UTType]](writabledocument/writablecontenttypes.md)
  The file types that the document supports saving or exporting to.
- [associatedtype Writer : DocumentWriter](writabledocument/writer.md)
  A type that implements writing to disk logic.
- [func writer(configuration: sending Self.WriteConfiguration) -> sending Self.Writer](writabledocument/writer(configuration:).md)
  Creates a value that writes a document to disk.
- [func snapshot(contentType: UTType) async throws -> sending Self.Writer.Snapshot](writabledocument/snapshot(contenttype:).md)
  Creates a snapshot of the document’s current state to be saved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/writabledocument/writeconfiguration)*