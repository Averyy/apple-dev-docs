# CollisionGroup

**Framework**: RealityKit  
**Kind**: struct

A bitmask used to define the collision group to which an entity belongs.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct CollisionGroup
```

#### Overview

Use collision groups along with [`CollisionFilter`](collisionfilter.md) to define custom collision properties for entities in your scene and to control which entities collide with which others. By default, all entities that participate in the physics simulation collide with all other participating entities. There are times, however, when you need certain entities to not collide with certain other entities, and that’s where collision groups and filters come into play.

Create individual collision groups using raw bit flag values, like this:

```swift
let redGroup = CollisionGroup(rawValue: 1 << 0)
let blueGroup = CollisionGroup(rawValue: 1 << 1)
let greenGroup = CollisionGroup(rawValue: 1 << 2)
let yellowGroup = CollisionGroup(rawValue: 1 << 3)
```

Because [`CollisionGroup`](collisiongroup.md) conforms to [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet), this allows you to create aggregate groups that encompass multiple individual collision groups, like so:

```swift
let blueAndRedGroup = redGroup.union(blueGroup)
let greenAndYellowGroup = greenGroup.union(yellowGroup)
```

You can also define groups that have all entities except those in specific groups. In a game, for example, you might want to turn off collisions between members of the same team or between pieces owned by the same player. This is what creating that kind of filter would look like:

```swift
let allButRedGroup = CollisionGroup.all.subtracting(redGroup)
```

Collision groups aren’t assigned directly to entities. Instead, you create a [`CollisionFilter`](collisionfilter.md) for the group, and then assign that filter to all the entities you wish to include in its group. The collision filter’s mask defines which objects the entities in this group collide with, and all entities that share the same filter are part of the same collision group.

```swift
let allButRedFilter = CollisionFilter(group: redGroup, mask: allButRedGroup)
redTeamPlayer1.collision?.filter = allButRedFilter
```

## Topics

### Standard collision groups
- [static let `default`: CollisionGroup](collisiongroup/default.md)
  The default collision group for objects.
- [static let all: CollisionGroup](collisiongroup/all.md)
  The collision group that represents all groups.
- [static let sceneUnderstanding: CollisionGroup](collisiongroup/sceneunderstanding.md)
  The default collision group for scene-understanding meshes.
### Creating a collision group
- [init(rawValue: UInt32)](collisiongroup/init(rawvalue:).md)
  Creates a collision group from a raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Simulating physics with collisions in your visionOS app](simulating-physics-with-collisions-in-your-visionos-app.md)
  Create entities that behave and react like physical objects in a RealityKit view.
- [Configuring Collision in RealityKit](configuring-collision-in-realitykit.md)
  Use collision groups and collision filters to control which objects collide.
- [struct CollisionComponent](collisioncomponent.md)
  A component that gives an entity the ability to collide with other entities that also have collision components.
- [CollisionComponent.Mode](collisioncomponent/mode-swift.enum.md)
  A mode that dictates how much collision data is collected for a given entity.
- [class ShapeResource](shaperesource.md)
  A representation of a shape.
- [enum ShapeResourceError](shaperesourceerror.md)
- [struct CollisionFilter](collisionfilter.md)
  A set of masks that determine whether entities can collide during simulations.
- [class TriggerVolume](triggervolume.md)
  An invisible 3D shape that detects when objects enter or exit a given region of space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisiongroup)*