# originalDescriptors

**Framework**: IOUSBHost  
**Kind**: property  
**Role**: Instance Property

A property that retrieves the original endpoint descriptors from the pipe at the point of creation.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var originalDescriptors: UnsafePointer<IOUSBHostIOSourceDescriptors> { get }
```

```objc
@property (readonly) const IOUSBHostIOSourceDescriptors * originalDescriptors;
```

#### Return Value

The original [`IOUSBHostIOSourceDescriptors`](../iousbhostiosourcedescriptors.md).

## See Also

### Managing Periodic Bandwidth
- [struct IOUSBHostIOSourceDescriptors](../iousbhostiosourcedescriptors.md)
  The descriptors for a single endpoint.
- [func adjust(with: UnsafePointer<IOUSBHostIOSourceDescriptors>) throws](./adjust%28with%29.md)
  Adjusts the behavior of periodic endpoints to consume a different amount of bus bandwidth.
- [var descriptors: UnsafePointer<IOUSBHostIOSourceDescriptors>](./descriptors.md)
  A property that retrieves the current endpoint descriptors controlling the endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/originaldescriptors)*