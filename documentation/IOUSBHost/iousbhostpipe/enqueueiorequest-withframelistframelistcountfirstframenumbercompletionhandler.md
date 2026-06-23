# enqueueIORequest(with:frameList:frameListCount:firstFrameNumber:completionHandler:)

**Framework**: IOUSBHost  
**Kind**: method

Enqueues a request on an isochronous endpoint.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func enqueueIORequest(with data: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64) async throws -> (IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousFrame>)
```

#### Return Value

`YES` if the request queues successfully; otherwise, `NO`.

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func enqueueIORequest(with data: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64) async throws -> (IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousFrame>)
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This method issues asynchronous isochronous requests. The caller allocates and initializes an array of [`IOUSBHostIsochronousFrame`](iousbhostisochronousframe.md) structures to describe the transferred frames.

## Parameters

- `data`: An [`NSMutableData`](https://developer.apple.com/documentation/Foundation/NSMutableData) object defining the memory to use for the transfer.
- `frameList`: A pointer to the first element in an [`IOUSBHostIsochronousFrame`](iousbhostisochronousframe.md) array. The array must contain at least `frameListCount` elements.
- `frameListCount`: The number of elements in `frameList`.
- `firstFrameNumber`: The frame number the request should begin on. Query the current frame number with [`frameNumberWithTime:`](iousbhostobject/framenumberwithtime:.md). If `0`, the transfer starts on the next available frame (XHCI only).
- `completionHandler`: An [`IOUSBHostIsochronousCompletionHandler`](iousbhostisochronouscompletionhandler.md) that runs when the request completes, or times out if the call returns successfully. The `completionHandler` doesn’t run if the method returns with an error.

## See Also

- [typealias IOUSBHostIsochronousCompletionHandler](iousbhostisochronouscompletionhandler.md)
  A completion handler for asynchronous isochronous transfers.
- [typealias IOUSBHostTime](iousbhosttime.md)
  The absolute time.
- [struct IOUSBHostIsochronousFrame](iousbhostisochronousframe.md)
  A structure that represents a single frame in an isochronous transfer.
- [func sendIORequest(with: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64) throws](iousbhostpipe/sendiorequest(with:framelist:framelistcount:firstframenumber:).md)
  Sends a request on an isochronous endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/enqueueiorequest(with:framelist:framelistcount:firstframenumber:completionhandler:))*