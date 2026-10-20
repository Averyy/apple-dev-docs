# *(_:_:)

**Framework**: Spatial  
**Kind**: op  
**Role**: Operator

Returns the concatenation of two projective transforms.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
static func * (lhs: ProjectiveTransform3D, rhs: ProjectiveTransform3D) -> ProjectiveTransform3D
```

## Parameters

- `lhs`: The left-hand-side value.
- `rhs`: The right-hand-side value.

## See Also

### Applying arithmetic operations
- [static func *= (inout ProjectiveTransform3D, ProjectiveTransform3D)](./stareq%28_,_%29.md)
  Concatenates two projective transforms and stores the result in the left-hand-side variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/*(_:_:))*