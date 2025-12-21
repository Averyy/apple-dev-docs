# unapplying(_:)

**Framework**: Spatial  
**Kind**: method

Returns a ray that’s transformed by the inverse of the specified affine transform.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func unapplying(_ transform: AffineTransform3DFloat) -> Ray3DFloat
```

#### Discussion

- Returns The transformed ray.

This function applies the transform to the ray’s origin and direction.

## Parameters

- `transform`: The affine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3dfloat/unapplying(_:)-9mbz3)*