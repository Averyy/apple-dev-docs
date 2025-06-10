# IOUSBHostPipe

**Framework**: IOUSBHost  
**Kind**: class

The class that sends control, bulk, interrupt, and isochronous input/output requests for function drivers, and manages stream capabilities.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostPipe
```

#### Overview

The client creates pipe objects using [`copyPipe(withAddress:)`](iousbhostinterface/copypipe(withaddress:).md).

## Topics

### Sending Bulk and Interrupt I/O
- [typealias IOUSBHostCompletionHandler](iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [let IOUSBHostDefaultControlCompletionTimeout: TimeInterval](iousbhostdefaultcontrolcompletiontimeout.md)
  The default completion timeout for input/output requests.
- [func enqueueIORequest(with: NSMutableData?, completionTimeout: TimeInterval, completionHandler: ((IOReturn, Int) -> Void)?) throws](iousbhostpipe/enqueueiorequest(with:completiontimeout:completionhandler:).md)
  Enqueues an input/output request on the pipe.
- [func clearStall() throws](iousbhostpipe/clearstall.md)
  Clears the halt condition of the pipe.
### Sending Isochronous I/O
- [typealias IOUSBHostIsochronousCompletionHandler](iousbhostisochronouscompletionhandler.md)
  A completion handler for asynchronous isochronous transfers.
- [typealias IOUSBHostTime](iousbhosttime.md)
  The absolute time.
- [struct IOUSBHostIsochronousFrame](iousbhostisochronousframe.md)
  A structure that represents a single frame in an isochronous transfer.
- [func enqueueIORequest(with: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64, completionHandler: ((IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousFrame>) -> Void)?) throws](iousbhostpipe/enqueueiorequest(with:framelist:framelistcount:firstframenumber:completionhandler:).md)
  Enqueues a request on an isochronous endpoint.
- [func sendIORequest(with: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64) throws](iousbhostpipe/sendiorequest(with:framelist:framelistcount:firstframenumber:).md)
  Sends a request on an isochronous endpoint.
### Sending Control Requests
- [func IOUSBHostDeviceRequestType(tIOUSBDeviceRequestDirectionValue, tIOUSBDeviceRequestTypeValue, tIOUSBDeviceRequestRecipientValue) -> UInt8](iousbhostdevicerequesttype(_:_:_:).md)
  Creates the request type field of a device request.
- [let IOUSBHostDefaultControlCompletionTimeout: TimeInterval](iousbhostdefaultcontrolcompletiontimeout.md)
  The default completion timeout for input/output requests.
- [typealias IOUSBHostCompletionHandler](iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
### Managing Periodic Bandwidth
- [struct IOUSBHostIOSourceDescriptors](iousbhostiosourcedescriptors.md)
  The descriptors for a single endpoint.
- [func adjust(with: UnsafePointer<IOUSBHostIOSourceDescriptors>) throws](iousbhostpipe/adjust(with:).md)
  Adjusts the behavior of periodic endpoints to consume a different amount of bus bandwidth.
- [var descriptors: UnsafePointer<IOUSBHostIOSourceDescriptors>](iousbhostpipe/descriptors.md)
  A property that retrieves the current endpoint descriptors controlling the endpoint.
- [var originalDescriptors: UnsafePointer<IOUSBHostIOSourceDescriptors>](iousbhostpipe/originaldescriptors.md)
  A property that retrieves the original endpoint descriptors from the pipe at the point of creation.
### Enabling Power Savings
- [func setIdleTimeout(TimeInterval) throws](iousbhostpipe/setidletimeout(_:).md)
  Sets the desired idle suspend timeout for the interface.
- [var idleTimeout: TimeInterval](iousbhostpipe/idletimeout.md)
  A property that retrieves the current idle suspend timeout.
### Managing Streams
- [func enableStreams() throws](iousbhostpipe/enablestreams.md)
  Enables streams for the pipe.
- [func copyStream(withStreamID: Int) throws -> IOUSBHostStream](iousbhostpipe/copystream(withstreamid:).md)
  Returns the stream for a stream ID.
- [func disableStreams() throws](iousbhostpipe/disablestreams.md)
  Disables streams for the pipe.
### Instance Methods
- [func enqueueIORequest(with: NSMutableData, transactionList: UnsafeMutablePointer<IOUSBHostIsochronousTransaction>, transactionListCount: Int, firstFrameNumber: UInt64, options: IOUSBHostIsochronousTransferOptions, completionHandler: ((IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousTransaction>) -> Void)?) throws](iousbhostpipe/enqueueiorequest(with:transactionlist:transactionlistcount:firstframenumber:options:completionhandler:).md)
- [func sendIORequest(with: NSMutableData, transactionList: UnsafeMutablePointer<IOUSBHostIsochronousTransaction>, transactionListCount: Int, firstFrameNumber: UInt64, options: IOUSBHostIsochronousTransferOptions) throws](iousbhostpipe/sendiorequest(with:transactionlist:transactionlistcount:firstframenumber:options:).md)

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
- [class IOUSBHostStream](iousbhoststream.md)
  The class responsible for sending stream data for function drivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe)*