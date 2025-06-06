# FileDocument.WriteConfiguration

**Framework**: SwiftUI  
**Kind**: typealias

The configuration for writing document contents.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
typealias WriteConfiguration = FileDocumentWriteConfiguration
```

#### Discussion

This type is an alias for [`FileDocumentWriteConfiguration`](filedocumentwriteconfiguration.md), which contains a content type and a file wrapper that you use to access the contents of a document file, if one already exists. You get a value of this type as an input to the [`fileWrapper(configuration:)`](filedocument/filewrapper(configuration:).md) method.

## See Also

- [func fileWrapper(configuration: Self.WriteConfiguration) throws -> FileWrapper](filedocument/filewrapper(configuration:).md)
  Serializes a document snapshot to a file wrapper.
- [static var writableContentTypes: [UTType]](filedocument/writablecontenttypes.md)
  The file types that the document supports saving or exporting to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filedocument/writeconfiguration)*