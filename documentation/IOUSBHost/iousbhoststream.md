# IOUSBHostStream

**Framework**: IOUSBHost  
**Kind**: class  
**Role**: Class

The class responsible for sending stream data for function drivers.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostStream
```

```objc
@interface IOUSBHostStream : IOUSBHostIOSource
```

#### Overview

The [`copyStream(withStreamID:)`](./iousbhostpipe/copystream%28withstreamid%29.md) method creates stream objects.

## Topics

### Sending I/O
- [typealias IOUSBHostCompletionHandler](./iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [func enqueueIORequest(with: NSMutableData?, completionHandler: ((IOReturn, Int) -> Void)?) throws](./iousbhoststream/enqueueiorequest%28with,completionhandler%29.md)
  Enqueues an input/output request on the stream.
- [func abort(with: IOUSBHostAbortOption) throws](./iousbhoststream/abort%28with%29.md)
  Aborts pending input/output requests.
- [func abort() throws](./iousbhoststream/abort%28%29.md)
  Aborts pending input/output requests synchronously.
- [- sendIORequestWithData:bytesTransferred:error:](./iousbhoststream/sendiorequestwithdata_bytestransferred_error_.md)
  Sends an input/output request on the stream.
### Getting the Pipe Object
- [var hostPipe: IOUSBHostPipe](./iousbhoststream/hostpipe.md)
  The pipe that creates the stream.
### Getting the Stream ID
- [var streamID: Int](./iousbhoststream/streamid.md)
  The ID for the stream.

## Relationships

### Inherits From
- [IOUSBHostIOSource](./iousbhostiosource.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Function Drivers
- [class IOUSBHostInterface](./iousbhostinterface.md)
  The class for accessing USB-related services.
- [class IOUSBHostPipe](./iousbhostpipe.md)
  The class that sends control, bulk, interrupt, and isochronous input/output requests for function drivers, and manages stream capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhoststream)*