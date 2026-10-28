# kCMTagProjectionTypeEquirectangular

**Framework**: Core Media  
**Kind**: var  
**Role**: Global Variable

A value for projection tags indicating that display is on a 360 degree equirectangular projection.

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
extern const CMTag kCMTagProjectionTypeEquirectangular;
```

## Discussion

This value is for use in tags with the [`kCMTagCategory_ProjectionType`](./cmtagcategory/kcmtagcategory_projectiontype.md) category. The video frames map onto the interior of a 3D sphere projection.

## See Also

### Projection Surfaces
- [kCMTagProjectionTypeRectangular](./kcmtagprojectiontyperectangular.md)
  A value for projection tags indicating that display is on a flat rectangular surface.
- [kCMTagProjectionTypeFisheye](./kcmtagprojectiontypefisheye.md)
  Video content displays as a fisheye projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmtagprojectiontypeequirectangular)*