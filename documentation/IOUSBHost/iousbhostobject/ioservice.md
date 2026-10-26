# ioService

**Framework**: IOUSBHost  
**Kind**: property  
**Role**: Instance Property

A reference to the kernel object.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var ioService: io_service_t { get }
```

```objc
@property (readonly) io_service_t ioService;
```

## See Also

### Managing the Object Life Cycle
- [struct IOUSBHostObjectInitOptions](../iousbhostobjectinitoptions.md)
  Options for initializing the host object.
- [typealias IOUSBHostInterestHandler](../iousbhostinteresthandler.md)
  The callback that handles underlying service-state changes.
- [var queue: dispatch_queue_t](./queue.md)
  The queue for servicing input/output requests.
- [func destroy()](./destroy%28%29.md)
  Removes underlying allocations and connections from the USB host object.
- [- initWithIOService:options:queue:error:interestHandler:](./initwithioservice_options_queue_error_interesthandler_.md)
  Creates a USB host object and sets up a communication channel to the kernel.
- [- initWithIOService:queue:error:interestHandler:](./initwithioservice_queue_error_interesthandler_.md)
  Creates a USB host object and sets up a default communication channel to the kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/ioservice)*