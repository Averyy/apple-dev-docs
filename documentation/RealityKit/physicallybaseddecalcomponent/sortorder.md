# sortOrder

**Framework**: RealityKit  
**Kind**: property

The sort layer for the decal. Higher layers show up on top of lower layers.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var sortOrder: Int32
```

## See Also

- [var layers: RenderLayer.Set](physicallybaseddecalcomponent/layers.md)
  The layers this decal affects. Only entities whose [`layers`](renderlayercomponent/layers.md) intersect with these layers will be affected.
- [var receiverEntities: Set<Entity>](physicallybaseddecalcomponent/receiverentities.md)
  An optional set of receiver entities that are not part of any layers. The limit on the number of receiver entities is 8, extra entities are ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybaseddecalcomponent/sortorder)*