# inverse

**Framework**: Spatial  
**Kind**: property

The projective transform’s inverse.

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
var inverse: ProjectiveTransform3DFloat? { get }
```

#### Discussion

If the source transform isn’t invertible, this value is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3dfloat/inverse)*