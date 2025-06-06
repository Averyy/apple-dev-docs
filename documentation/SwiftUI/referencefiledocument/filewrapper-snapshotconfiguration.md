# fileWrapper(snapshot:configuration:)

**Framework**: Swiftui  
**Kind**: method  
**Required**: Yes

Serializes a document snapshot to a file wrapper.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func fileWrapper(snapshot: Self.Snapshot, configuration: Self.WriteConfiguration) throws -> FileWrapper
```

#### Return Value

The destination to serialize the document contents to. The value can be a newly created [`FileWrapper`](https://developer.apple.com/documentation/Foundation/FileWrapper) or an update of the one provided in the `configuration` input.

#### Discussion

To store a document — for example, in response to a Save command — SwiftUI begins by calling the [`snapshot(contentType:)`](referencefiledocument/snapshot(contenttype:).md) method to get a copy of the document data in its current state. Then SwiftUI passes that snapshot to this method, where you serialize it and create or modify a file wrapper with the serialized data:

```swift
func fileWrapper(snapshot: Snapshot, configuration: WriteConfiguration) throws -> FileWrapper {
    let data = try JSONEncoder().encode(snapshot)
    return FileWrapper(regularFileWithContents: data)
}
```

SwiftUI disables document edits during the snapshot to ensure that the document’s data remains coherent, but reenables edits during the serialization operation.

> **Note**: SwiftUI calls this method on a background thread. Don’t make user interface changes from that thread.

## Parameters

- `snapshot`: The document snapshot to save.
- `configuration`: Information about a file that already exists for the   document, if any.

## See Also

- [static var writableContentTypes: [UTType]](referencefiledocument/writablecontenttypes.md)
  The file types that the document supports saving or exporting to.
- [ReferenceFileDocument.WriteConfiguration](referencefiledocument/writeconfiguration.md)
  The configuration for writing document contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/referencefiledocument/filewrapper(snapshot:configuration:))*