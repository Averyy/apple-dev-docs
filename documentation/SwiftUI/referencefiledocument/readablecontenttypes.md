# readableContentTypes

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

The file and data types that the document reads from.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static var readableContentTypes: [UTType] { get }
```

#### Discussion

Define this list to indicate the content types that your document can read. By default, SwiftUI assumes that your document can also write the same set of content types. If you need to indicate a different set of types for writing files, define the [`writableContentTypes`](referencefiledocument/writablecontenttypes.md) property in addition to this property.

## See Also

- [init(configuration: Self.ReadConfiguration) throws](referencefiledocument/init(configuration:).md)
  Creates a document and initializes it with the contents of a file.
- [ReferenceFileDocument.ReadConfiguration](referencefiledocument/readconfiguration.md)
  The configuration for reading document contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/referencefiledocument/readablecontenttypes)*