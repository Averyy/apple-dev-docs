# abort(with:)

**Framework**: IOUSBHost  
**Kind**: method

Aborts pending input/output requests.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func abort(with option: IOUSBHostAbortOption) throws
```

#### Discussion

Set the stream context as nonactive on the device with an out-of-band (class-defined) mechanism before calling this method, in accordance with USB 3.2, 8.12.1.4. The device won’t select a nonactive stream to become the current stream on the endpoint.

## Parameters

- `option`: A set of options.   is the default.

## Topics

### Options
- [enum IOUSBHostAbortOption](iousbhostabortoption.md)
  Options for aborting pending input/output requests.

## See Also

- [typealias IOUSBHostCompletionHandler](iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [func enqueueIORequest(with: NSMutableData?, completionHandler: IOUSBHostCompletionHandler?) throws](iousbhoststream/enqueueiorequest(with:completionhandler:).md)
  Enqueues an input/output request on the stream.
- [func abort() throws](iousbhoststream/abort.md)
  Aborts pending input/output requests synchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhoststream/abort(with:))*