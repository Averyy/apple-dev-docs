# applying(_:)

**Framework**: Spatial  
**Kind**: method

Returns a ray that’s transformed by the specified projective transform.

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
func applying(_ transform: ProjectiveTransform3DFloat) -> Ray3DFloat
```

#### Discussion

- Returns The transformed ray.

This function applies the transform to the ray’s origin and direction.

## Parameters

- `transform`: The projective transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3dfloat/applying(_:)-6phxw)*