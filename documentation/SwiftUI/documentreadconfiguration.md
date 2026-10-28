# DocumentReadConfiguration

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The context SwiftUI passes to [`reader(configuration:)`](./readabledocument/reader%28configuration%29.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct DocumentReadConfiguration
```

## Overview

Contains the [`contentType`](./documentreadconfiguration/contenttype.md) of the file being read (one of the document’s [`readableContentTypes`](./readabledocument/readablecontenttypes.md)). Use it to choose the correct deserialization strategy when a document supports multiple formats.

Access this type through the [`ReadableDocument.ReadConfiguration`](./readabledocument/readconfiguration.md) typealias.

## Topics

### Accessing read properties
- [var contentType: UTType](./documentreadconfiguration/contenttype.md)
  The content type of the file being read.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Reading and writing documents
- [struct DocumentWriteConfiguration](./documentwriteconfiguration.md)
  The context SwiftUI passes to [`writer(configuration:)`](./writabledocument/writer%28configuration%29.md).
- [protocol DocumentReader](./documentreader.md)
  A type that reads a document’s content from a file.
- [protocol DocumentWriter](./documentwriter.md)
  A type that writes a document’s content to a file.
- [struct FileWrapperDocumentReader](./filewrapperdocumentreader.md)
  A document reader that deserializes a `FileWrapper` into a snapshot.
- [struct FileWrapperDocumentWriter](./filewrapperdocumentwriter.md)
  A document writer that serializes a snapshot into a `FileWrapper`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentreadconfiguration)*