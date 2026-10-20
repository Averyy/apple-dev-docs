# DispatchIO.StreamType

**Framework**: Dispatch  
**Kind**: enum  
**Role**: Enumeration

The semantics for accessing the contents of a file descriptor.

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
enum StreamType
```

## Topics

### Stream Types
- [DispatchIO.StreamType.stream](./streamtype/stream.md)
  Access content sequentially, in a stream.
- [DispatchIO.StreamType.random](./streamtype/random.md)
  Access content randomly.
### Initializing the Type
- [var DISPATCH_IO_RANDOM: Int32](../dispatch_io_random.md)
- [var DISPATCH_IO_STREAM: Int32](../dispatch_io_stream.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a Dispatch I/O Object
- [convenience init(type: DispatchIO.StreamType, fileDescriptor: Int32, queue: DispatchQueue, cleanupHandler: (Int32) -> Void)](./init%28type,filedescriptor,queue,cleanuphandler%29.md)
  Creates a new I/O channel that accesses the specified file descriptor.
- [convenience init?(type: DispatchIO.StreamType, path: UnsafePointer<Int8>, oflag: Int32, mode: mode_t, queue: DispatchQueue, cleanupHandler: (Int32) -> Void)](./init%28type,path,oflag,mode,queue,cleanuphandler%29-50rb0.md)
  Creates a new I/O channel that accesses the file at the specified path, potentially creating that file in the process.
- [convenience init(type: DispatchIO.StreamType, io: DispatchIO, queue: DispatchQueue, cleanupHandler: (Int32) -> Void)](./init%28type,io,queue,cleanuphandler%29.md)
  Creates a new I/O channel from an existing I/O channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchio/streamtype)*