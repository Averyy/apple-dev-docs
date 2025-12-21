# changeBasis(from:to:)

**Framework**: Spatial  
**Kind**: method

Returns a new affine transform structure by applying a change-of-basis.

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
func changeBasis(from: AffineTransform3DFloat = .identity, to: AffineTransform3DFloat) -> AffineTransform3DFloat?
```

#### Return Value

A new affine transform structure.

## Parameters

- `from`: The old basis.
- `to`: The new basis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3dfloat/changebasis(from:to:))*