# DispatchSourceRead

**Framework**: Dispatch  
**Kind**: protocol

A dispatch source object for reading data from a file descriptor.

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
protocol DispatchSourceRead : DispatchSourceProtocol, Sendable
```

#### Overview

You do not adopt this protocol in your objects. Instead, use the [`makeReadSource(fileDescriptor:queue:)`](dispatchsource/makereadsource(filedescriptor:queue:).md) method to create an object that adopts this protocol.

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
- [protocol DispatchSourceWrite](dispatchsourcewrite.md)
  A dispatch source object for writing data to a file descriptor.
- [protocol DispatchSourceFileSystemObject](dispatchsourcefilesystemobject.md)
  A dispatch source that monitors events associated with a file descriptor.
- [DispatchSource.FileSystemEvent](dispatchsource/filesystemevent.md)
  Events involving a change to a file system object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourceread)*