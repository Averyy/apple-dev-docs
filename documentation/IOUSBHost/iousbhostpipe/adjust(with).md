# adjust(with:)

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Adjusts the behavior of periodic endpoints to consume a different amount of bus bandwidth.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func adjust(with descriptors: UnsafePointer<IOUSBHostIOSourceDescriptors>) throws
```

```objc
- (BOOL) adjustPipeWithDescriptors:(const IOUSBHostIOSourceDescriptors *) descriptors error:(NSError **) error;
```

#### Discussion

During creation, periodic (interrupt and isochronous) endpoints reserve bus bandwidth to allow for maximum packet size, mult (the maximum number of packets that this endpoint supports), burst size, and the endpoint service interval.

If an endpoint won’t use all of the allocated bandwidth, use [`adjust(with:)`](./adjust%28with%29.md) to reduce the bandwidth reserved for the endpoint. Copy the original endpoint descriptors, adjust maximum packet size, mult, burst size, and interval, then pass to [`adjust(with:)`](./adjust%28with%29.md). The altered descriptors must pass validation from the kernel for policy changes to process.

## Parameters

- `descriptors`: A reference to [`IOUSBHostIOSourceDescriptors`](../iousbhostiosourcedescriptors.md) describing the new endpoint policy.

## See Also

### Managing Periodic Bandwidth
- [struct IOUSBHostIOSourceDescriptors](../iousbhostiosourcedescriptors.md)
  The descriptors for a single endpoint.
- [var descriptors: UnsafePointer<IOUSBHostIOSourceDescriptors>](./descriptors.md)
  A property that retrieves the current endpoint descriptors controlling the endpoint.
- [var originalDescriptors: UnsafePointer<IOUSBHostIOSourceDescriptors>](./originaldescriptors.md)
  A property that retrieves the original endpoint descriptors from the pipe at the point of creation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/adjust(with:))*