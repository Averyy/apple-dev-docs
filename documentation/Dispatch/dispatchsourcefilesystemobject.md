# DispatchSourceFileSystemObject

**Framework**: Dispatch  
**Kind**: protocol

A dispatch source that monitors events associated with a file descriptor.

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
protocol DispatchSourceFileSystemObject : DispatchSourceProtocol, Sendable
```

#### Overview

You do not adopt this protocol in your objects. Instead, use the [`makeFileSystemObjectSource(fileDescriptor:eventMask:queue:)`](dispatchsource/makefilesystemobjectsource(filedescriptor:eventmask:queue:).md) method to create an object that adopts this protocol.

## Topics

### Getting the Data Handle
- [var handle: Int32](dispatchsourcefilesystemobject/handle.md)
  The file descriptor of the file or socket.
### Getting the Event Data
- [var data: DispatchSource.FileSystemEvent](dispatchsourcefilesystemobject/data.md)
  The type of the last file system event.
- [var mask: DispatchSource.FileSystemEvent](dispatchsourcefilesystemobject/mask.md)
  The file descriptor attributes being monitored by the dispatch source.

## Relationships

### Inherits From
- [DispatchSourceProtocol](dispatchsourceprotocol.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [DispatchSource](dispatchsource.md)

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
- [DispatchSource.FileSystemEvent](dispatchsource/filesystemevent.md)
  Events involving a change to a file system object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourcefilesystemobject)*