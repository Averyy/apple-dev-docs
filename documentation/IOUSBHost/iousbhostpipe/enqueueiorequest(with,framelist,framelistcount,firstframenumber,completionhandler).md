# enqueueIORequest(with:frameList:frameListCount:firstFrameNumber:completionHandler:)

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Enqueues a request on an isochronous endpoint.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+ - Deprecated in 27.0

## Declaration

```swift
func enqueueIORequest(with data: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64, completionHandler: (@Sendable (IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousFrame>) -> Void)? = nil) throws
```

```swift
func enqueueIORequest(with data: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64) async throws -> (IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousFrame>)
```

```objc
- (BOOL) enqueueIORequestWithData:(NSMutableData *) data frameList:(IOUSBHostIsochronousFrame *) frameList frameListCount:(NSUInteger) frameListCount firstFrameNumber:(uint64_t) firstFrameNumber error:(NSError **) error completionHandler:(IOUSBHostIsochronousCompletionHandler) completionHandler;
```

#### Return Value

`YES` if the request queues successfully; otherwise, `NO`.

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func enqueueIORequest(with data: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64) async throws -> (IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousFrame>)
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

This method issues asynchronous isochronous requests. The caller allocates and initializes an array of [`IOUSBHostIsochronousFrame`](../iousbhostisochronousframe.md) structures to describe the transferred frames.

## Parameters

- `data`: An [`NSMutableData`](../../Foundation/nsmutabledata.md) object defining the memory to use for the transfer.
- `frameList`: A pointer to the first element in an [`IOUSBHostIsochronousFrame`](../iousbhostisochronousframe.md) array. The array must contain at least `frameListCount` elements.
- `frameListCount`: The number of elements in `frameList`.
- `firstFrameNumber`: The frame number the request should begin on. Query the current frame number with [`frameNumberWithTime:`](../iousbhostobject/framenumberwithtime_.md). If `0`, the transfer starts on the next available frame (XHCI only).
- `completionHandler`: An [`IOUSBHostIsochronousCompletionHandler`](../iousbhostisochronouscompletionhandler.md) that runs when the request completes, or times out if the call returns successfully. The `completionHandler` doesn’t run if the method returns with an error.

## See Also

### Sending Isochronous I/O
- [typealias IOUSBHostIsochronousCompletionHandler](../iousbhostisochronouscompletionhandler.md)
  A completion handler for asynchronous isochronous transfers.
- [typealias IOUSBHostTime](../iousbhosttime.md)
  The absolute time.
- [struct IOUSBHostIsochronousFrame](../iousbhostisochronousframe.md)
  A structure that represents a single frame in an isochronous transfer.
- [func sendIORequest(with: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64) throws](./sendiorequest%28with,framelist,framelistcount,firstframenumber%29.md)
  Sends a request on an isochronous endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/enqueueiorequest(with:framelist:framelistcount:firstframenumber:completionhandler:))*