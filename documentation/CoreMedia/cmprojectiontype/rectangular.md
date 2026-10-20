# CMProjectionType.rectangular

**Framework**: Core Media  
**Kind**: case  
**Role**: Case

Video content displays on a flat, rectangular 2D surface.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
case rectangular
```

```c
kCMProjectionType_Rectangular
```

#### Discussion

Rectangular projection is equivalent to displaying as a 2D texture in the world.

Rectangular projection is the default for 3D video when a channel or buffer has no projection metadata.

## See Also

### Projection Surfaces
- [CMProjectionType.equirectangular](./equirectangular.md)
  Video content displays as a 360 degree equirectangular projection.
- [CMProjectionType.halfEquirectangular](./halfequirectangular.md)
  Video content displays as a 180 degree equirectangular projection.
- [CMProjectionType.fisheye](./fisheye.md)
  Video content displays as a fisheye projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmprojectiontype/rectangular)*