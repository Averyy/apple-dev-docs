# snapshot(contentType:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates a snapshot of the document’s current state to be saved.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
func snapshot(contentType: UTType) async throws -> sending Self.Writer.Snapshot
```

#### Discussion

SwiftUI calls this on the main actor when saving. Perform expensive serialization inside `DocumentWriter.write(snapshot:to:previous:progress:)` rather than here.

## Parameters

- `contentType`: The format of the data requested.

## See Also

- [static var writableContentTypes: [UTType]](writabledocument/writablecontenttypes.md)
  The file types that the document supports saving or exporting to.
- [WritableDocument.WriteConfiguration](writabledocument/writeconfiguration.md)
  The configuration for writing document contents.
- [associatedtype Writer : DocumentWriter](writabledocument/writer.md)
  A type that implements writing to disk logic.
- [func writer(configuration: sending Self.WriteConfiguration) -> sending Self.Writer](writabledocument/writer(configuration:).md)
  Creates a value that writes a document to disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/writabledocument/snapshot(contenttype:))*