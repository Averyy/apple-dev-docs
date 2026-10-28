# kCMTagProjectionTypeRectangular

**Framework**: Core Media  
**Kind**: var  
**Role**: Global Variable

A value for projection tags indicating that display is on a flat rectangular surface.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```c
extern const CMTag kCMTagProjectionTypeRectangular;
```

## Discussion

This value is for use in tags with the [`kCMTagCategory_ProjectionType`](./cmtagcategory/kcmtagcategory_projectiontype.md) category. Rectangular projection is equivalent to displaying as a 2D texture in the world.

Rectangular projection is the default for 3D video when a channel or buffer has no projection metadata.

## See Also

### Projection Surfaces
- [kCMTagProjectionTypeEquirectangular](./kcmtagprojectiontypeequirectangular.md)
  A value for projection tags indicating that display is on a 360 degree equirectangular projection.
- [kCMTagProjectionTypeFisheye](./kcmtagprojectiontypefisheye.md)
  Video content displays as a fisheye projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmtagprojectiontyperectangular)*