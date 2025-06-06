# fileWrapper(configuration:)

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
func fileWrapper(configuration: Self.WriteConfiguration) throws -> FileWrapper
```

#### Return Value

The destination to serialize the document contents to. The value can be a newly created [`FileWrapper`](https://developer.apple.com/documentation/Foundation/FileWrapper) or an update of the one provided in the `configuration` input.

#### Discussion

To store a document — for example, in response to a Save command — SwiftUI calls this method. Use it to serialize the document’s data and create or modify a file wrapper with the serialized data:

```swift
func fileWrapper(configuration: WriteConfiguration) throws -> FileWrapper {
    let data = try JSONEncoder().encode(model)
    return FileWrapper(regularFileWithContents: data)
}
```

> **Note**: SwiftUI calls this method on a background thread. Don’t make user interface changes from that thread.

## Parameters

- `configuration`: Information about a file that already exists for the   document, if any.

## See Also

- [static var writableContentTypes: [UTType]](filedocument/writablecontenttypes.md)
  The file types that the document supports saving or exporting to.
- [FileDocument.WriteConfiguration](filedocument/writeconfiguration.md)
  The configuration for writing document contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filedocument/filewrapper(configuration:))*