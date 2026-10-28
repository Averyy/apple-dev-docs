# unapply(_:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

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

Available when `Scalar` is `Float`.

## Discussion

> **Note**: The transform must be rectilinear otherwise this function returns `self`.

## Parameters

- `transform`: The affine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/primitive3dprotocol/unapply(_:)-2wwwi)*