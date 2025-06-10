# unapply(_:)

**Framework**: Spatial  
**Kind**: method  
**Required**: Yes

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
mutating func unapply(_ transform: Self.AffineTransform)
```

#### Discussion

> **Note**: The transform must be rectilinear otherwise this function returns `self`.

## Parameters

- `transform`: The affine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/primitive3dprotocol/unapply(_:)-34afa)*