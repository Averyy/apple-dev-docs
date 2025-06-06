# preferredDevice

**Framework**: Core Animation  
**Kind**: property

The device object that the system recommends using for this layer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var preferredDevice: (any MTLDevice)? { get }
```

#### Discussion

On systems with a single GPU, this method returns the default device object; see [`MTLCreateSystemDefaultDevice()`](https://developer.apple.com/documentation/Metal/MTLCreateSystemDefaultDevice()). On systems with more than one GPU, this method returns the [`MTLDevice`](https://developer.apple.com/documentation/Metal/MTLDevice) that was last used to composite and present the [`CAMetalLayer`](cametallayer.md). This device object usually corresponds to the GPU associated with the screen that’s displaying the layer. If you set the layer’s [`device`](cametallayer/device.md) property to this device object, you reduce the number of cross-GPU texture copies that Core Animation must perform to present the layer’s contents onscreen.

## See Also

- [var device: (any MTLDevice)?](cametallayer/device.md)
  The Metal device responsible for the layer’s drawable resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametallayer/preferreddevice)*