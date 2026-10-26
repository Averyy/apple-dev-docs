# abort()

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Aborts pending input/output requests synchronously.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func abort() throws
```

```objc
- (BOOL) abortWithError:(NSError **) error;
```

#### Discussion

Set the stream context as nonactive on the device with an out-of-band (class-defined) mechanism before calling this method, in accordance with USB 3.2, 8.12.1.4. The device won’t select a nonactive stream to become the current stream on the endpoint.

## See Also

### Sending I/O
- [typealias IOUSBHostCompletionHandler](../iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [func enqueueIORequest(with: NSMutableData?, completionHandler: ((IOReturn, Int) -> Void)?) throws](./enqueueiorequest%28with,completionhandler%29.md)
  Enqueues an input/output request on the stream.
- [func abort(with: IOUSBHostAbortOption) throws](./abort%28with%29.md)
  Aborts pending input/output requests.
- [- sendIORequestWithData:bytesTransferred:error:](./sendiorequestwithdata_bytestransferred_error_.md)
  Sends an input/output request on the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhoststream/abort())*