# inverse

**Framework**: Spatial  
**Kind**: property

The projective transform’s inverse.

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
var inverse: ProjectiveTransform3DFloat? { get }
```

#### Discussion

If the source transform isn’t invertible, this value is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3dfloat/inverse)*