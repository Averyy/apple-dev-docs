# snapshot(contentType:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Captures the document’s current state for saving.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
func snapshot(contentType: UTType) async throws -> sending Self.Writer.Snapshot
```

#### Discussion

SwiftUI calls this on the main actor when a save is needed. Keep this method lightweight — return a value that represents what to save, and perform actual serialization in [`write(snapshot:to:previous:progress:)`](../documentwriter/write%28snapshot,to,previous,progress%29.md).

## Parameters

- `contentType`: The format requested (one of [`writableContentTypes`](./writablecontenttypes.md)).

## See Also

### Writing a document
- [static var writableContentTypes: [UTType]](./writablecontenttypes.md)
  The content types this document can save or export to.
- [WritableDocument.WriteConfiguration](./writeconfiguration.md)
  The configuration for writing document contents.
- [associatedtype Writer : DocumentWriter](./writer.md)
  A type that implements writing to disk.
- [func writer(configuration: sending Self.WriteConfiguration) -> sending Self.Writer](./writer%28configuration%29.md)
  Creates a writer to save this document to disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/writabledocument/snapshot(contenttype:))*