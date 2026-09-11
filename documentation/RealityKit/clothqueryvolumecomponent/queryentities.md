# queryEntities

**Framework**: RealityKit  
**Kind**: property

The entities to query for intersections with the volume.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var queryEntities: [Entity]
```

#### Discussion

Only entities with a [`ClothBodyComponent`](clothbodycomponent.md) are included in the query; others are ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothqueryvolumecomponent/queryentities)*