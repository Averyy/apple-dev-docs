# unapply(_:)

**Framework**: Spatial  
**Kind**: method  
**Required**: Yes

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
mutating func unapply(_ transform: Self.AffineTransform)
```

#### Discussion

> **Note**: The transform must be rectilinear otherwise this function returns `self`.

## Parameters

- `transform`: The affine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/primitive3dprotocol/unapply(_:)-34afa)*