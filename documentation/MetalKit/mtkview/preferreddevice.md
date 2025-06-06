# preferredDevice

**Framework**: MetalKit  
**Kind**: property

The device object that the system recommends using for this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredDevice: (any MTLDevice)? { get }
```

#### Discussion

On systems with a single GPU, this method returns the default Metal system device; see [`MTLCreateSystemDefaultDevice()`](https://developer.apple.com/documentation/Metal/MTLCreateSystemDefaultDevice()). On systems with more than one GPU, this method returns the [`MTLDevice`](https://developer.apple.com/documentation/Metal/MTLDevice) that was last used to composite and present the view’s contents. This device object usually corresponds to the GPU associated with the screen that’s displaying the view. If you set the view’s [`device`](mtkview/device.md) property to this device object, you reduce the number of cross-GPU texture copies that Core Animation must make to present the view’s contents onscreen.

## See Also

- [var device: (any MTLDevice)?](mtkview/device.md)
  The device object the view uses to create its Metal objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/preferreddevice)*