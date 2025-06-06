# IOUSBHostIsochronousFrame

**Framework**: IOUSBHost  
**Kind**: struct

A structure that represents a single frame in an isochronous transfer.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
struct IOUSBHostIsochronousFrame
```

## Topics

### Frame Structure
- [var status: IOReturn](iousbhostisochronousframe/status.md)
  The completion status for an individual frame.
- [var requestCount: UInt32](iousbhostisochronousframe/requestcount.md)
  The number of requested bytes to transfer for the frame.
- [var completeCount: UInt32](iousbhostisochronousframe/completecount.md)
  The number of bytes that the system actually transferred for the frame.
- [var timeStamp: IOUSBHostTime](iousbhostisochronousframe/timestamp.md)
  The observed time for the frame’s completion.
### Initializing the Structure
- [init()](iousbhostisochronousframe/init.md)
  Creates a new frame structure.
### Initializers
- [init(status: IOReturn, requestCount: UInt32, completeCount: UInt32, reserved: UInt32, timeStamp: IOUSBHostTime)](iousbhostisochronousframe/init(status:requestcount:completecount:reserved:timestamp:).md)
### Instance Properties
- [var reserved: UInt32](iousbhostisochronousframe/reserved.md)
- [var completeCount: UInt32](iousbhostisochronousframe/completecount.md)
  The number of bytes that the system actually transferred for the frame.
- [var requestCount: UInt32](iousbhostisochronousframe/requestcount.md)
  The number of requested bytes to transfer for the frame.
- [var reserved: UInt32](iousbhostisochronousframe/reserved.md)
- [var status: IOReturn](iousbhostisochronousframe/status.md)
  The completion status for an individual frame.
- [var timeStamp: IOUSBHostTime](iousbhostisochronousframe/timestamp.md)
  The observed time for the frame’s completion.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias IOUSBHostIsochronousCompletionHandler](iousbhostisochronouscompletionhandler.md)
  A completion handler for asynchronous isochronous transfers.
- [typealias IOUSBHostTime](iousbhosttime.md)
  The absolute time.
- [func enqueueIORequest(with: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64, completionHandler: IOUSBHostIsochronousCompletionHandler?) throws](iousbhostpipe/enqueueiorequest(with:framelist:framelistcount:firstframenumber:completionhandler:).md)
  Enqueues a request on an isochronous endpoint.
- [func sendIORequest(with: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64) throws](iousbhostpipe/sendiorequest(with:framelist:framelistcount:firstframenumber:).md)
  Sends a request on an isochronous endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostisochronousframe)*