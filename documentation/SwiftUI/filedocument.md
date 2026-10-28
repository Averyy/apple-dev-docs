# FileDocument

**Framework**: SwiftUI  
**Kind**: protocol  
**Role**: Protocol

A type that you use to serialize documents to and from file.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Conform your type to Document instead.

## Declaration

```swift
@preconcurrency
protocol FileDocument : Sendable
```

## Overview

To store a document as a value type — like a structure — create a type that conforms to the `FileDocument` protocol and implement the required methods and properties. Your implementation:

- Provides a list of the content types that the document can read from and write to by defining [`readableContentTypes`](./filedocument/readablecontenttypes.md). If the list of content types that the document can write to is different from those that it reads from, you can optionally also define [`writableContentTypes`](./filedocument/writablecontenttypes.md).
- Loads documents from file in the [`init(configuration:)`](./filedocument/init%28configuration%29.md) initializer.
- Stores documents to file by serializing their content in the [`fileWrapper(configuration:)`](./filedocument/filewrapper%28configuration%29.md) method.

> **Note**: The `fileWrapper(configuration:)` method can either serialize the whole document into a single file, or use a document package — a directory `FileWrapper` — to store the document as a collection of files. With a package, you can improve performance by rewriting only the specific files that changed since the last save. For examples, see [`fileWrapper(configuration:)`](./filedocument/filewrapper%28configuration%29.md).

Because `FileDocument` is a value type, SwiftUI automatically registers an undo action whenever your document’s value changes. You don’t need to call `UndoManager/registerUndo(withTarget:handler:)` yourself.

Ensure that types that conform to this protocol are `Sendable`. In particular, SwiftUI calls the protocol’s methods from different isolation domains. Don’t perform serialization and deserialization on `MainActor`.

> ❗ **Important**: If you store your document as a reference type — like a class — use [`ReferenceFileDocument`](./referencefiledocument.md) instead. Because SwiftUI can’t detect changes to a reference type’s properties on its own, you’re responsible for registering undo actions yourself.

## Topics

### Reading a document
- [init(configuration: Self.ReadConfiguration) throws](./filedocument/init%28configuration%29.md)
  Creates a document and initializes it with the contents of a file.
- [static var readableContentTypes: [UTType]](./filedocument/readablecontenttypes.md)
  The file and data types that the document reads from.
- [FileDocument.ReadConfiguration](./filedocument/readconfiguration.md)
  The configuration for reading document contents.
### Writing a document
- [func fileWrapper(configuration: Self.WriteConfiguration) throws -> FileWrapper](./filedocument/filewrapper%28configuration%29.md)
  Serializes a document snapshot to a file wrapper.
- [static var writableContentTypes: [UTType]](./filedocument/writablecontenttypes.md)
  The file types that the document supports saving or exporting to.
- [FileDocument.WriteConfiguration](./filedocument/writeconfiguration.md)
  The configuration for writing document contents.

## Relationships

### Inherits From
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deprecated protocols
- [protocol ReferenceFileDocument](./referencefiledocument.md)
  A type that you use to serialize reference type documents to and from file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filedocument)*