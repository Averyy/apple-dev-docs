# init(group:mask:)

**Framework**: RealityKit  
**Kind**: init

Creates a collision filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
init(group: CollisionGroup, mask: CollisionGroup)
```

#### Discussion

Collision filters are created for the collision group specified in the `group` parameter. The `mask` parameter defines which objects will collide with the objects that use this filter. Because [`CollisionGroup`](collisiongroup.md) conforms to [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet), you can specify any combination of collision groups in the `mask` parameter by using the various [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet) methods like `CollisionGroup/union(_:)`, `CollisionGroup/subtracting(_:)`, and `CollisionGroup/intersection(_:)`. Entities from any group contained in `mask` will collide with entities using this filter, while those not contained by `mask` will not.

To combine multiple groups into a filter, use the `CollisionGroup/union(_:)` method, like this:

```swift
let groupA = CollisionGroup(rawValue: 1 << 0)
let groupB = CollisionGroup(rawValue: 1 << 1)
let groupC = CollisionGroup(rawValue: 1 << 2)

// Create a filter that collides with A and C, but not B
let theFilter = CollisionFilter(group: groupA, mask: groupA.union(groupB))
```

A common use case is to want entities to collide with everything except one group, or a few groups. In a game, for example, you might not want a player’s pieces to collide with their own pieces, or you might not want players on the same team to collide with each other. You can accomplish that by starting with the [`all`](collisiongroup/all.md) property, subtracting the group or groups that you don’t want the entities using this filter to collide with, like this:

```swift
// Create a filter that collides with everything except B
let notGroupB = CollisionGroup.all.subtracting(groupB)
```

## Parameters

- `group`: The collision group identifier.
- `mask`: The collision mask defines what objects will collide with   objects using this filter.

## See Also

- [static let `default`: CollisionFilter](collisionfilter/default.md)
  The default collision filter.
- [static let sensor: CollisionFilter](collisionfilter/sensor.md)
  A collision filter for an entity that collides with everything.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisionfilter/init(group:mask:))*