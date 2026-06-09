# lightingBlendDistance

**Framework**: RealityKit  
**Kind**: property

The lighting blend distance from the clipping/crossing plane.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 18.0+
- macOS 27.0+ (Beta)
- tvOS 26.0+
- visionOS 27.0+ (Beta)

## Declaration

```swift
var lightingBlendDistance: Float { get set }
```

#### Discussion

This property controls the smooth blending between outside world environment probe lighting and portal world environment probe lighting for crossing entities. The blend is calculated based on fragment distance to the portal surface as defined by the crossing modes.

**Behavior:**

- **Value 0**: Sharp lighting transition at portal boundary
- **Positive values**: Smooth gradient over the specified distance in meters
- **Distance calculation**: Uses the SDF (Signed Distance Field) from crossing geometry - Plane mode: Distance to plane or cylindrical surface
- Volume mode: Distance to box boundary

> **Note**: Only functional when crossing mode is enabled and target world uses blend lighting mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/lightingblenddistance)*