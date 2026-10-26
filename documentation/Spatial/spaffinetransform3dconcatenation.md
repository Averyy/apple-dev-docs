# SPAffineTransform3DConcatenation

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```c
static SPAffineTransform3D SPAffineTransform3DConcatenation(SPAffineTransform3D t1, SPAffineTransform3D t2);
```

#### Return Value

An affine transformation matrix that’s constructed by concatenating two existing affine transforms.

#### Discussion

Returns an affine transformation matrix that’s constructed by concatenating two existing affine transforms.

## Parameters

- `t1`: The first transform.
- `t2`: The second transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spaffinetransform3dconcatenation)*