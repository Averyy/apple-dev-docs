# sendIORequestWithData:bytesTransferred:completionTimeout:error:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Sends an input/output request on the pipe.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
- (BOOL) sendIORequestWithData:(NSMutableData *) data bytesTransferred:(NSUInteger *) bytesTransferred completionTimeout:(NSTimeInterval) completionTimeout error:(NSError **) error;
```

## Return Value

`YES` if the request completes successfully; otherwise, `NO`.

## Discussion

Use this method to issue a synchronous input/output request on a bulk or interrupt pipe. The method doesn’t return until the request completes or times out.

## Parameters

- `data`: An [`NSMutableData`](../../Foundation/nsmutabledata.md) object defining the memory to use for the transfer. Use `nil` to send a zero-length packet.
- `bytesTransferred`: An [`NSUInteger`](../../ObjectiveC/nsuinteger.md) reference that updates with the number of bytes the request transferred.
- `completionTimeout`: A [`TimeInterval`](../../Foundation/timeinterval.md) value representing the timeout of the request. If `0`, the request never times out. Use [`IOUSBHostDefaultControlCompletionTimeout`](../iousbhostdefaultcontrolcompletiontimeout.md) unless there’s a need for a specific timeout.
- `error`: An [`NSError`](../../Foundation/nserror.md) that contains an [`IOReturn`](../../kernel/ioreturn.md) value on failure.

## See Also

### Sending Bulk and Interrupt I/O
- [typealias IOUSBHostCompletionHandler](../iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [let IOUSBHostDefaultControlCompletionTimeout: TimeInterval](../iousbhostdefaultcontrolcompletiontimeout.md)
  The default completion timeout for input/output requests.
- [func enqueueIORequest(with: NSMutableData?, completionTimeout: TimeInterval, completionHandler: ((IOReturn, Int) -> Void)?) throws](./enqueueiorequest%28with,completiontimeout,completionhandler%29.md)
  Enqueues an input/output request on the pipe.
- [- abortWithOption:error:](./abortwithoption_error_.md)
  Aborts pending input/output requests.
- [- abortWithError:](./abortwitherror_.md)
  Aborts pending input/output requests synchronously.
- [func clearStall() throws](./clearstall%28%29.md)
  Clears the halt condition of the pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/sendiorequestwithdata:bytestransferred:completiontimeout:error:)*