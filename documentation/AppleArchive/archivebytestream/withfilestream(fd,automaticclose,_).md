# withFileStream(fd:automaticClose:_:)

**Framework**: Apple Archive  
**Kind**: method  
**Role**: Type Method

Calls the given closure with a file stream created from the specified file descriptor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
static func withFileStream<E>(fd: FileDescriptor, automaticClose: Bool = true, _ body: (ArchiveByteStream) throws -> E) throws -> E
```

## Return Value

The result of the closure.

## Parameters

- `fd`: The file descriptor that you have previously opened with `open(2)`.
- `automaticClose`: A Boolean value that specifies whether to close the file descriptor when you close the stream.
- `body`: A closure with the archive byte stream passed as a parameter.

## See Also

### File Streaming
- [static func fileStream(fd: FileDescriptor, automaticClose: Bool) -> ArchiveByteStream?](./filestream%28fd,automaticclose%29.md)
  Creates a stream from an open file descriptor.
- [static func fileStream(path: FilePath, mode: FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions) -> ArchiveByteStream?](./filestream%28path,mode,options,permissions%29.md)
  Opens a new file descriptor using the given path and parameters, and creates a stream from the file descriptor.
- [static func withFileStream<E>(path: FilePath, mode: FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions, (ArchiveByteStream) throws -> E) throws -> E](./withfilestream%28path,mode,options,permissions,_%29.md)
  Calls the given closure with a file stream.
- [static func temporaryFileStream() -> ArchiveByteStream?](./temporaryfilestream%28%29.md)
  Creates a new temporary file stream.
- [static func withTemporaryFileStream<E>((ArchiveByteStream) throws -> E) throws -> E](./withtemporaryfilestream%28_%29.md)
  Calls the given closure with a temporary file stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/withfilestream(fd:automaticclose:_:))*