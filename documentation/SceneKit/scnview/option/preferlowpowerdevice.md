# preferLowPowerDevice

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

An option for whether to select low-power-usage devices for Metal rendering.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
static let preferLowPowerDevice: SCNView.Option
```

```c
extern SCNViewOption const SCNPreferLowPowerDeviceKey;
```

#### Discussion

The value for this key is an [`NSNumber`](../../../Foundation/nsnumber.md) object containing a Boolean value.

SceneKit uses this option when automatically selecting a Metal device on systems with multiple GPUs. If the value is [`true`](../../../Swift/true.md), SceneKit uses a device with low power usage requirements—for example, the integrated GPU on a MacBook Pro with both integrated and discrete graphics hardware.

Leaving this key unspecified is equivalent to setting its value to [`false`](../../../Swift/false.md). In this case, SceneKit chooses the most capable available Metal device.

## See Also

### View Options
- [static let preferredDevice: SCNView.Option](./preferreddevice.md)
  The device to use for Metal rendering.
- [static let preferredRenderingAPI: SCNView.Option](./preferredrenderingapi.md)
  The rendering API to use for rendering the view (for example, Metal or OpenGL).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/option/preferlowpowerdevice)*