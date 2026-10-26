# IOUSBHostIsochronousCompletionHandler

**Framework**: IOUSBHost  
**Kind**: typealias  
**Role**: Type Alias

A completion handler for asynchronous isochronous transfers.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
typealias IOUSBHostIsochronousCompletionHandler = (IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousFrame>) -> Void
```

```c
typedef void (^)(int, struct IOUSBHostIsochronousFrame *) IOUSBHostIsochronousCompletionHandler;
```

## Parameters

- `status`: The result code for isochronous transfer.
- `frameList`: The frame list of [`IOUSBHostIsochronousFrame`](./iousbhostisochronousframe.md) that [`enqueueIORequest(with:frameList:frameListCount:firstFrameNumber:completionHandler:)`](./iousbhostpipe/enqueueiorequest%28with,framelist,framelistcount,firstframenumber,completionhandler%29.md) passes.

## See Also

### Sending Isochronous I/O
- [typealias IOUSBHostTime](./iousbhosttime.md)
  The absolute time.
- [struct IOUSBHostIsochronousFrame](./iousbhostisochronousframe.md)
  A structure that represents a single frame in an isochronous transfer.
- [func enqueueIORequest(with: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64, completionHandler: ((IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousFrame>) -> Void)?) throws](./iousbhostpipe/enqueueiorequest%28with,framelist,framelistcount,firstframenumber,completionhandler%29.md)
  Enqueues a request on an isochronous endpoint.
- [func sendIORequest(with: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64) throws](./iousbhostpipe/sendiorequest%28with,framelist,framelistcount,firstframenumber%29.md)
  Sends a request on an isochronous endpoint.
- [- abortWithOption:error:](./iousbhostpipe/abortwithoption_error_.md)
  Aborts pending input/output requests.
- [- abortWithError:](./iousbhostpipe/abortwitherror_.md)
  Aborts pending input/output requests synchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostisochronouscompletionhandler)*