# queue

**Framework**: IOUSBHost  
**Kind**: property

The queue for servicing input/output requests.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var queue: dispatch_queue_t { get }
```

#### Discussion

Use this queue only for asynchronous input/output requests.

## See Also

- [struct IOUSBHostObjectInitOptions](iousbhostobjectinitoptions.md)
  Options for initializing the host object.
- [typealias IOUSBHostInterestHandler](iousbhostinteresthandler.md)
  The callback that handles underlying service-state changes.
- [var ioService: io_service_t](iousbhostobject/ioservice.md)
  A reference to the kernel object.
- [func destroy()](iousbhostobject/destroy.md)
  Removes underlying allocations and connections from the USB host object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/queue)*