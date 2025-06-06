# destroy()

**Framework**: IOUSBHost  
**Kind**: method

Removes underlying allocations and connections from the USB host object.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func destroy()
```

#### Discussion

When you no longer need the [`IOUSBHostObject`](iousbhostobject.md), call [`destroy()`](iousbhostobject/destroy().md). This method destroys the connection with the kernel object and deregisters interest on [`io_service_t`](https://developer.apple.com/documentation/iokit/io_service_t). Calling [`destroy()`](iousbhostobject/destroy().md) multiple times has no effect.

## See Also

- [struct IOUSBHostObjectInitOptions](iousbhostobjectinitoptions.md)
  Options for initializing the host object.
- [typealias IOUSBHostInterestHandler](iousbhostinteresthandler.md)
  The callback that handles underlying service-state changes.
- [var ioService: io_service_t](iousbhostobject/ioservice.md)
  A reference to the kernel object.
- [var queue: dispatch_queue_t](iousbhostobject/queue.md)
  The queue for servicing input/output requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/destroy())*