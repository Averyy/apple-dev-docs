# unapply(_:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Unapplies a projective transform.

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
mutating func unapply(_ transform: Self.ProjectiveTransform)
```

Available when `Scalar` is `Float`.

#### Discussion

> **Note**: When unapplying transforms on rectangle structures, the transform must be rectilinear, otherwise this function has no effect.

## Parameters

- `transform`: The projective transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/primitive3dprotocol/unapply(_:)-4ip05)*