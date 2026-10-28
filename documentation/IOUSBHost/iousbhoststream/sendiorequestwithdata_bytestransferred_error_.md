# sendIORequestWithData:bytesTransferred:error:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Sends an input/output request on the stream.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
- (BOOL) sendIORequestWithData:(NSMutableData *) data bytesTransferred:(NSUInteger *) bytesTransferred error:(NSError **) error;
```

## Return Value

`YES` if the request completes successfully; otherwise, `NO`.

## Discussion

This method sends a synchronous request on the stream, and won’t return until the request completes

> **Note**:  Completion timeouts aren’t applicable to streams.

## Parameters

- `data`: An [`NSMutableData`](../../Foundation/nsmutabledata.md) object defining the memory to use for the transfer.
- `bytesTransferred`: An [`NSUInteger`](../../ObjectiveC/nsuinteger.md) reference that updates with the byte count of the completed data phase.
- `error`: An [`NSError`](../../Foundation/nserror.md) that contains an [`IOReturn`](../../iokit/ioreturn.md) value on failure.

## See Also

### Sending I/O
- [typealias IOUSBHostCompletionHandler](../iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [func enqueueIORequest(with: NSMutableData?, completionHandler: ((IOReturn, Int) -> Void)?) throws](./enqueueiorequest%28with,completionhandler%29.md)
  Enqueues an input/output request on the stream.
- [func abort(with: IOUSBHostAbortOption) throws](./abort%28with%29.md)
  Aborts pending input/output requests.
- [func abort() throws](./abort%28%29.md)
  Aborts pending input/output requests synchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhoststream/sendiorequestwithdata:bytestransferred:error:)*