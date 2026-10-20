# preferredDevice

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

The device to use for Metal rendering.

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
static let preferredDevice: SCNView.Option
```

```c
extern SCNViewOption const SCNPreferredDeviceKey;
```

#### Discussion

The value for this key is a [`MTLDevice`](../../../Metal/mtldevice.md) object.

Use this key to choose a specific device for rendering (for example, on a macOS system with multiple GPUs), or leave it unspecified to allow SceneKit to automatically choose a device.

## See Also

### View Options
- [static let preferLowPowerDevice: SCNView.Option](./preferlowpowerdevice.md)
  An option for whether to select low-power-usage devices for Metal rendering.
- [static let preferredRenderingAPI: SCNView.Option](./preferredrenderingapi.md)
  The rendering API to use for rendering the view (for example, Metal or OpenGL).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/option/preferreddevice)*