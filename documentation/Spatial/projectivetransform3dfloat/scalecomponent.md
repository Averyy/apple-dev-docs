# scaleComponent

**Framework**: Spatial  
**Kind**: property

The projective transform’s scale component.

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
var scaleComponent: Size3DFloat { get }
```

#### Discussion

This function computes the scale from the first three rows of the transform matrix and ignores the fourth row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3dfloat/scalecomponent)*