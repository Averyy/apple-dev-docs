# abortWithError:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Aborts pending input/output requests synchronously.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
- (BOOL) abortWithError:(NSError **) error;
```

## Return Value

`YES` if the abort completes successfully; otherwise, `NO`.

## Discussion

This method aborts all pending input/output requests and blocks any new ones.

## Parameters

- `error`: An [`NSError`](../../Foundation/nserror.md) that contains an [`IOReturn`](../../kernel/ioreturn.md) value on failure.

## See Also

### Sending Bulk and Interrupt I/O
- [typealias IOUSBHostCompletionHandler](../iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [let IOUSBHostDefaultControlCompletionTimeout: TimeInterval](../iousbhostdefaultcontrolcompletiontimeout.md)
  The default completion timeout for input/output requests.
- [func enqueueIORequest(with: NSMutableData?, completionTimeout: TimeInterval, completionHandler: ((IOReturn, Int) -> Void)?) throws](./enqueueiorequest%28with,completiontimeout,completionhandler%29.md)
  Enqueues an input/output request on the pipe.
- [- sendIORequestWithData:bytesTransferred:completionTimeout:error:](./sendiorequestwithdata_bytestransferred_completiontimeout_error_.md)
  Sends an input/output request on the pipe.
- [- abortWithOption:error:](./abortwithoption_error_.md)
  Aborts pending input/output requests.
- [func clearStall() throws](./clearstall%28%29.md)
  Clears the halt condition of the pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/abortwitherror:)*