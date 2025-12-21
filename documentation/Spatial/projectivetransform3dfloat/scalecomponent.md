# scaleComponent

**Framework**: Spatial  
**Kind**: property

The projective transform’s scale component.

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
var scaleComponent: Size3DFloat { get }
```

#### Discussion

This function computes the scale from the first three rows of the transform matrix and ignores the fourth row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3dfloat/scalecomponent)*