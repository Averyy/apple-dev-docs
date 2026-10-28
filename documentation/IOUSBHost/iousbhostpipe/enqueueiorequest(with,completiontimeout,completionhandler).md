# enqueueIORequest(with:completionTimeout:completionHandler:)

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Enqueues an input/output request on the pipe.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func enqueueIORequest(with data: NSMutableData?, completionTimeout: TimeInterval, completionHandler: (@Sendable (IOReturn, Int) -> Void)? = nil) throws
```

```swift
func enqueueIORequest(with data: NSMutableData?, completionTimeout: TimeInterval) async throws -> (IOReturn, Int)
```

```objc
- (BOOL) enqueueIORequestWithData:(NSMutableData *) data completionTimeout:(NSTimeInterval) completionTimeout error:(NSError **) error completionHandler:(IOUSBHostCompletionHandler) completionHandler;
```

## Return Value

`YES` if the request completes successfully; otherwise, `NO`.

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func enqueueIORequest(with data: NSMutableData?, completionTimeout: TimeInterval) async throws -> (IOReturn, Int)
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

Use this method to issue an asynchronous input/output request on a bulk or interrupt pipe.

## Parameters

- `data`: An [`NSMutableData`](../../Foundation/nsmutabledata.md) object defining the memory to use for the transfer. Use [`nil`](../../ObjectiveC/nil-227m0.md) to send a zero-length packet.
- `completionTimeout`: A [`TimeInterval`](../../Foundation/timeinterval.md) value representing the timeout of the request. If `0`, the request never times out. Use [`IOUSBHostDefaultControlCompletionTimeout`](../iousbhostdefaultcontrolcompletiontimeout.md) unless there’s a need for a specific timeout.
- `completionHandler`: An [`IOUSBHostCompletionHandler`](../iousbhostcompletionhandler.md) that runs when the request completes, or times out after the call returns successfully. If the method returns with an error, the completion handler doesn’t run.

## See Also

### Sending Bulk and Interrupt I/O
- [typealias IOUSBHostCompletionHandler](../iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [let IOUSBHostDefaultControlCompletionTimeout: TimeInterval](../iousbhostdefaultcontrolcompletiontimeout.md)
  The default completion timeout for input/output requests.
- [func clearStall() throws](./clearstall%28%29.md)
  Clears the halt condition of the pipe.
- [- sendIORequestWithData:bytesTransferred:completionTimeout:error:](./sendiorequestwithdata_bytestransferred_completiontimeout_error_.md)
  Sends an input/output request on the pipe.
- [- abortWithOption:error:](./abortwithoption_error_.md)
  Aborts pending input/output requests.
- [- abortWithError:](./abortwitherror_.md)
  Aborts pending input/output requests synchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/enqueueiorequest(with:completiontimeout:completionhandler:))*