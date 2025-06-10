# abort()

**Framework**: IOUSBHost  
**Kind**: method

Aborts pending input/output requests synchronously.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func abort() throws
```

#### Discussion

Set the stream context as nonactive on the device with an out-of-band (class-defined) mechanism before calling this method, in accordance with USB 3.2, 8.12.1.4. The device won’t select a nonactive stream to become the current stream on the endpoint.

## See Also

- [typealias IOUSBHostCompletionHandler](iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [func enqueueIORequest(with: NSMutableData?, completionHandler: ((IOReturn, Int) -> Void)?) throws](iousbhoststream/enqueueiorequest(with:completionhandler:).md)
  Enqueues an input/output request on the stream.
- [func abort(with: IOUSBHostAbortOption) throws](iousbhoststream/abort(with:).md)
  Aborts pending input/output requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhoststream/abort())*