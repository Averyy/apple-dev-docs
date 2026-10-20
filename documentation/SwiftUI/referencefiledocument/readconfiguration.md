# ReferenceFileDocument.ReadConfiguration

**Framework**: SwiftUI  
**Kind**: typealias  
**Role**: Type Alias

The configuration for reading document contents.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+

> **Deprecated**: Use Document protocol instead.

## Declaration

```swift
typealias ReadConfiguration = FileDocumentReadConfiguration
```

#### Discussion

This type is an alias for [`FileDocumentReadConfiguration`](../filedocumentreadconfiguration.md), which contains a content type and a file wrapper that you use to access the contents of a document file. You get a value of this type as an input to the [`init(configuration:)`](./init%28configuration%29.md) initializer. Use it to load a document from a file.

## See Also

### Reading a document
- [init(configuration: Self.ReadConfiguration) throws](./init%28configuration%29.md)
  Creates a document and initializes it with the contents of a file.
- [static var readableContentTypes: [UTType]](./readablecontenttypes.md)
  The file and data types that the document reads from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/referencefiledocument/readconfiguration)*