# DispatchSource.FileSystemEvent

**Framework**: Dispatch  
**Kind**: struct

Events involving a change to a file system object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct FileSystemEvent
```

## Topics

### File System Event Flags
- [static let all: DispatchSource.FileSystemEvent](dispatchsource/filesystemevent/all.md)
  All changes related to the file system object.
- [static let attrib: DispatchSource.FileSystemEvent](dispatchsource/filesystemevent/attrib.md)
  Changes to the metadata of the file system object.
- [static let delete: DispatchSource.FileSystemEvent](dispatchsource/filesystemevent/delete.md)
  The deletion of the file system object.
- [static let extend: DispatchSource.FileSystemEvent](dispatchsource/filesystemevent/extend.md)
  Changes to the size of the file system object.
- [static let funlock: DispatchSource.FileSystemEvent](dispatchsource/filesystemevent/funlock.md)
  The unlocking of the file system object.
- [static let link: DispatchSource.FileSystemEvent](dispatchsource/filesystemevent/link.md)
  Changes to the link count of the file system object.
- [static let rename: DispatchSource.FileSystemEvent](dispatchsource/filesystemevent/rename.md)
  Changes to the name of the file system object.
- [static let revoke: DispatchSource.FileSystemEvent](dispatchsource/filesystemevent/revoke.md)
  The revocation of the file system object.
- [static let write: DispatchSource.FileSystemEvent](dispatchsource/filesystemevent/write.md)
  The writing of data to the file system object.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class func makeReadSource(fileDescriptor: Int32, queue: DispatchQueue?) -> any DispatchSourceRead](dispatchsource/makereadsource(filedescriptor:queue:).md)
  Creates a new dispatch source object for reading bytes from the specified file.
- [class func makeWriteSource(fileDescriptor: Int32, queue: DispatchQueue?) -> any DispatchSourceWrite](dispatchsource/makewritesource(filedescriptor:queue:).md)
  Creates a new dispatch source object for writing data to the specified file.
- [class func makeFileSystemObjectSource(fileDescriptor: Int32, eventMask: DispatchSource.FileSystemEvent, queue: DispatchQueue?) -> any DispatchSourceFileSystemObject](dispatchsource/makefilesystemobjectsource(filedescriptor:eventmask:queue:).md)
  Creates a new dispatch source object for monitoring file-system events.
- [protocol DispatchSourceRead](dispatchsourceread.md)
  A dispatch source object for reading data from a file descriptor.
- [protocol DispatchSourceWrite](dispatchsourcewrite.md)
  A dispatch source object for writing data to a file descriptor.
- [protocol DispatchSourceFileSystemObject](dispatchsourcefilesystemobject.md)
  A dispatch source that monitors events associated with a file descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/filesystemevent)*