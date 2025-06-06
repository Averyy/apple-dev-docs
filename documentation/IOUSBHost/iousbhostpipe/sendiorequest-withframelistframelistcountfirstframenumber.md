# sendIORequest(with:frameList:frameListCount:firstFrameNumber:)

**Framework**: IOUSBHost  
**Kind**: method

Sends a request on an isochronous endpoint.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func sendIORequest(with data: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64) throws
```

#### Discussion

This method issues synchronous isochronous requests. The caller allocates and initializes an array of [`IOUSBHostIsochronousFrame`](iousbhostisochronousframe.md) structures to describe the transferred frames.

## Parameters

- `data`: An   object defining the memory to use for the transfer.
- `frameList`: A pointer to the first element in an   array. The array must contain at least   elements.
- `frameListCount`: The number of elements in  .
- `firstFrameNumber`: The frame number the request begins on. Query the current frame number with  . If  , the transfer starts on the next available frame (XHCI only).

## See Also

- [typealias IOUSBHostIsochronousCompletionHandler](iousbhostisochronouscompletionhandler.md)
  A completion handler for asynchronous isochronous transfers.
- [typealias IOUSBHostTime](iousbhosttime.md)
  The absolute time.
- [struct IOUSBHostIsochronousFrame](iousbhostisochronousframe.md)
  A structure that represents a single frame in an isochronous transfer.
- [func enqueueIORequest(with: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64, completionHandler: IOUSBHostIsochronousCompletionHandler?) throws](iousbhostpipe/enqueueiorequest(with:framelist:framelistcount:firstframenumber:completionhandler:).md)
  Enqueues a request on an isochronous endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/sendiorequest(with:framelist:framelistcount:firstframenumber:))*