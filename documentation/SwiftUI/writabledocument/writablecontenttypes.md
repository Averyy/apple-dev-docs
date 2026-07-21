# writableContentTypes

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

The content types this document can save or export to.

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

#### Discussion

The save panel uses this list to offer format options. When a document also conforms to [`ReadableDocument`](readabledocument.md), the default implementation returns [`readableContentTypes`](readabledocument/readablecontenttypes.md).

## See Also

- [WritableDocument.WriteConfiguration](writabledocument/writeconfiguration.md)
  The configuration for writing document contents.
- [associatedtype Writer : DocumentWriter](writabledocument/writer.md)
  A type that implements writing to disk.
- [func writer(configuration: sending Self.WriteConfiguration) -> sending Self.Writer](writabledocument/writer(configuration:).md)
  Creates a writer to save this document to disk.
- [func snapshot(contentType: UTType) async throws -> sending Self.Writer.Snapshot](writabledocument/snapshot(contenttype:).md)
  Captures the document’s current state for saving.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/writabledocument/writablecontenttypes)*