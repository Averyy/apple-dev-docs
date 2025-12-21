# read(offset:length:queue:ioHandler:)

**Framework**: Dispatch  
**Kind**: method

Schedules an asynchronous read operation on the specified channel.

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
func read(offset: off_t, length: Int, queue: DispatchQueue, ioHandler: @escaping (Bool, DispatchData?, Int32) -> Void)
```

#### Discussion

This function reads the specified data and submits the handler block to queue to process the data. If the `done` parameter of the handler is set to false, it means that only part of the data was read. If the `done` parameter is [`true`](https://developer.apple.com/documentation/Swift/true), it means the read operation is complete and the handler will not be submitted again. If an unrecoverable error occurs on the channel’s file descriptor, the `done` parameter is set to true and an appropriate error value is reported in the handler’s error parameter.

If the handler is submitted with the done parameter set to true, an empty data object, and an error code of 0, it means that the channel reached the end of the file.

## Parameters

- `offset`: For random-access channels, this parameter specifies the offset into the channel from which to read. The offset is specified relative to the initial file pointer of the channel’s file descriptor at the time the channel was created.   For stream-based channels, this parameter is ignored and data is read from the current position.
- `length`: The number of bytes to read from the channel. Specify   to continue reading data until an EOF is reached.
- `queue`: The dispatch queue on which to submit the   closure.
- `ioHandler`: Your block need not be reentrant. The system guarantees that only one instance of this block will be executed at any given time.

## See Also

- [class func read(fromFileDescriptor: Int32, maxLength: Int, runningHandlerOn: DispatchQueue, handler: (DispatchData, Int32) -> Void)](dispatchio/read(fromfiledescriptor:maxlength:runninghandleron:handler:).md)
  Schedules an asynchronous read operation using the specified file descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchio/read(offset:length:queue:iohandler:))*