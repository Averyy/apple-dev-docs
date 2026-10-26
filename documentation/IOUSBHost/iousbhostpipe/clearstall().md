# clearStall()

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Clears the halt condition of the pipe.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func clearStall() throws
```

```objc
- (BOOL) clearStallWithError:(NSError **) error;
```

#### Discussion

When a bulk or interrupt USB endpoint encounters any input/output error other than a timeout, it transitions to a halted state. It must also clear to perform additional input/output requests on the endpoint.

This method clears the halted condition for the endpoint. It also sends a `CLEAR_TT_BUFFER` control request (See USB 2.0, 11.24.2.3.) to an intermediate hub, if necessary. All pending input/output requests on the endpoint abort, and the data toggle for the endpoint resets.

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
- [- abortWithError:](./abortwitherror_.md)
  Aborts pending input/output requests synchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/clearstall())*