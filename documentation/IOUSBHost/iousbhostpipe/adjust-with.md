# adjust(with:)

**Framework**: IOUSBHost  
**Kind**: method

Adjusts the behavior of periodic endpoints to consume a different amount of bus bandwidth.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func adjust(with descriptors: UnsafePointer<IOUSBHostIOSourceDescriptors>) throws
```

#### Discussion

During creation, periodic (interrupt and isochronous) endpoints reserve bus bandwidth to allow for maximum packet size, mult (the maximum number of packets that this endpoint supports), burst size, and the endpoint service interval.

If an endpoint won’t use all of the allocated bandwidth, use [`adjust(with:)`](iousbhostpipe/adjust(with:).md) to reduce the bandwidth reserved for the endpoint. Copy the original endpoint descriptors, adjust maximum packet size, mult, burst size, and interval, then pass to [`adjust(with:)`](iousbhostpipe/adjust(with:).md). The altered descriptors must pass validation from the kernel for policy changes to process.

## Parameters

- `descriptors`: A reference to   describing the new endpoint policy.

## See Also

- [struct IOUSBHostIOSourceDescriptors](iousbhostiosourcedescriptors.md)
  The descriptors for a single endpoint.
- [var descriptors: UnsafePointer<IOUSBHostIOSourceDescriptors>](iousbhostpipe/descriptors.md)
  A property that retrieves the current endpoint descriptors controlling the endpoint.
- [var originalDescriptors: UnsafePointer<IOUSBHostIOSourceDescriptors>](iousbhostpipe/originaldescriptors.md)
  A property that retrieves the original endpoint descriptors from the pipe at the point of creation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/adjust(with:))*