# applying(_:)

**Framework**: Spatial  
**Kind**: method

Returns a ray that’s transformed by the specified affine transform.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func applying(_ transform: AffineTransform3DFloat) -> Ray3DFloat
```

#### Discussion

- Returns The transformed ray.

This function applies the transform to the ray’s origin and direction.

## Parameters

- `transform`: The affine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3dfloat/applying(_:)-7miic)*