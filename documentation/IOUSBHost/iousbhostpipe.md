# IOUSBHostPipe

**Framework**: IOUSBHost  
**Kind**: class  
**Role**: Class

The class that sends control, bulk, interrupt, and isochronous input/output requests for function drivers, and manages stream capabilities.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostPipe
```

```objc
@interface IOUSBHostPipe : IOUSBHostIOSource
```

#### Overview

The client creates pipe objects using [`copyPipe(withAddress:)`](./iousbhostinterface/copypipe%28withaddress%29.md).

## Topics

### Sending Bulk and Interrupt I/O
- [typealias IOUSBHostCompletionHandler](./iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [let IOUSBHostDefaultControlCompletionTimeout: TimeInterval](./iousbhostdefaultcontrolcompletiontimeout.md)
  The default completion timeout for input/output requests.
- [func enqueueIORequest(with: NSMutableData?, completionTimeout: TimeInterval, completionHandler: ((IOReturn, Int) -> Void)?) throws](./iousbhostpipe/enqueueiorequest%28with,completiontimeout,completionhandler%29.md)
  Enqueues an input/output request on the pipe.
- [func clearStall() throws](./iousbhostpipe/clearstall%28%29.md)
  Clears the halt condition of the pipe.
- [- sendIORequestWithData:bytesTransferred:completionTimeout:error:](./iousbhostpipe/sendiorequestwithdata_bytestransferred_completiontimeout_error_.md)
  Sends an input/output request on the pipe.
- [- abortWithOption:error:](./iousbhostpipe/abortwithoption_error_.md)
  Aborts pending input/output requests.
- [- abortWithError:](./iousbhostpipe/abortwitherror_.md)
  Aborts pending input/output requests synchronously.
### Sending Isochronous I/O
- [typealias IOUSBHostIsochronousCompletionHandler](./iousbhostisochronouscompletionhandler.md)
  A completion handler for asynchronous isochronous transfers.
- [typealias IOUSBHostTime](./iousbhosttime.md)
  The absolute time.
- [struct IOUSBHostIsochronousFrame](./iousbhostisochronousframe.md)
  A structure that represents a single frame in an isochronous transfer.
- [func enqueueIORequest(with: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64, completionHandler: ((IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousFrame>) -> Void)?) throws](./iousbhostpipe/enqueueiorequest%28with,framelist,framelistcount,firstframenumber,completionhandler%29.md)
  Enqueues a request on an isochronous endpoint.
- [func sendIORequest(with: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64) throws](./iousbhostpipe/sendiorequest%28with,framelist,framelistcount,firstframenumber%29.md)
  Sends a request on an isochronous endpoint.
### Sending Control Requests
- [func IOUSBHostDeviceRequestType(tIOUSBDeviceRequestDirectionValue, tIOUSBDeviceRequestTypeValue, tIOUSBDeviceRequestRecipientValue) -> UInt8](./iousbhostdevicerequesttype%28_,_,_%29.md)
  Creates the request type field of a device request.
- [let IOUSBHostDefaultControlCompletionTimeout: TimeInterval](./iousbhostdefaultcontrolcompletiontimeout.md)
  The default completion timeout for input/output requests.
- [typealias IOUSBHostCompletionHandler](./iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [- enqueueControlRequest:data:completionTimeout:error:completionHandler:](./iousbhostpipe/enqueuecontrolrequest_data_completiontimeout_error_completionhandler_.md)
  Enqueues a request on a control endpoint.
- [- enqueueControlRequest:data:error:completionHandler:](./iousbhostpipe/enqueuecontrolrequest_data_error_completionhandler_.md)
  Enqueues a request on a control endpoint with a default completion timeout.
- [- enqueueControlRequest:error:completionHandler:](./iousbhostpipe/enqueuecontrolrequest_error_completionhandler_.md)
  Enqueues a request on a control endpoint without a data phase and a default completion timeout.
- [- sendControlRequest:data:bytesTransferred:completionTimeout:error:](./iousbhostpipe/sendcontrolrequest_data_bytestransferred_completiontimeout_error_.md)
  Sends a request on a control endpoint.
- [- sendControlRequest:data:bytesTransferred:error:](./iousbhostpipe/sendcontrolrequest_data_bytestransferred_error_.md)
  Sends a request on a control endpoint with a default timeout.
- [- sendControlRequest:error:](./iousbhostpipe/sendcontrolrequest_error_.md)
  Sends a request on a control endpoint without a data phase and a default completion timeout.
### Managing Periodic Bandwidth
- [struct IOUSBHostIOSourceDescriptors](./iousbhostiosourcedescriptors.md)
  The descriptors for a single endpoint.
- [func adjust(with: UnsafePointer<IOUSBHostIOSourceDescriptors>) throws](./iousbhostpipe/adjust%28with%29.md)
  Adjusts the behavior of periodic endpoints to consume a different amount of bus bandwidth.
- [var descriptors: UnsafePointer<IOUSBHostIOSourceDescriptors>](./iousbhostpipe/descriptors.md)
  A property that retrieves the current endpoint descriptors controlling the endpoint.
- [var originalDescriptors: UnsafePointer<IOUSBHostIOSourceDescriptors>](./iousbhostpipe/originaldescriptors.md)
  A property that retrieves the original endpoint descriptors from the pipe at the point of creation.
### Enabling Power Savings
- [func setIdleTimeout(TimeInterval) throws](./iousbhostpipe/setidletimeout%28_%29.md)
  Sets the desired idle suspend timeout for the interface.
- [var idleTimeout: TimeInterval](./iousbhostpipe/idletimeout.md)
  A property that retrieves the current idle suspend timeout.
### Managing Streams
- [func enableStreams() throws](./iousbhostpipe/enablestreams%28%29.md)
  Enables streams for the pipe.
- [func copyStream(withStreamID: Int) throws -> IOUSBHostStream](./iousbhostpipe/copystream%28withstreamid%29.md)
  Returns the stream for a stream ID.
- [func disableStreams() throws](./iousbhostpipe/disablestreams%28%29.md)
  Disables streams for the pipe.
### Instance Methods
- [func enqueueIORequest(with: NSMutableData, transactionList: UnsafeMutablePointer<IOUSBHostIsochronousTransaction>, transactionListCount: Int, firstFrameNumber: UInt64, options: IOUSBHostIsochronousTransferOptions, completionHandler: ((IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousTransaction>) -> Void)?) throws](./iousbhostpipe/enqueueiorequest%28with,transactionlist,transactionlistcount,firstframenumber,options,completionhandler%29.md)
- [func sendIORequest(with: NSMutableData, transactionList: UnsafeMutablePointer<IOUSBHostIsochronousTransaction>, transactionListCount: Int, firstFrameNumber: UInt64, options: IOUSBHostIsochronousTransferOptions) throws](./iousbhostpipe/sendiorequest%28with,transactionlist,transactionlistcount,firstframenumber,options%29.md)

## Relationships

### Inherits From
- [IOUSBHostIOSource](./iousbhostiosource.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Function Drivers
- [class IOUSBHostInterface](./iousbhostinterface.md)
  The class for accessing USB-related services.
- [class IOUSBHostStream](./iousbhoststream.md)
  The class responsible for sending stream data for function drivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe)*