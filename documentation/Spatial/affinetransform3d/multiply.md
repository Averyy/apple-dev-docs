# *(_:_:)

**Framework**: Spatial  
**Kind**: op

Returns the concatenation of two affine transforms.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
static func * (lhs: AffineTransform3D, rhs: AffineTransform3D) -> AffineTransform3D
```

## Parameters

- `lhs`: The left-hand-side value.
- `rhs`: The right-hand-side value.

## See Also

- [static func *= (inout AffineTransform3D, AffineTransform3D)](affinetransform3d/*=(_:_:).md)
  Concatenates two affine transforms and stores the result in the left-hand-side variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3d/*(_:_:))*