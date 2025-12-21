# rotation

**Framework**: Spatial  
**Kind**: property

The projective transform’s rotation.

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
var rotation: Rotation3DFloat? { get }
```

#### Discussion

This function computes the rotation from the first three rows of the transform matrix and ignores the fourth row. This function can’t extract rotation from a non-scale-rotate-translate projective transform. In that case, the function returns `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3dfloat/rotation)*