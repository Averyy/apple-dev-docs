# DocumentReadConfiguration

**Framework**: SwiftUI  
**Kind**: struct

The context SwiftUI passes to [`reader(configuration:)`](readabledocument/reader(configuration:).md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct DocumentReadConfiguration
```

#### Overview

Contains the [`contentType`](documentreadconfiguration/contenttype.md) of the file being read (one of the document’s [`readableContentTypes`](readabledocument/readablecontenttypes.md)). Use it to choose the correct deserialization strategy when a document supports multiple formats.

Access this type through the [`ReadableDocument.ReadConfiguration`](readabledocument/readconfiguration.md) typealias.

## Topics

### Accessing read properties
- [var contentType: UTType](documentreadconfiguration/contenttype.md)
  The content type of the file being read.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct DocumentWriteConfiguration](documentwriteconfiguration.md)
  The context SwiftUI passes to [`writer(configuration:)`](writabledocument/writer(configuration:).md).
- [protocol DocumentReader](documentreader.md)
  A type that reads a document’s content from a file.
- [protocol DocumentWriter](documentwriter.md)
  A type that writes a document’s content to a file.
- [struct FileWrapperDocumentReader](filewrapperdocumentreader.md)
  A document reader that deserializes a `FileWrapper` into a snapshot.
- [struct FileWrapperDocumentWriter](filewrapperdocumentwriter.md)
  A document writer that serializes a snapshot into a `FileWrapper`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentreadconfiguration)*