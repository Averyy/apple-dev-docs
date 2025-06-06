# init(type:io:queue:cleanupHandler:)

**Framework**: Dispatch  
**Kind**: init

Creates a new I/O channel from an existing I/O channel.

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
convenience init(type: DispatchIO.StreamType, io: DispatchIO, queue: DispatchQueue, cleanupHandler: @escaping (Int32) -> Void)
```

## Parameters

- `type`: The access semantics for the channel. For a list of possible values, see  .
- `io`: An existing channel.
- `queue`: The dispatch queue on which to perform work.
- `cleanupHandler`: The handler to execute once the channel is closed. This block has no return value and takes the following parameter:

## See Also

- [convenience init(type: DispatchIO.StreamType, fileDescriptor: Int32, queue: DispatchQueue, cleanupHandler: (Int32) -> Void)](dispatchio/init(type:filedescriptor:queue:cleanuphandler:).md)
  Creates a new I/O channel that accesses the specified file descriptor.
- [convenience init?(type: DispatchIO.StreamType, path: UnsafePointer<Int8>, oflag: Int32, mode: mode_t, queue: DispatchQueue, cleanupHandler: (Int32) -> Void)](dispatchio/init(type:path:oflag:mode:queue:cleanuphandler:)-50rb0.md)
  Creates a new I/O channel that accesses the file at the specified path, potentially creating that file in the process.
- [DispatchIO.StreamType](dispatchio/streamtype.md)
  The semantics for accessing the contents of a file descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchio/init(type:io:queue:cleanuphandler:))*