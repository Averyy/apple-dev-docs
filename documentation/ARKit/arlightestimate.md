# ARLightEstimate

**Framework**: ARKit  
**Kind**: class

Estimated scene lighting information associated with a captured video frame in an AR session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARLightEstimate
```

#### Overview

If you enable the [`isLightEstimationEnabled`](arconfiguration/islightestimationenabled.md) setting, ARKit provides light estimates in the [`lightEstimate`](arframe/lightestimate.md) property of each [`ARFrame`](arframe.md) it delivers.

If you render your own overlay graphics for the AR scene, you can use this information in shading algorithms to help make those graphics match the real-world lighting conditions of the scene captured by the camera. The [`ARSCNView`](arscnview.md) class automatically uses this information to configure SceneKit lighting.

## Topics

### Examining Light Parameters
- [var ambientIntensity: CGFloat](arlightestimate/ambientintensity.md)
  The estimated intensity, in lumens, of ambient light throughout the scene.
- [var ambientColorTemperature: CGFloat](arlightestimate/ambientcolortemperature.md)
  The estimated color temperature, in degrees Kelvin, of ambient light throughout the scene.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [ARDirectionalLightEstimate](ardirectionallightestimate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Adding realistic reflections to an AR experience](adding-realistic-reflections-to-an-ar-experience.md)
  Use ARKit to generate environment probe textures from camera imagery and render reflective virtual objects.
- [class AREnvironmentProbeAnchor](arenvironmentprobeanchor.md)
  An object that provides environmental lighting information for a specific area of space in a world-tracking AR session.
- [class ARDirectionalLightEstimate](ardirectionallightestimate.md)
  Estimated environmental lighting information associated with a captured video frame in a face-tracking AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arlightestimate)*