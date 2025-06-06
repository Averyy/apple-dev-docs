# write(toFileDescriptor:data:runningHandlerOn:handler:)

**Framework**: Dispatch  
**Kind**: method

Schedules an asynchronous write operation to the specified file descriptor.

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
class func write(toFileDescriptor: Int32, data: DispatchData, runningHandlerOn queue: DispatchQueue, handler: @escaping (DispatchData?, Int32) -> Void)
```

#### Discussion

This is a convenience method for initiating a single, asynchronous write operation at the current position of the specified file descriptor. This method is intended for simple operations where you do not need the overhead of creating a channel and do not plan on issuing more than a few calls to read or write data. Once submitted, there is no way to cancel the write operation.

After calling this method, the system takes control of the specified file descriptor until the handler block is enqueued. While it controls the file descriptor, the system may modify it on behalf of the application. For example, the system typically adds the `O_NONBLOCK` flag to ensure that any operations are non-blocking. During that time, it is an error for your application to modify the file descriptor directly. However, you may pass the file descriptor to this method or the [`dispatch_read`](dispatch_read.md) function. You may also use the file descriptor to create a new dispatch I/O channel. The system relinquishes control of the file descriptor before calling your handler, so it is safe to modify the file descriptor again from your handler code.

The handler you provide is not queued for execution until the write operation finishes. In addition, if you issue multiple read or write calls for the same file descriptor using the convenience APIs, all of those operations must complete before any of the associated handlers are queued. If you are already using the file descriptor with another channel, use the [`write(offset:data:queue:ioHandler:)`](dispatchio/write(offset:data:queue:iohandler:).md) method to write data to the channel instead of this method.

## Parameters

- `toFileDescriptor`: The file descriptor to use for writing the data. The file descriptor must be open and configured for writing.
- `data`: The data to write.
- `queue`: The dispatch queue on which to submit the handler block.
- `handler`: The handler to execute once the channel is closed. This block has no return value and takes the following parameters:

## See Also

- [func write(offset: off_t, data: DispatchData, queue: DispatchQueue, ioHandler: (Bool, DispatchData?, Int32) -> Void)](dispatchio/write(offset:data:queue:iohandler:).md)
  Schedules an asynchronous write operation for the specified channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchio/write(tofiledescriptor:data:runninghandleron:handler:))*