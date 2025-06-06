# MDLLightType.discArea

**Framework**: Model I/O  
**Kind**: case

The light source illuminates a scene in all directions from an area in the shape of a disc.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case discArea
```

#### Discussion

This light type is exclusive to the [`MDLAreaLight`](mdlarealight.md) class.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdllighttype/discarea)*