# IOUSBHostIsochronousCompletionHandler

**Framework**: IOUSBHost  
**Kind**: typealias

A completion handler for asynchronous isochronous transfers.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
typealias IOUSBHostIsochronousCompletionHandler = (IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousFrame>) -> Void
```

## Parameters

- `status`: The result code for isochronous transfer.
- `frameList`: The frame list of   that   passes.

## See Also

- [typealias IOUSBHostTime](iousbhosttime.md)
  The absolute time.
- [struct IOUSBHostIsochronousFrame](iousbhostisochronousframe.md)
  A structure that represents a single frame in an isochronous transfer.
- [func enqueueIORequest(with: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64, completionHandler: ((IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousFrame>) -> Void)?) throws](iousbhostpipe/enqueueiorequest(with:framelist:framelistcount:firstframenumber:completionhandler:).md)
  Enqueues a request on an isochronous endpoint.
- [func sendIORequest(with: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64) throws](iousbhostpipe/sendiorequest(with:framelist:framelistcount:firstframenumber:).md)
  Sends a request on an isochronous endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostisochronouscompletionhandler)*