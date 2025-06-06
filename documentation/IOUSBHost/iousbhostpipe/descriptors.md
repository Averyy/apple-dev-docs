# descriptors

**Framework**: IOUSBHost  
**Kind**: property

A property that retrieves the current endpoint descriptors controlling the endpoint.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var descriptors: UnsafePointer<IOUSBHostIOSourceDescriptors> { get }
```

#### Return Value

The current [`IOUSBHostIOSourceDescriptors`](iousbhostiosourcedescriptors.md).

## See Also

- [struct IOUSBHostIOSourceDescriptors](iousbhostiosourcedescriptors.md)
  The descriptors for a single endpoint.
- [func adjust(with: UnsafePointer<IOUSBHostIOSourceDescriptors>) throws](iousbhostpipe/adjust(with:).md)
  Adjusts the behavior of periodic endpoints to consume a different amount of bus bandwidth.
- [var originalDescriptors: UnsafePointer<IOUSBHostIOSourceDescriptors>](iousbhostpipe/originaldescriptors.md)
  A property that retrieves the original endpoint descriptors from the pipe at the point of creation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/descriptors)*