# ARDirectionalLightEstimate

**Framework**: ARKit  
**Kind**: class

Estimated environmental lighting information associated with a captured video frame in a face-tracking AR session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARDirectionalLightEstimate
```

#### Overview

When you run a face tracking AR session (see [`ARFaceTrackingConfiguration`](arfacetrackingconfiguration.md)) with the [`isLightEstimationEnabled`](arconfiguration/islightestimationenabled.md) property set to [`true`](https://developer.apple.com/documentation/swift/true), ARKit uses the detected face as a light probe to estimate the directional lighting environment in the scene. The [`lightEstimate`](arframe/lightestimate.md) property of each frame vended by the session contains an [`ARDirectionalLightEstimate`](ardirectionallightestimate.md) instance containing this information.

If you render your own overlay graphics for the AR scene, you can use this information in shading algorithms to help make those graphics match the real-world lighting conditions of the scene captured by the camera. (The [`ARSCNView`](arscnview.md) class automatically uses this information to configure SceneKit lighting.)

## Topics

### Examining Light Parameters
- [var sphericalHarmonicsCoefficients: Data](ardirectionallightestimate/sphericalharmonicscoefficients.md)
  Data describing the estimated lighting environment in all directions.
- [var primaryLightDirection: simd_float3](ardirectionallightestimate/primarylightdirection.md)
  A vector indicating the orientation of the strongest directional light source in the scene.
- [var primaryLightIntensity: CGFloat](ardirectionallightestimate/primarylightintensity.md)
  The estimated intensity, in lumens, of the strongest directional light source in the scene.

## Relationships

### Inherits From
- [ARLightEstimate](arlightestimate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Adding realistic reflections to an AR experience](adding-realistic-reflections-to-an-ar-experience.md)
  Use ARKit to generate environment probe textures from camera imagery and render reflective virtual objects.
- [class AREnvironmentProbeAnchor](arenvironmentprobeanchor.md)
  An object that provides environmental lighting information for a specific area of space in a world-tracking AR session.
- [class ARLightEstimate](arlightestimate.md)
  Estimated scene lighting information associated with a captured video frame in an AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ardirectionallightestimate)*