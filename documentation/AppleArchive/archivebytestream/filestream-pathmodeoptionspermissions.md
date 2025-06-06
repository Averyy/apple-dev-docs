# fileStream(path:mode:options:permissions:)

**Framework**: Apple Archive  
**Kind**: method

Opens a new file descriptor using the given path and parameters, and creates a stream from the file descriptor.

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
static func fileStream(path: FilePath, mode: FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions) -> ArchiveByteStream?
```

#### Return Value

A new archive byte stream.

## Parameters

- `path`: The file path.
- `mode`: The file descriptor access mode.
- `options`: The file descriptor options that specify behavior on opening a file.
- `permissions`: The file permission bits that govern access to a file.

## See Also

- [static func fileStream(fd: FileDescriptor, automaticClose: Bool) -> ArchiveByteStream?](archivebytestream/filestream(fd:automaticclose:).md)
  Creates a stream from an open file descriptor.
- [static func withFileStream<E>(fd: FileDescriptor, automaticClose: Bool, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withfilestream(fd:automaticclose:_:).md)
  Calls the given closure with a file stream created from the specified file descriptor.
- [static func withFileStream<E>(path: FilePath, mode: FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withfilestream(path:mode:options:permissions:_:).md)
  Calls the given closure with a file stream.
- [static func temporaryFileStream() -> ArchiveByteStream?](archivebytestream/temporaryfilestream.md)
  Creates a new temporary file stream.
- [static func withTemporaryFileStream<E>((ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withtemporaryfilestream(_:).md)
  Calls the given closure with a temporary file stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/filestream(path:mode:options:permissions:))*