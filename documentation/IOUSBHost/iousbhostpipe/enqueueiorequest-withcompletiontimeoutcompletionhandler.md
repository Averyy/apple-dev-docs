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

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func enqueueIORequest(with data: NSMutableData?, completionTimeout: TimeInterval) async throws -> (IOReturn, Int)
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Use this method to issue an asynchronous input/output request on a bulk or interrupt pipe.

## Parameters

- `data`: An   object defining the memory to use for the transfer. Use   to send a zero-length packet.
- `completionTimeout`: A   value representing the timeout of the request. If  , the request never times out. Use   unless there’s a need for a specific timeout.
- `completionHandler`: An   that runs when the request completes, or times out after the call returns successfully. If the method returns with an error, the completion handler doesn’t run.

## See Also

- [typealias IOUSBHostCompletionHandler](iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [let IOUSBHostDefaultControlCompletionTimeout: TimeInterval](iousbhostdefaultcontrolcompletiontimeout.md)
  The default completion timeout for input/output requests.
- [func clearStall() throws](iousbhostpipe/clearstall.md)
  Clears the halt condition of the pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/enqueueiorequest(with:completiontimeout:completionhandler:))*