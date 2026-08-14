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

> **Note**: The `fileWrapper(configuration:)` method can either serialize the whole document into a single file, or use a document package — a directory `FileWrapper` — to store the document as a collection of files. With a package, you can improve performance by rewriting only the specific files that changed since the last save. For examples, see [`fileWrapper(configuration:)`](filedocument/filewrapper(configuration:).md).

Ensure that types that conform to this protocol are `Sendable`. In particular, SwiftUI calls the protocol’s methods from different isolation domains. Don’t perform serialization and deserialization on `MainActor`.

> ❗ **Important**: If you store your document as a reference type — like a class — use [`ReferenceFileDocument`](referencefiledocument.md) instead.

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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct FileDocumentConfiguration](filedocumentconfiguration.md)
  The properties of an open file document.
- [struct FileDocumentReadConfiguration](filedocumentreadconfiguration.md)
  The configuration for reading file contents.
- [struct FileDocumentWriteConfiguration](filedocumentwriteconfiguration.md)
  The configuration for serializing file contents.
- [struct NewDocumentAction](newdocumentaction.md)
  An action that presents a new document.
- [protocol ReferenceFileDocument](referencefiledocument.md)
  A type that you use to serialize reference type documents to and from file.
- [struct ReferenceFileDocumentConfiguration](referencefiledocumentconfiguration.md)
  The properties of an open reference file document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filedocument)*