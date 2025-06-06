# Scene

**Framework**: RealityKit  
**Kind**: class

A container that holds the collection of entities that an AR view renders.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class Scene
```

#### Overview

You don’t create a [`Scene`](scene.md) instance directly. Instead, you get the one and only scene associated with a view from the [`scene`](arview/scene.md) property of an [`ARView`](arview.md) instance.

![Block diagram showing the scene as a property of an AR view, with anchor](https://docs-assets.developer.apple.com/published/4dc0859966232845f9097db726e4eeb4/Scene-1%402x.png)

To add content to the view’s scene, you first create and add one or more [`AnchorEntity`](anchorentity.md) instances to the scene’s [`anchors`](scene/anchors.md) collection. Anchors tell RealityKit how to pin virtual content to real world objects, like flat surfaces or images. You then add a hierarchy of other [`Entity`](entity.md) instances to each anchor to indicate the geometry and behaviors that RealityKit should render at a given anchor point.

## Topics

### Identifying the scene
- [var name: String](scene/name.md)
  A name for the scene.
- [var id: UInt64](scene/id-9ai5s.md)
  The stable identity of the entity associated with this instance.
- [var id: UInt64](scene/id-9ai5s.md)
  The stable identity of the entity associated with this instance.
### Adding and removing anchors
- [var anchors: Scene.AnchorCollection](scene/anchors.md)
  The collection of anchors contained in the scene.
- [func addAnchor(any HasAnchoring)](scene/addanchor(_:).md)
  Adds an anchor to the scene’s list of anchors.
- [func removeAnchor(any HasAnchoring)](scene/removeanchor(_:).md)
  Removes the specified anchor from the scene.
### Finding entities
- [func findEntity(named: String) -> Entity?](scene/findentity(named:).md)
  Searches the scene’s anchor entity hierarchies for an entity with the given name.
- [func performQuery(EntityQuery) -> QueryResult<Entity>](scene/performquery(_:).md)
  Returns all entities of the scene which pass the query.
- [func findEntity(id: Entity.ID) -> Entity?](scene/findentity(id:).md)
  Returns `Entity` with the given `Entity.ID` in the `Scene`.
### Detecting intersections
- [func raycast(origin: SIMD3<Float>, direction: SIMD3<Float>, length: Float, query: CollisionCastQueryType, mask: CollisionGroup, relativeTo: Entity?) -> [CollisionCastHit]](scene/raycast(origin:direction:length:query:mask:relativeto:).md)
  Performs a ray cast against all the geometry in the scene for a ray of a given origin, direction, and length.
- [func raycast(from: SIMD3<Float>, to: SIMD3<Float>, query: CollisionCastQueryType, mask: CollisionGroup, relativeTo: Entity?) -> [CollisionCastHit]](scene/raycast(from:to:query:mask:relativeto:).md)
  Performs a ray cast against all the geometry in the scene for a ray between two end points.
- [func convexCast(convexShape: ShapeResource, fromPosition: SIMD3<Float>, fromOrientation: simd_quatf, toPosition: SIMD3<Float>, toOrientation: simd_quatf, query: CollisionCastQueryType, mask: CollisionGroup, relativeTo: Entity?) -> [CollisionCastHit]](scene/convexcast(convexshape:fromposition:fromorientation:toposition:toorientation:query:mask:relativeto:).md)
  Performs a convex shape cast against all the geometry in the scene.
- [func pixelCast(from: SIMD3<Float>, to: SIMD3<Float>) async throws -> PixelCastHit?](scene/pixelcast(from:to:).md)
  Performs a ray cast against all the geometry in the scene for a ray between two end points.
- [func pixelCast(origin: SIMD3<Float>, direction: SIMD3<Float>, length: Float) async throws -> PixelCastHit?](scene/pixelcast(origin:direction:length:).md)
  Performs a ray cast against all the geometry in the scene for a ray of a given origin, direction, and length.
### Synchronizing entities with other devices
- [var synchronizationService: (any SynchronizationService)?](scene/synchronizationservice.md)
  The service to use for network synchronization.
### Publishing and subscribing to events
- [func publisher<E>(for: E.Type, on: (any EventSource)?) -> Scene.Publisher<E>](scene/publisher(for:on:).md)
  Generates a publisher for events of the specified type.
- [func subscribe<E>(to: E.Type, on: (any EventSource)?, (E) -> Void) -> any Cancellable](scene/subscribe(to:on:_:).md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene.
- [func publisher<E>(for: E.Type, on: (any EventSource)?, componentType: (any Component.Type)?) -> Scene.Publisher<E>](scene/publisher(for:on:componenttype:).md)
  Returns a `Publisher` for events of the specified type in a `Scene`.
- [func subscribe<E>(to: E.Type, on: (any EventSource)?, componentType: (any Component.Type)?, (E) -> Void) -> any Cancellable](scene/subscribe(to:on:componenttype:_:).md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene, or limited to a specific component type for component events.
### Comparing scenes
- [static func == (Scene, Scene) -> Bool](scene/==(_:_:).md)
  Indicates whether two scenes are equal.
- [static func != (Self, Self) -> Bool](scene/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func hash(into: inout Hasher)](scene/hash(into:).md)
  Hashes the essential components of the scene by feeding them into the given hash function.
- [var hashValue: Int](scene/hashvalue.md)
  The hash value.
### Structures
- [struct AnchorCollection](scene/anchorcollection.md)
  A collection of anchor entities.
- [struct Publisher](scene/publisher.md)
  A publisher for the given event type in the scene.
### Instance Properties
- [var timebase: CMTimebase](scene/timebase.md)
  The default timebase for the scene, useful for driving custom times managed by the user which are derived from the scene time.
### Default Implementations
- [Equatable Implementations](scene/equatable-implementations.md)
- [Hashable Implementations](scene/hashable-implementations.md)
- [Identifiable Implementations](scene/identifiable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [EventSource](eventsource.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AnchorCollection](scene/anchorcollection.md)
  A collection of anchor entities.
- [typealias ID](scene/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene)*