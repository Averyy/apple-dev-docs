# preferredDevice

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

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
var preferredDevice: (any MTLDevice)? { get }
```

```objc
@property (readonly, nullable) id<MTLDevice> preferredDevice;
```

## Discussion

On systems with a single GPU, this method returns the default Metal system device; see [`MTLCreateSystemDefaultDevice()`](../../Metal/mtlcreatesystemdefaultdevice%28%29.md). On systems with more than one GPU, this method returns the [`MTLDevice`](../../Metal/mtldevice.md) that was last used to composite and present the view’s contents. This device object usually corresponds to the GPU associated with the screen that’s displaying the view. If you set the view’s [`device`](./device.md) property to this device object, you reduce the number of cross-GPU texture copies that Core Animation must make to present the view’s contents onscreen.

## See Also

### Configuring the Metal Device
- [var device: (any MTLDevice)?](./device.md)
  The device object the view uses to create its Metal objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/preferreddevice)*