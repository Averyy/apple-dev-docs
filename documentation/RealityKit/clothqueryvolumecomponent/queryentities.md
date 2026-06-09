# queryEntities

**Framework**: RealityKit  
**Kind**: property

The entities to query for intersections with the volume.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var queryEntities: [Entity]
```

#### Discussion

Only entities with a [`ClothBodyComponent`](clothbodycomponent.md) are included in the query; others are ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothqueryvolumecomponent/queryentities)*