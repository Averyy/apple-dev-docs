# IOUSBHostStream

**Framework**: IOUSBHost  
**Kind**: class

The class responsible for sending stream data for function drivers.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostStream
```

#### Overview

The [`copyStream(withStreamID:)`](iousbhostpipe/copystream(withstreamid:).md) method creates stream objects.

## Topics

### Sending I/O
- [typealias IOUSBHostCompletionHandler](iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [func enqueueIORequest(with: NSMutableData?, completionHandler: IOUSBHostCompletionHandler?) throws](iousbhoststream/enqueueiorequest(with:completionhandler:).md)
  Enqueues an input/output request on the stream.
- [func abort(with: IOUSBHostAbortOption) throws](iousbhoststream/abort(with:).md)
  Aborts pending input/output requests.
- [func abort() throws](iousbhoststream/abort.md)
  Aborts pending input/output requests synchronously.
### Getting the Pipe Object
- [var hostPipe: IOUSBHostPipe](iousbhoststream/hostpipe.md)
  The pipe that creates the stream.
### Getting the Stream ID
- [var streamID: Int](iousbhoststream/streamid.md)
  The ID for the stream.

## Relationships

### Inherits From
- [IOUSBHostIOSource](iousbhostiosource.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class IOUSBHostInterface](iousbhostinterface.md)
  The class for accessing USB-related services.
- [class IOUSBHostPipe](iousbhostpipe.md)
  The class that sends control, bulk, interrupt, and isochronous input/output requests for function drivers, and manages stream capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhoststream)*