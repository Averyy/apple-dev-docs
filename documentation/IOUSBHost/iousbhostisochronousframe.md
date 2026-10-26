# IOUSBHostIsochronousFrame

**Framework**: IOUSBHost  
**Kind**: struct  
**Role**: Structure

A structure that represents a single frame in an isochronous transfer.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+ - Deprecated in 27.0

> **Deprecated**: Use IOUSBHostIsochronousTransaction instead

## Declaration

```swift
struct IOUSBHostIsochronousFrame
```

```c
typedef struct IOUSBHostIsochronousFrame { ... } IOUSBHostIsochronousFrame;
```

## Topics

### Frame Structure
- [var status: IOReturn](./iousbhostisochronousframe/status.md)
  The completion status for an individual frame.
- [var requestCount: UInt32](./iousbhostisochronousframe/requestcount.md)
  The number of requested bytes to transfer for the frame.
- [var completeCount: UInt32](./iousbhostisochronousframe/completecount.md)
  The number of bytes that the system actually transferred for the frame.
- [var timeStamp: IOUSBHostTime](./iousbhostisochronousframe/timestamp.md)
  The observed time for the frame’s completion.
### Initializing the Structure
- [init()](./iousbhostisochronousframe/init%28%29.md)
  Creates a new frame structure.
### Initializers
- [init(status: IOReturn, requestCount: UInt32, completeCount: UInt32, reserved: UInt32, timeStamp: IOUSBHostTime)](./iousbhostisochronousframe/init%28status,requestcount,completecount,reserved,timestamp%29.md)
### Instance Properties
- [var reserved: UInt32](./iousbhostisochronousframe/reserved.md)
- [var completeCount: UInt32](./iousbhostisochronousframe/completecount.md)
  The number of bytes that the system actually transferred for the frame.
- [var requestCount: UInt32](./iousbhostisochronousframe/requestcount.md)
  The number of requested bytes to transfer for the frame.
- [var reserved: UInt32](./iousbhostisochronousframe/reserved.md)
- [var status: IOReturn](./iousbhostisochronousframe/status.md)
  The completion status for an individual frame.
- [var timeStamp: IOUSBHostTime](./iousbhostisochronousframe/timestamp.md)
  The observed time for the frame’s completion.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Sending Isochronous I/O
- [typealias IOUSBHostIsochronousCompletionHandler](./iousbhostisochronouscompletionhandler.md)
  A completion handler for asynchronous isochronous transfers.
- [typealias IOUSBHostTime](./iousbhosttime.md)
  The absolute time.
- [func enqueueIORequest(with: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64, completionHandler: ((IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousFrame>) -> Void)?) throws](./iousbhostpipe/enqueueiorequest%28with,framelist,framelistcount,firstframenumber,completionhandler%29.md)
  Enqueues a request on an isochronous endpoint.
- [func sendIORequest(with: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64) throws](./iousbhostpipe/sendiorequest%28with,framelist,framelistcount,firstframenumber%29.md)
  Sends a request on an isochronous endpoint.
- [- abortWithOption:error:](./iousbhostpipe/abortwithoption_error_.md)
  Aborts pending input/output requests.
- [- abortWithError:](./iousbhostpipe/abortwitherror_.md)
  Aborts pending input/output requests synchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostisochronousframe)*