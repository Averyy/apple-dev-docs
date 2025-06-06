# clearStall()

**Framework**: IOUSBHost  
**Kind**: method

Clears the halt condition of the pipe.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func clearStall() throws
```

#### Discussion

When a bulk or interrupt USB endpoint encounters any input/output error other than a timeout, it transitions to a halted state. It must also clear to perform additional input/output requests on the endpoint.

This method clears the halted condition for the endpoint. It also sends a `CLEAR_TT_BUFFER` control request (See USB 2.0, 11.24.2.3.) to an intermediate hub, if necessary. All pending input/output requests on the endpoint abort, and the data toggle for the endpoint resets.

## See Also

- [typealias IOUSBHostCompletionHandler](iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [let IOUSBHostDefaultControlCompletionTimeout: TimeInterval](iousbhostdefaultcontrolcompletiontimeout.md)
  The default completion timeout for input/output requests.
- [func enqueueIORequest(with: NSMutableData?, completionTimeout: TimeInterval, completionHandler: IOUSBHostCompletionHandler?) throws](iousbhostpipe/enqueueiorequest(with:completiontimeout:completionhandler:).md)
  Enqueues an input/output request on the pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/clearstall())*