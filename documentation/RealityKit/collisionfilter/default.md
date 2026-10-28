# default

**Framework**: RealityKit  
**Kind**: property  
**Role**: Type Property

The default collision filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
static let `default`: CollisionFilter
```

## Discussion

Entities with a [`default`](./default.md) collision filter have a [`group`](./group.md) of [`default`](../collisiongroup/default.md) and a [`mask`](./mask.md) of [`all`](../collisiongroup/all.md).

## See Also

### Creating a collision filter
- [init(group: CollisionGroup, mask: CollisionGroup)](./init%28group,mask%29.md)
  Creates a collision filter.
- [static let sensor: CollisionFilter](./sensor.md)
  A collision filter for an entity that collides with everything.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisionfilter/default)*