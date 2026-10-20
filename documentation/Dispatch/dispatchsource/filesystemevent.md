# DispatchSource.FileSystemEvent

**Framework**: Dispatch  
**Kind**: struct  
**Role**: Structure

Events involving a change to a file system object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct FileSystemEvent
```

## Topics

### File System Event Flags
- [static let all: DispatchSource.FileSystemEvent](./filesystemevent/all.md)
  All changes related to the file system object.
- [static let attrib: DispatchSource.FileSystemEvent](./filesystemevent/attrib.md)
  Changes to the metadata of the file system object.
- [static let delete: DispatchSource.FileSystemEvent](./filesystemevent/delete.md)
  The deletion of the file system object.
- [static let extend: DispatchSource.FileSystemEvent](./filesystemevent/extend.md)
  Changes to the size of the file system object.
- [static let funlock: DispatchSource.FileSystemEvent](./filesystemevent/funlock.md)
  The unlocking of the file system object.
- [static let link: DispatchSource.FileSystemEvent](./filesystemevent/link.md)
  Changes to the link count of the file system object.
- [static let rename: DispatchSource.FileSystemEvent](./filesystemevent/rename.md)
  Changes to the name of the file system object.
- [static let revoke: DispatchSource.FileSystemEvent](./filesystemevent/revoke.md)
  The revocation of the file system object.
- [static let write: DispatchSource.FileSystemEvent](./filesystemevent/write.md)
  The writing of data to the file system object.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Creating a File System Source
- [class func makeReadSource(fileDescriptor: Int32, queue: DispatchQueue?) -> any DispatchSourceRead](./makereadsource%28filedescriptor,queue%29.md)
  Creates a new dispatch source object for reading bytes from the specified file.
- [class func makeWriteSource(fileDescriptor: Int32, queue: DispatchQueue?) -> any DispatchSourceWrite](./makewritesource%28filedescriptor,queue%29.md)
  Creates a new dispatch source object for writing data to the specified file.
- [class func makeFileSystemObjectSource(fileDescriptor: Int32, eventMask: DispatchSource.FileSystemEvent, queue: DispatchQueue?) -> any DispatchSourceFileSystemObject](./makefilesystemobjectsource%28filedescriptor,eventmask,queue%29.md)
  Creates a new dispatch source object for monitoring file-system events.
- [protocol DispatchSourceRead](../dispatchsourceread.md)
  A dispatch source object for reading data from a file descriptor.
- [protocol DispatchSourceWrite](../dispatchsourcewrite.md)
  A dispatch source object for writing data to a file descriptor.
- [protocol DispatchSourceFileSystemObject](../dispatchsourcefilesystemobject.md)
  A dispatch source that monitors events associated with a file descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/filesystemevent)*