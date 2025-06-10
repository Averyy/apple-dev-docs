# unapplying(_:)

**Framework**: Spatial  
**Kind**: method

Unapplies an affine transform.

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
func unapplying(_ transform: AffineTransform3DFloat) -> Size3DFloat
```

#### Discussion

> **Note**: The transform must be rectilinear otherwise this function returns `self`.

## Parameters

- `transform`: The affine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/size3dfloat/unapplying(_:)-2tlsj)*