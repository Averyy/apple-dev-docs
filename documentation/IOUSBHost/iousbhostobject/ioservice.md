# ioService

**Framework**: IOUSBHost  
**Kind**: property

A reference to the kernel object.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var ioService: io_service_t { get }
```

## See Also

- [struct IOUSBHostObjectInitOptions](iousbhostobjectinitoptions.md)
  Options for initializing the host object.
- [typealias IOUSBHostInterestHandler](iousbhostinteresthandler.md)
  The callback that handles underlying service-state changes.
- [var queue: dispatch_queue_t](iousbhostobject/queue.md)
  The queue for servicing input/output requests.
- [func destroy()](iousbhostobject/destroy.md)
  Removes underlying allocations and connections from the USB host object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/ioservice)*