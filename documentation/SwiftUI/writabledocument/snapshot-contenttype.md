# snapshot(contentType:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Captures the document’s current state for saving.

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

SwiftUI calls this on the main actor when a save is needed. Keep this method lightweight — return a value that represents what to save, and perform actual serialization in [`write(snapshot:to:previous:progress:)`](documentwriter/write(snapshot:to:previous:progress:).md).

## Parameters

- `contentType`: The format requested (one of [`writableContentTypes`](writabledocument/writablecontenttypes.md)).

## See Also

- [static var writableContentTypes: [UTType]](writabledocument/writablecontenttypes.md)
  The content types this document can save or export to.
- [WritableDocument.WriteConfiguration](writabledocument/writeconfiguration.md)
  The configuration for writing document contents.
- [associatedtype Writer : DocumentWriter](writabledocument/writer.md)
  A type that implements writing to disk.
- [func writer(configuration: sending Self.WriteConfiguration) -> sending Self.Writer](writabledocument/writer(configuration:).md)
  Creates a writer to save this document to disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/writabledocument/snapshot(contenttype:))*