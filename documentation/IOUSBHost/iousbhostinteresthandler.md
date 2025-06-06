# IOUSBHostInterestHandler

**Framework**: IOUSBHost  
**Kind**: typealias

The callback that handles underlying service-state changes.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
typealias IOUSBHostInterestHandler = (IOUSBHostObject, UInt32, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

This is the block for the `kIOGeneralInterest` handler, and handles underlying service-state changes, such as termination. See [`IOServiceInterestCallback`](https://developer.apple.com/documentation/iokit/ioserviceinterestcallback) in [`IOKit`](https://developer.apple.com/documentation/iokit) for more details. An internal serial queue separate from the input/output queue services all notifications.

## Parameters

- `hostObject`: The   of the interest notification.
- `messageType`: A   enumeration that   or the   family defines.
- `messageArgument`: An argument for the message, dependent on the message type. If the message data is larger than  ,   contains a pointer to the message data; otherwise,   contains the message data.

## See Also

- [struct IOUSBHostObjectInitOptions](iousbhostobjectinitoptions.md)
  Options for initializing the host object.
- [var ioService: io_service_t](iousbhostobject/ioservice.md)
  A reference to the kernel object.
- [var queue: dispatch_queue_t](iousbhostobject/queue.md)
  The queue for servicing input/output requests.
- [func destroy()](iousbhostobject/destroy.md)
  Removes underlying allocations and connections from the USB host object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostinteresthandler)*