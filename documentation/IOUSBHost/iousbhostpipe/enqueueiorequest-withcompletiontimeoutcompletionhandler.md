# enqueueIORequest(with:completionTimeout:completionHandler:)

**Framework**: IOUSBHost  
**Kind**: method

Enqueues an input/output request on the pipe.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func enqueueIORequest(with data: NSMutableData?, completionTimeout: TimeInterval) async throws -> (IOReturn, Int)
```

#### Return Value

`YES` if the request completes successfully; otherwise, `NO`.

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func enqueueIORequest(with data: NSMutableData?, completionTimeout: TimeInterval) async throws -> (IOReturn, Int)
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/swift/calling-objective-c-apis-asynchronously).

Use this method to issue an asynchronous input/output request on a bulk or interrupt pipe.

## Parameters

- `data`: An [`NSMutableData`](https://developer.apple.com/documentation/foundation/nsmutabledata) object defining the memory to use for the transfer. Use [`nil`](https://developer.apple.com/documentation/objectivec/nil-227m0) to send a zero-length packet.
- `completionTimeout`: A [`TimeInterval`](https://developer.apple.com/documentation/foundation/timeinterval) value representing the timeout of the request. If `0`, the request never times out. Use [`IOUSBHostDefaultControlCompletionTimeout`](iousbhostdefaultcontrolcompletiontimeout.md) unless there’s a need for a specific timeout.
- `completionHandler`: An [`IOUSBHostCompletionHandler`](iousbhostcompletionhandler.md) that runs when the request completes, or times out after the call returns successfully. If the method returns with an error, the completion handler doesn’t run.

## See Also

- [typealias IOUSBHostCompletionHandler](iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [let IOUSBHostDefaultControlCompletionTimeout: TimeInterval](iousbhostdefaultcontrolcompletiontimeout.md)
  The default completion timeout for input/output requests.
- [func clearStall() throws](iousbhostpipe/clearstall.md)
  Clears the halt condition of the pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/enqueueiorequest(with:completiontimeout:completionhandler:))*