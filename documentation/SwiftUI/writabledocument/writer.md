# Writer

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Required**: Yes

A type that implements writing to disk.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
associatedtype Writer : DocumentWriter
```

## See Also

- [static var writableContentTypes: [UTType]](writabledocument/writablecontenttypes.md)
  The content types this document can save or export to.
- [WritableDocument.WriteConfiguration](writabledocument/writeconfiguration.md)
  The configuration for writing document contents.
- [func writer(configuration: sending Self.WriteConfiguration) -> sending Self.Writer](writabledocument/writer(configuration:).md)
  Creates a writer to save this document to disk.
- [func snapshot(contentType: UTType) async throws -> sending Self.Writer.Snapshot](writabledocument/snapshot(contenttype:).md)
  Captures the document’s current state for saving.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/writabledocument/writer)*