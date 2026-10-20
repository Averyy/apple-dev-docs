# EntityGeometricPins

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A structure that wraps all geometric pins an entity owns.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
struct EntityGeometricPins
```

#### Overview

Access an instance of this structure through the entity property [`pins`](./entity/pins.md).

## Topics

### Structures
- [EntityGeometricPins.Iterator](./entitygeometricpins/iterator.md)
  An object to iterate over all geometric pins in the collection.
### Instance Properties
- [var count: Int](./entitygeometricpins/count.md)
  The total number of pins.
- [let entity: Entity](./entitygeometricpins/entity.md)
  The entity where the local frame lives.
- [var isEmpty: Bool](./entitygeometricpins/isempty.md)
  A Boolean value indicating whether the collection is empty.
### Instance Methods
- [func makeIterator() -> EntityGeometricPins.Iterator](./entitygeometricpins/makeiterator%28%29.md)
  Returns an iterator for the sequence.
- [func remove(named: String)](./entitygeometricpins/remove%28named%29.md)
  Removes a geometric pin with the given name from this entity.
- [func set(named: String, position: SIMD3<Float>, orientation: simd_quatf) -> GeometricPin](./entitygeometricpins/set%28named,position,orientation%29.md)
  Creates and adds a geometric pin to the entity, and returns the entity geometric pin.
- [func set(named: String, position: SIMD3<Float>, orientation: simd_quatf, relativeTo: Entity?) -> GeometricPin](./entitygeometricpins/set%28named,position,orientation,relativeto%29.md)
  Creates and adds a geometric pin to the entity, and returns the entity geometric pin.
- [func set(named: String, skeletalJointName: String, position: SIMD3<Float>, orientation: simd_quatf) -> GeometricPin](./entitygeometricpins/set%28named,skeletaljointname,position,orientation%29.md)
  Creates and adds a geometric pin to the entity’s skeletal joint, and returns the geometric pin.
### Subscripts
- [subscript(String) -> GeometricPin?](./entitygeometricpins/subscript%28_%29.md)
  Obtains a geometric pin the entity owns by name.
### Type Aliases
- [EntityGeometricPins.Element](./entitygeometricpins/element.md)
  An individual pin in the collection.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Pin and joint components
- [Simulating physics joints in your RealityKit app](./simulating-physics-joints-in-your-realitykit-app.md)
  Create realistic, connected motion using physics joints.
- [struct GeometricPin](./geometricpin.md)
  A structure that identifies a local transform relative to an entity or entity’s animating skeletal joint.
- [struct GeometricPinsComponent](./geometricpinscomponent.md)
  A component that stores a sequence of geometric pins.
- [protocol PhysicsJoint](./physicsjoint.md)
  A type that describes physics joints.
- [struct PhysicsJointsComponent](./physicsjointscomponent.md)
  A component that stores physics joints which RealityKit simulates.
- [struct AttachedTransformComponent](./attachedtransformcomponent.md)
  A component that stores an optional source pin owned by this entity and a target pin which this entity is attached to


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitygeometricpins)*