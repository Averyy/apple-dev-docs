# default

**Framework**: RealityKit  
**Kind**: property

The default collision filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
static let `default`: CollisionFilter
```

#### Discussion

Entities with a [`default`](collisionfilter/default.md) collision filter have a [`group`](collisionfilter/group.md) of [`default`](collisiongroup/default.md) and a [`mask`](collisionfilter/mask.md) of [`all`](collisiongroup/all.md).

## See Also

- [init(group: CollisionGroup, mask: CollisionGroup)](collisionfilter/init(group:mask:).md)
  Creates a collision filter.
- [static let sensor: CollisionFilter](collisionfilter/sensor.md)
  A collision filter for an entity that collides with everything.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisionfilter/default)*