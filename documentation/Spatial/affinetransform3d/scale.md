# scale

**Framework**: Spatial  
**Kind**: property  
**Role**: Instance Property

The affine transform’s scale.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var scale: Size3D { get }
```

```c
static SPSize3D SPAffineTransform3DGetScale(SPAffineTransform3D transform);
```

## See Also

### Decomposing a 3D affine transform
- [var rotation: Rotation3D?](./rotation.md)
  The affine transform’s rotation.
- [var translation: Vector3D](./translation.md)
  The translation component of the affine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3d/scale)*