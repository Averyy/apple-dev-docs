# unapplying(_:)

**Framework**: Spatial  
**Kind**: method

Unapplies an affine transform.

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
func unapplying(_ transform: AffineTransform3DFloat) -> Rect3DFloat
```

#### Discussion

> **Note**: The transform must be rectilinear otherwise this function returns `self`.

## Parameters

- `transform`: The affine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3dfloat/unapplying(_:)-32dls)*