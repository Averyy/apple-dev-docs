# DocumentWriteConfiguration

**Framework**: SwiftUI  
**Kind**: struct

The context SwiftUI passes to [`writer(configuration:)`](writabledocument/writer(configuration:).md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct DocumentWriteConfiguration
```

#### Overview

Contains the [`contentType`](documentwriteconfiguration/contenttype.md) of the file being written (one of the document’s [`writableContentTypes`](writabledocument/writablecontenttypes.md)). Use it to choose the correct serialization strategy when a document supports exporting to multiple formats.

Access this type through the [`WritableDocument.WriteConfiguration`](writabledocument/writeconfiguration.md) typealias.

## Topics

### Accessing write properties
- [var contentType: UTType](documentwriteconfiguration/contenttype.md)
  The content type of the file being written.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Escapable](../Swift/Escapable.md)

## See Also

- [struct DocumentReadConfiguration](documentreadconfiguration.md)
  The context SwiftUI passes to [`reader(configuration:)`](readabledocument/reader(configuration:).md).
- [protocol DocumentReader](documentreader.md)
  A type that reads a document’s content from a file.
- [protocol DocumentWriter](documentwriter.md)
  A type that writes a document’s content to a file.
- [struct FileWrapperDocumentReader](filewrapperdocumentreader.md)
  A document reader that deserializes a `FileWrapper` into a snapshot.
- [struct FileWrapperDocumentWriter](filewrapperdocumentwriter.md)
  A document writer that serializes a snapshot into a `FileWrapper`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentwriteconfiguration)*