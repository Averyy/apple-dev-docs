# makeFileSystemObjectSource(fileDescriptor:eventMask:queue:)

**Framework**: Dispatch  
**Kind**: method

Creates a new dispatch source object for monitoring file-system events.

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
class func makeFileSystemObjectSource(fileDescriptor: Int32, eventMask: DispatchSource.FileSystemEvent, queue: DispatchQueue? = nil) -> any DispatchSourceFileSystemObject
```

#### Return Value

A dispatch source object that conforms to the [`DispatchSourceFileSystemObject`](dispatchsourcefilesystemobject.md) protocol.

#### Discussion

After creating the dispatch source, use the methods of the [`DispatchSourceProtocol`](dispatchsourceprotocol.md) protocol to install the event handlers you need. The returned dispatch source is in the inactive state initially. When you are ready to begin processing events, call its [`activate()`](dispatchobject/activate().md) method.

## Parameters

- `fileDescriptor`: A file descriptor pointing to an open file or socket.
- `eventMask`: The set of events you want to monitor. For a list of possible values, see  .
- `queue`: The dispatch queue to use when executing the installed handlers.

## See Also

- [class func makeReadSource(fileDescriptor: Int32, queue: DispatchQueue?) -> any DispatchSourceRead](dispatchsource/makereadsource(filedescriptor:queue:).md)
  Creates a new dispatch source object for reading bytes from the specified file.
- [class func makeWriteSource(fileDescriptor: Int32, queue: DispatchQueue?) -> any DispatchSourceWrite](dispatchsource/makewritesource(filedescriptor:queue:).md)
  Creates a new dispatch source object for writing data to the specified file.
- [protocol DispatchSourceRead](dispatchsourceread.md)
  A dispatch source object for reading data from a file descriptor.
- [protocol DispatchSourceWrite](dispatchsourcewrite.md)
  A dispatch source object for writing data to a file descriptor.
- [protocol DispatchSourceFileSystemObject](dispatchsourcefilesystemobject.md)
  A dispatch source that monitors events associated with a file descriptor.
- [DispatchSource.FileSystemEvent](dispatchsource/filesystemevent.md)
  Events involving a change to a file system object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/makefilesystemobjectsource(filedescriptor:eventmask:queue:))*