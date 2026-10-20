# destroy()

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Removes underlying allocations and connections from the USB host object.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func destroy()
```

```objc
- (void) destroy;
```

#### Discussion

When you no longer need the [`IOUSBHostObject`](../iousbhostobject.md), call [`destroy()`](./destroy%28%29.md). This method destroys the connection with the kernel object and deregisters interest on [`io_service_t`](../../iokit/io_service_t.md). Calling [`destroy()`](./destroy%28%29.md) multiple times has no effect.

## See Also

### Managing the Object Life Cycle
- [struct IOUSBHostObjectInitOptions](../iousbhostobjectinitoptions.md)
  Options for initializing the host object.
- [typealias IOUSBHostInterestHandler](../iousbhostinteresthandler.md)
  The callback that handles underlying service-state changes.
- [var ioService: io_service_t](./ioservice.md)
  A reference to the kernel object.
- [var queue: dispatch_queue_t](./queue.md)
  The queue for servicing input/output requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/destroy())*