# FileDocument

**Framework**: SwiftUI  
**Kind**: protocol

A type that you use to serialize documents to and from file.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@preconcurrency
protocol FileDocument : Sendable
```

#### Overview

To store a document as a value type — like a structure — create a type that conforms to the `FileDocument` protocol and implement the required methods and properties. Your implementation:

- Provides a list of the content types that the document can read from and write to by defining [`readableContentTypes`](filedocument/readablecontenttypes.md). If the list of content types that the document can write to is different from those that it reads from, you can optionally also define [`writableContentTypes`](filedocument/writablecontenttypes.md).
- Loads documents from file in the [`init(configuration:)`](filedocument/init(configuration:).md) initializer.
- Stores documents to file by serializing their content in the [`fileWrapper(configuration:)`](filedocument/filewrapper(configuration:).md) method.

> ❗ **Important**: If you store your document as a reference type — like a class — use [`ReferenceFileDocument`](referencefiledocument.md) instead.

If you store your document as a reference type — like a class — use [`ReferenceFileDocument`](referencefiledocument.md) instead.

Ensure that types that conform to this protocol are `Sendable`. In particular, SwiftUI calls the protocol’s methods from different isolation domains. Don’t perform serialization and deserialization on `MainActor`.

## Topics

### Reading a document
- [init(configuration: Self.ReadConfiguration) throws](filedocument/init(configuration:).md)
  Creates a document and initializes it with the contents of a file.
- [static var readableContentTypes: [UTType]](filedocument/readablecontenttypes.md)
  The file and data types that the document reads from.
- [FileDocument.ReadConfiguration](filedocument/readconfiguration.md)
  The configuration for reading document contents.
### Writing a document
- [func fileWrapper(configuration: Self.WriteConfiguration) throws -> FileWrapper](filedocument/filewrapper(configuration:).md)
  Serializes a document snapshot to a file wrapper.
- [static var writableContentTypes: [UTType]](filedocument/writablecontenttypes.md)
  The file types that the document supports saving or exporting to.
- [FileDocument.WriteConfiguration](filedocument/writeconfiguration.md)
  The configuration for writing document contents.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct FileDocumentConfiguration](filedocumentconfiguration.md)
  The properties of an open file document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filedocument)*