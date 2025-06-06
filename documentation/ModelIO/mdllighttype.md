# MDLLightType

**Framework**: Model I/O  
**Kind**: enum

Options for the shape and style of illumination provided by a light, used by the [`lightType`](mdllight/lighttype.md) property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum MDLLightType
```

## Topics

### Constants
- [MDLLightType.unknown](mdllighttype/unknown.md)
  The type of the light is unknown or has not been initialized.
- [MDLLightType.ambient](mdllighttype/ambient.md)
  The light source should illuminate a scene evenly regardless of position or direction.
- [MDLLightType.directional](mdllighttype/directional.md)
  The light source illuminates a scene from a uniform direction regardless of its position.
- [MDLLightType.spot](mdllighttype/spot.md)
  The light source illuminates a scene from a specific position and direction.
- [MDLLightType.point](mdllighttype/point.md)
  The light source illuminates a scene in all directions from a specific position.
- [MDLLightType.linear](mdllighttype/linear.md)
  The light source illuminates a scene in all directions from an area in the shape of a line.
- [MDLLightType.discArea](mdllighttype/discarea.md)
  The light source illuminates a scene in all directions from an area in the shape of a disc.
- [MDLLightType.rectangularArea](mdllighttype/rectangulararea.md)
  The light source illuminates a scene in all directions from an area in the shape of a rectangle.
- [MDLLightType.superElliptical](mdllighttype/superelliptical.md)
  The light source illuminates a scene in all directions from an area in the shape of a superellipse.
- [MDLLightType.photometric](mdllighttype/photometric.md)
  The illumination from the light is determined by a photometric profile.
- [MDLLightType.probe](mdllighttype/probe.md)
  The illumination from the light is determined by texture images representing a sample of a scene at a specific point.
- [MDLLightType.environment](mdllighttype/environment.md)
  The illumination from the light is determined by texture images representing a sample of the surrounding environment for a scene.
### Initializers
- [init?(rawValue: UInt)](mdllighttype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdllighttype)*