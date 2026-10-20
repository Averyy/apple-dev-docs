# sendIORequest(with:frameList:frameListCount:firstFrameNumber:)

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Sends a request on an isochronous endpoint.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+ - Deprecated in 27.0

## Declaration

```swift
func sendIORequest(with data: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64) throws
```

```objc
- (BOOL) sendIORequestWithData:(NSMutableData *) data frameList:(IOUSBHostIsochronousFrame *) frameList frameListCount:(NSUInteger) frameListCount firstFrameNumber:(uint64_t) firstFrameNumber error:(NSError **) error;
```

#### Discussion

This method issues synchronous isochronous requests. The caller allocates and initializes an array of [`IOUSBHostIsochronousFrame`](../iousbhostisochronousframe.md) structures to describe the transferred frames.

## Parameters

- `data`: An [`NSMutableData`](../../Foundation/nsmutabledata.md) object defining the memory to use for the transfer.
- `frameList`: A pointer to the first element in an [`IOUSBHostIsochronousFrame`](../iousbhostisochronousframe.md) array. The array must contain at least `frameListCount` elements.
- `frameListCount`: The number of elements in `frameList`.
- `firstFrameNumber`: The frame number the request begins on. Query the current frame number with [`frameNumberWithTime:`](../iousbhostobject/framenumberwithtime_.md). If `0`, the transfer starts on the next available frame (XHCI only).

## See Also

### Sending Isochronous I/O
- [typealias IOUSBHostIsochronousCompletionHandler](../iousbhostisochronouscompletionhandler.md)
  A completion handler for asynchronous isochronous transfers.
- [typealias IOUSBHostTime](../iousbhosttime.md)
  The absolute time.
- [struct IOUSBHostIsochronousFrame](../iousbhostisochronousframe.md)
  A structure that represents a single frame in an isochronous transfer.
- [func enqueueIORequest(with: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64, completionHandler: ((IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousFrame>) -> Void)?) throws](./enqueueiorequest%28with,framelist,framelistcount,firstframenumber,completionhandler%29.md)
  Enqueues a request on an isochronous endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/sendiorequest(with:framelist:framelistcount:firstframenumber:))*