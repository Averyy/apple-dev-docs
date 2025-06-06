# Entity.CoordinateSpaceReference.immersiveSpace

**Framework**: Realitykit  
**Kind**: case

A reference to an opened immersive space.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
case immersiveSpace
```

#### Discussion

You can use this enum case to get an entity’s relative transform to the immersive space:

```swift
let transformInImmersiveSpace = entity.transformMatrix(relativeTo: .immersiveSpace)
```

> **Note**: If no immersive space is open, calling [`transformMatrix(relativeTo:)`](entity/transformmatrix(relativeto:).md) with the case `immersiveSpace` returns `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/coordinatespacereference/immersivespace)*