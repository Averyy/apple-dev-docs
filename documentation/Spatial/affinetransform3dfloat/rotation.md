# rotation

**Framework**: Spatial  
**Kind**: property

The affine transform’s rotation.

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

This function can’t extract rotation from a non-scale-rotate-translate affine transform. In that case, the function returns `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3dfloat/rotation)*