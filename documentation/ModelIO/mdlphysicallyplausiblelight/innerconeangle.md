# innerConeAngle

**Framework**: Model I/O  
**Kind**: property

The radial angle, in degrees, of the area fully illuminated by the light.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var innerConeAngle: Float { get set }
```

#### Discussion

This property measures the angle from the light axis (the direction in which the light points; the negative z-axis of its local coordinate space) to the edge of the light’s effect. For example, a cone angle of 22.5 degrees (the default) creates a broad spot light. (The light’s [`lightType`](mdllight/lighttype.md) value is [`MDLLightType.spot`](mdllighttype/spot.md).) An angle of 90 degrees divides space evenly, illuminating in all directions in front of the light and none behind, and an angle of 180 degrees illuminates in all directions (creating a light whose type is [`MDLLightType.point`](mdllighttype/point.md)).

## See Also

- [var outerConeAngle: Float](mdlphysicallyplausiblelight/outerconeangle.md)
  The radial angle, in degrees, at which the illumination from a spotlight becomes zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlphysicallyplausiblelight/innerconeangle)*