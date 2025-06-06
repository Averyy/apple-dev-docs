# makeWriteSource(fileDescriptor:queue:)

**Framework**: Dispatch  
**Kind**: method

Creates a new dispatch source object for writing data to the specified file.

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
class func makeWriteSource(fileDescriptor: Int32, queue: DispatchQueue? = nil) -> any DispatchSourceWrite
```

#### Return Value

A dispatch source object that conforms to the [`DispatchSourceWrite`](dispatchsourcewrite.md) protocol.

#### Discussion

After creating the dispatch source, use the methods of the [`DispatchSourceProtocol`](dispatchsourceprotocol.md) protocol to install the event handlers you need. The returned dispatch source is in the inactive state initially. When you are ready to begin processing events, call its [`activate()`](dispatchobject/activate().md) method.

## Parameters

- `fileDescriptor`: A file descriptor pointing to an open file or socket. The dispatch source begins writing at the file descriptor’s current location.
- `queue`: The dispatch queue to use when executing the installed handlers.

## See Also

- [class func makeReadSource(fileDescriptor: Int32, queue: DispatchQueue?) -> any DispatchSourceRead](dispatchsource/makereadsource(filedescriptor:queue:).md)
  Creates a new dispatch source object for reading bytes from the specified file.
- [class func makeFileSystemObjectSource(fileDescriptor: Int32, eventMask: DispatchSource.FileSystemEvent, queue: DispatchQueue?) -> any DispatchSourceFileSystemObject](dispatchsource/makefilesystemobjectsource(filedescriptor:eventmask:queue:).md)
  Creates a new dispatch source object for monitoring file-system events.
- [protocol DispatchSourceRead](dispatchsourceread.md)
  A dispatch source object for reading data from a file descriptor.
- [protocol DispatchSourceWrite](dispatchsourcewrite.md)
  A dispatch source object for writing data to a file descriptor.
- [protocol DispatchSourceFileSystemObject](dispatchsourcefilesystemobject.md)
  A dispatch source that monitors events associated with a file descriptor.
- [DispatchSource.FileSystemEvent](dispatchsource/filesystemevent.md)
  Events involving a change to a file system object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/makewritesource(filedescriptor:queue:))*