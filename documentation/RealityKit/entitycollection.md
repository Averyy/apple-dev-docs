# EntityCollection

**Framework**: RealityKit  
**Kind**: protocol  
**Role**: Protocol

An ordered, mutable collection of entities.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
protocol EntityCollection : Collection where Self.Element == Entity, Self.Index == Int
```

## Topics

### Instance Methods
- [func append(Entity)](./entitycollection/append%28_%29.md)
  Adds the specified entity to the end of this collection.
- [func append<S>(contentsOf: S)](./entitycollection/append%28contentsof%29.md)
  Adds the specified sequence of entities to the end of this collection, in order.
- [func insert(Entity, beforeIndex: Int)](./entitycollection/insert%28_,beforeindex%29.md)
  Adds the specified entity to this collection directly before the entity at the given index. If the entity is already located before the index, the collection will not change.
- [func insert<S>(contentsOf: S, beforeIndex: Int)](./entitycollection/insert%28contentsof,beforeindex%29.md)
  Adds the specified sequence of entities to this collection in order, directly before the entity at the given index.
- [func remove(Entity)](./entitycollection/remove%28_%29.md)
  Removes the entity from the collection.
- [func remove(at: Int)](./entitycollection/remove%28at%29.md)
  Removes the entity at the given index from this collection.
- [func removeAll()](./entitycollection/removeall%28%29.md)
  Removes all entities from this collection.
- [func removeAll(where: (Entity) throws -> Bool) rethrows](./entitycollection/removeall%28where%29.md)
  Removes all entities from this collection that satisfy the given predicate.
- [func replaceAll<S>(S)](./entitycollection/replaceall%28_%29.md)
  Replaces all entities in this collection with those from the given sequence.

## Relationships

### Inherits From
- [Collection](../Swift/collection.md)
- [Sequence](../Swift/sequence.md)
### Conforming Types
- [Entity.ChildCollection](./entity/childcollection.md)
- [RealityRenderer.EntityCollection](./realityrenderer/entitycollection.md)
- [RealityViewEntityCollection](./realityviewentitycollection.md)

## See Also

### SwiftUI scene presentation
- [Controlling the layout behavior of a reality view](./controlling-the-layout-behavior-of-a-realityview.md)
  Choose a strategy for sizing frames and centering 3D content.
- [struct RealityView](./realityview.md)
  A view that contains RealityKit content.
- [struct RealityViewContent](./realityviewcontent.md)
  The content of a visionOS reality view.
- [struct RealityViewCameraContent](./realityviewcameracontent.md)
  The content of a reality view that is displayed through a camera.
- [protocol RealityViewContentProtocol](./realityviewcontentprotocol.md)
  A protocol representing the content of a reality view.
- [struct RealityViewDefaultPlaceholder](./realityviewdefaultplaceholder.md)
  A view that represents the default placeholder for a RealityView.
- [struct RealityViewEntityCollection](./realityviewentitycollection.md)
  A collection of entities in a RealityView.
- [struct RealityViewLayoutOption](./realityviewlayoutoption.md)
  Options that specify the frame sizing and content alignment option for `RealityView`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitycollection)*