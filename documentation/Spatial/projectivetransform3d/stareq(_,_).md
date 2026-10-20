# *=(_:_:)

**Framework**: Spatial  
**Kind**: op  
**Role**: Operator

Concatenates two projective transforms and stores the result in the left-hand-side variable.

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
static func *= (lhs: inout ProjectiveTransform3D, rhs: ProjectiveTransform3D)
```

## Parameters

- `lhs`: The left-hand-side value.
- `rhs`: The right-hand-side value.

## See Also

### Applying arithmetic operations
- [static func * (ProjectiveTransform3D, ProjectiveTransform3D) -> ProjectiveTransform3D](./star%28_,_%29.md)
  Returns the concatenation of two projective transforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/*=(_:_:))*