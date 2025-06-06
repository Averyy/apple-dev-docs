# CollisionGroup

**Framework**: RealityKit  
**Kind**: struct

A bitmask used to define the collision group to which an entity belongs.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
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
- [init()](collisiongroup/init.md)
  Creates an empty option set.
- [init(rawValue: UInt32)](collisiongroup/init(rawvalue:).md)
  Creates a collision group from a raw value.
- [init<S>(S)](collisiongroup/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](collisiongroup/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
### Option set
- [let rawValue: UInt32](collisiongroup/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [static func != (Self, Self) -> Bool](collisiongroup/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [CollisionGroup.Element](collisiongroup/element.md)
  The element type of the option set.
- [var isEmpty: Bool](collisiongroup/isempty.md)
  A Boolean value that indicates whether the set has no elements.
- [let rawValue: UInt32](collisiongroup/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [func contains(Self) -> Bool](collisiongroup/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
- [func formIntersection(Self)](collisiongroup/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func formSymmetricDifference(Self)](collisiongroup/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
- [func formUnion(Self)](collisiongroup/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](collisiongroup/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func intersection(Self) -> Self](collisiongroup/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func isDisjoint(with: Self) -> Bool](collisiongroup/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [func isStrictSubset(of: Self) -> Bool](collisiongroup/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](collisiongroup/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSubset(of: Self) -> Bool](collisiongroup/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isSuperset(of: Self) -> Bool](collisiongroup/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func remove(Self.Element) -> Self.Element?](collisiongroup/remove(_:).md)
  Removes the given element and all elements subsumed by it.
- [func subtract(Self)](collisiongroup/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](collisiongroup/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.
- [func symmetricDifference(Self) -> Self](collisiongroup/symmetricdifference(_:).md)
  Returns a new option set with the elements contained in this set or in the given set, but not in both.
- [func union(Self) -> Self](collisiongroup/union(_:).md)
  Returns a new option set of the elements contained in this set, in the given set, or in both.
- [func update(with: Self.Element) -> Self.Element?](collisiongroup/update(with:).md)
  Inserts the given element into the set.
- [CollisionGroup.ArrayLiteralElement](collisiongroup/arrayliteralelement.md)
  The type of the elements of an array literal.
- [CollisionGroup.RawValue](collisiongroup/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](collisiongroup/equatable-implementations.md)
- [OptionSet Implementations](collisiongroup/optionset-implementations.md)
- [SetAlgebra Implementations](collisiongroup/setalgebra-implementations.md)

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