# abortWithOption:error:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Aborts pending input/output requests.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
- (BOOL) abortWithOption:(IOUSBHostAbortOption) option error:(NSError **) error;
```

#### Return Value

`YES` if the abort completes successfully; otherwise, `NO`.

#### Discussion

This method aborts all pending input/output requests. If the `option` argument is [`IOUSBHostAbortOption.synchronous`](../iousbhostabortoption/synchronous.md), this method blocks any new ones.

## Parameters

- `option`: An [`IOUSBHostAbortOption`](../iousbhostabortoption.md). The default is [`IOUSBHostAbortOption.synchronous`](../iousbhostabortoption/synchronous.md).
- `error`: An [`NSError`](../../Foundation/nserror.md) that contains an [`IOReturn`](../../kernel/ioreturn.md) value on failure.

## Topics

### Options
- [enum IOUSBHostAbortOption](../iousbhostabortoption.md)
  Options for aborting pending input/output requests.

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
- [- abortWithError:](./abortwitherror_.md)
  Aborts pending input/output requests synchronously.
- [func clearStall() throws](./clearstall%28%29.md)
  Clears the halt condition of the pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/abortwithoption:error:)*