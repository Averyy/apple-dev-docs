# readableContentTypes

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property  
**Required**: Yes

The file and data types that the document reads from.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Conform your type to Document instead.

## Declaration

```swift
static var readableContentTypes: [UTType] { get }
```

#### Discussion

Define this list to indicate the content types that your document can read. By default, SwiftUI assumes that your document can also write the same set of content types. If you need to indicate a different set of types for writing files, define the [`writableContentTypes`](./writablecontenttypes.md) property in addition to this property.

## See Also

### Reading a document
- [init(configuration: Self.ReadConfiguration) throws](./init%28configuration%29.md)
  Creates a document and initializes it with the contents of a file.
- [FileDocument.ReadConfiguration](./readconfiguration.md)
  The configuration for reading document contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filedocument/readablecontenttypes)*