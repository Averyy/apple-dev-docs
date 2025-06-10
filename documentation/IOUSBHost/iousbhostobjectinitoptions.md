# IOUSBHostObjectInitOptions

**Framework**: IOUSBHost  
**Kind**: struct

Options for initializing the host object.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
struct IOUSBHostObjectInitOptions
```

## Topics

### Options
- [static var deviceCapture: IOUSBHostObjectInitOptions](iousbhostobjectinitoptions/devicecapture.md)
  The option to capture the device and terminate existing drivers.
### Initializing the Structure
- [init(rawValue: UInt)](iousbhostobjectinitoptions/init(rawvalue:).md)
  Initializes the object.
### Type Properties
- [static var deviceSeize: IOUSBHostObjectInitOptions](iousbhostobjectinitoptions/deviceseize.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [typealias IOUSBHostInterestHandler](iousbhostinteresthandler.md)
  The callback that handles underlying service-state changes.
- [var ioService: io_service_t](iousbhostobject/ioservice.md)
  A reference to the kernel object.
- [var queue: dispatch_queue_t](iousbhostobject/queue.md)
  The queue for servicing input/output requests.
- [func destroy()](iousbhostobject/destroy.md)
  Removes underlying allocations and connections from the USB host object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobjectinitoptions)*