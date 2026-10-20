# FileDocument.WriteConfiguration

**Framework**: SwiftUI  
**Kind**: typealias  
**Role**: Type Alias

The configuration for writing document contents.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Conform your type to Document instead.

## Declaration

```swift
typealias WriteConfiguration = FileDocumentWriteConfiguration
```

#### Discussion

This type is an alias for [`FileDocumentWriteConfiguration`](../filedocumentwriteconfiguration.md), which contains a content type and a file wrapper that you use to access the contents of a document file, if one already exists. You get a value of this type as an input to the [`fileWrapper(configuration:)`](./filewrapper%28configuration%29.md) method.

## See Also

### Writing a document
- [func fileWrapper(configuration: Self.WriteConfiguration) throws -> FileWrapper](./filewrapper%28configuration%29.md)
  Serializes a document snapshot to a file wrapper.
- [static var writableContentTypes: [UTType]](./writablecontenttypes.md)
  The file types that the document supports saving or exporting to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filedocument/writeconfiguration)*