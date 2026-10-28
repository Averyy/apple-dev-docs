# MDLLightType.discArea

**Framework**: Model I/O  
**Kind**: case  
**Role**: Case

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

```c
MDLLightTypeDiscArea
```

## Discussion

This light type is exclusive to the [`MDLAreaLight`](../mdlarealight.md) class.

## See Also

### Constants
- [MDLLightType.unknown](./unknown.md)
  The type of the light is unknown or has not been initialized.
- [MDLLightType.ambient](./ambient.md)
  The light source should illuminate a scene evenly regardless of position or direction.
- [MDLLightType.directional](./directional.md)
  The light source illuminates a scene from a uniform direction regardless of its position.
- [MDLLightType.spot](./spot.md)
  The light source illuminates a scene from a specific position and direction.
- [MDLLightType.point](./point.md)
  The light source illuminates a scene in all directions from a specific position.
- [MDLLightType.linear](./linear.md)
  The light source illuminates a scene in all directions from an area in the shape of a line.
- [MDLLightType.rectangularArea](./rectangulararea.md)
  The light source illuminates a scene in all directions from an area in the shape of a rectangle.
- [MDLLightType.superElliptical](./superelliptical.md)
  The light source illuminates a scene in all directions from an area in the shape of a superellipse.
- [MDLLightType.photometric](./photometric.md)
  The illumination from the light is determined by a photometric profile.
- [MDLLightType.probe](./probe.md)
  The illumination from the light is determined by texture images representing a sample of a scene at a specific point.
- [MDLLightType.environment](./environment.md)
  The illumination from the light is determined by texture images representing a sample of the surrounding environment for a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdllighttype/discarea)*