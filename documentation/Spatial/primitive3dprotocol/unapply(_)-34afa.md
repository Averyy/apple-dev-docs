# unapply(_:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Unapplies an affine transform.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
mutating func unapply(_ transform: Self.AffineTransform)
```

## Discussion

> **Note**: The transform must be rectilinear otherwise this function returns `self`.

## Parameters

- `transform`: The affine transform.

## Default Implementations

### Primitive3DProtocol Implementations
- [func unapply(Self.Pose)](./unapply%28_%29-2vz7p.md)
  Unapplies a pose.
- [func unapply(Self.AffineTransform)](./unapply%28_%29-2wwwi.md)
  Unapplies an affine transform.
- [func unapply(Self.ProjectiveTransform)](./unapply%28_%29-4ip05.md)
  Unapplies a projective transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/primitive3dprotocol/unapply(_:)-34afa)*