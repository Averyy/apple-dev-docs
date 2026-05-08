# ReferenceFileDocument

**Framework**: SwiftUI  
**Kind**: protocol

A type that you use to serialize reference type documents to and from file.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@preconcurrency
protocol ReferenceFileDocument : ObservableObject, Sendable
```

#### Overview

To store a document as a reference type — like a class — create a type that conforms to the `ReferenceFileDocument` protocol and implement the required methods and properties. Your implementation:

- Provides a list of the content types that the document can read from and write to by defining [`readableContentTypes`](referencefiledocument/readablecontenttypes.md). If the list of content types that the document can write to is different from those that it reads from, you can optionally also define [`writableContentTypes`](referencefiledocument/writablecontenttypes.md).
- Loads documents from file in the [`init(configuration:)`](referencefiledocument/init(configuration:).md) initializer.
- Stores documents to file by providing a snapshot of the document’s content in the [`snapshot(contentType:)`](referencefiledocument/snapshot(contenttype:).md) method, and then serializing that content in the [`fileWrapper(snapshot:configuration:)`](referencefiledocument/filewrapper(snapshot:configuration:).md) method.

Ensure that types that conform to this protocol are `Sendable`. In particular, SwiftUI calls the protocol’s methods from different isolation domains. Don’t perform serialization and deserialization on `MainActor`.

```swift
final class PDFDocument: ReferenceFileDocument {
    struct Storage {
        var contents: Data
    }

    static let readableContentTypes: [UTType] = [.pdf]
    let storage: Mutex<Storage>

    required init(configuration: ReadConfiguration) throws {
       guard let data = configuration.file.regularFileContents else {
           throw CocoaError(.fileReadCorruptFile)
       }
        self.storage = .init(.init(contents: data))
    }

    func snapshot(contentType: UTType) throws -> Data {
        storage.withLock { $0.contents }
    }

    func fileWrapper(snapshot: Data, configuration: WriteConfiguration) throws -> FileWrapper {
        return FileWrapper(regularFileWithContents: snapshot)
    }
}
```

> ❗ **Important**: If you store your document as a value type — like a structure — use [`FileDocument`](filedocument.md) instead.

## Topics

### Reading a document
- [init(configuration: Self.ReadConfiguration) throws](referencefiledocument/init(configuration:).md)
  Creates a document and initializes it with the contents of a file.
- [static var readableContentTypes: [UTType]](referencefiledocument/readablecontenttypes.md)
  The file and data types that the document reads from.
- [ReferenceFileDocument.ReadConfiguration](referencefiledocument/readconfiguration.md)
  The configuration for reading document contents.
### Getting a snapshot
- [func snapshot(contentType: UTType) throws -> Self.Snapshot](referencefiledocument/snapshot(contenttype:).md)
  Creates a snapshot that represents the current state of the document.
- [associatedtype Snapshot](referencefiledocument/snapshot.md)
  A type that represents the document’s stored content.
### Writing a document
- [func fileWrapper(snapshot: Self.Snapshot, configuration: Self.WriteConfiguration) throws -> FileWrapper](referencefiledocument/filewrapper(snapshot:configuration:).md)
  Serializes a document snapshot to a file wrapper.
- [static var writableContentTypes: [UTType]](referencefiledocument/writablecontenttypes.md)
  The file types that the document supports saving or exporting to.
- [ReferenceFileDocument.WriteConfiguration](referencefiledocument/writeconfiguration.md)
  The configuration for writing document contents.

## Relationships

### Inherits From
- [ObservableObject](../Combine/ObservableObject.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ReferenceFileDocumentConfiguration](referencefiledocumentconfiguration.md)
  The properties of an open reference file document.
- [var undoManager: UndoManager?](environmentvalues/undomanager.md)
  The undo manager used to register a view’s undo operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/referencefiledocument)*