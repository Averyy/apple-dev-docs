# unapplying(_:)

**Framework**: Spatial  
**Kind**: method

Unapplies a projective transform.

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
func unapplying(_ transform: ProjectiveTransform3DFloat) -> Rect3DFloat
```

#### Discussion

> **Note**: The transform must be rectilinear otherwise this function returns `self`.

## Parameters

- `transform`: The projective transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3dfloat/unapplying(_:)-31d5i)*