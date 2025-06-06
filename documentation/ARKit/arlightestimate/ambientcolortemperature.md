# ambientColorTemperature

**Framework**: ARKit  
**Kind**: property

The estimated color temperature, in degrees Kelvin, of ambient light throughout the scene.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var ambientColorTemperature: CGFloat { get }
```

#### Discussion

This value is based on the internal white balance compensation of the camera device, and scaled to be appropriate for use in rendering architectures that use realistic lighting metrics. A value of 6500 represents neutral (pure white) lighting; lower values indicate a “warmer” yellow or orange tint, and higher values indicate a “cooler” blue tint.

For example, you can pass this value directly to the [`temperature`](https://developer.apple.com/documentation/SceneKit/SCNLight/temperature) property of a SceneKit ambient light for lighting results that roughly match those of the real-world scene captured by the device camera. (However, passing this value to SceneKit is generally not necessary; the [`ARSCNView`](arscnview.md) class automatically sets SceneKit lighting based on this value.)

## See Also

- [var ambientIntensity: CGFloat](arlightestimate/ambientintensity.md)
  The estimated intensity, in lumens, of ambient light throughout the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arlightestimate/ambientcolortemperature)*