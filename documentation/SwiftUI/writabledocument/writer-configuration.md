# writer(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates a writer to save this document to disk.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func writer(configuration: sending Self.WriteConfiguration) -> sending Self.Writer
```

#### Discussion

Return a [`FileWrapperDocumentWriter`](filewrapperdocumentwriter.md) for cases that don’t require custom writing logic, or a [`DocumentWriter`](documentwriter.md) for direct URL access or streaming writes.

## Parameters

- `configuration`: The content type of the file being written.

## See Also

- [static var writableContentTypes: [UTType]](writabledocument/writablecontenttypes.md)
  The content types this document can save or export to.
- [WritableDocument.WriteConfiguration](writabledocument/writeconfiguration.md)
  The configuration for writing document contents.
- [associatedtype Writer : DocumentWriter](writabledocument/writer.md)
  A type that implements writing to disk.
- [func snapshot(contentType: UTType) async throws -> sending Self.Writer.Snapshot](writabledocument/snapshot(contenttype:).md)
  Captures the document’s current state for saving.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/writabledocument/writer(configuration:))*