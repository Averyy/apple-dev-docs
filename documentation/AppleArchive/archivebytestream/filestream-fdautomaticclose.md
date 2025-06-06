# fileStream(fd:automaticClose:)

**Framework**: Apple Archive  
**Kind**: method

Creates a stream from an open file descriptor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
static func fileStream(fd: FileDescriptor, automaticClose: Bool = true) -> ArchiveByteStream?
```

#### Return Value

A new archive byte stream.

## Parameters

- `fd`: The file descriptor that you have previously opened with  .
- `automaticClose`: A Boolean value that specifies whether to close the file descriptor when you close the stream.

## See Also

- [static func withFileStream<E>(fd: FileDescriptor, automaticClose: Bool, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withfilestream(fd:automaticclose:_:).md)
  Calls the given closure with a file stream created from the specified file descriptor.
- [static func fileStream(path: FilePath, mode: FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions) -> ArchiveByteStream?](archivebytestream/filestream(path:mode:options:permissions:).md)
  Opens a new file descriptor using the given path and parameters, and creates a stream from the file descriptor.
- [static func withFileStream<E>(path: FilePath, mode: FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withfilestream(path:mode:options:permissions:_:).md)
  Calls the given closure with a file stream.
- [static func temporaryFileStream() -> ArchiveByteStream?](archivebytestream/temporaryfilestream.md)
  Creates a new temporary file stream.
- [static func withTemporaryFileStream<E>((ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withtemporaryfilestream(_:).md)
  Calls the given closure with a temporary file stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/filestream(fd:automaticclose:))*