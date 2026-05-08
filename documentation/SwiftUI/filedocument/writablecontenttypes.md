# writableContentTypes

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

The file types that the document supports saving or exporting to.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static var writableContentTypes: [UTType] { get }
```

#### Discussion

By default, SwiftUI assumes that your document reads and writes the same set of content types. Only define this property if you need to indicate a different set of types for writing files. Otherwise, the default implementation of this property returns the list that you specify in your implementation of [`readableContentTypes`](filedocument/readablecontenttypes.md).

## See Also

- [func fileWrapper(configuration: Self.WriteConfiguration) throws -> FileWrapper](filedocument/filewrapper(configuration:).md)
  Serializes a document snapshot to a file wrapper.
- [FileDocument.WriteConfiguration](filedocument/writeconfiguration.md)
  The configuration for writing document contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filedocument/writablecontenttypes)*