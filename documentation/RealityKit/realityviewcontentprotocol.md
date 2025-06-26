# RealityViewContentProtocol

**Framework**: RealityKit  
**Kind**: protocol

A protocol representing the content of a reality view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
protocol RealityViewContentProtocol
```

#### Overview

Do not interface with this protocol directly. Instead, use [`RealityViewContent`](realityviewcontent.md) with your [`RealityView`](realityview.md).

## Topics

### Managing view content
- [func add(Entity)](realityviewcontentprotocol/add(_:).md)
  Adds an entity to this content.
- [func remove(Entity)](realityviewcontentprotocol/remove(_:).md)
  Removes an entity from this content, if present.
- [associatedtype Entities : EntityCollection](realityviewcontentprotocol/entities-swift.associatedtype.md)
  The type of collection used for `entities`.
- [var entities: Self.Entities](realityviewcontentprotocol/entities-swift.property.md)
  A collection of RealityKit entities that this view content renders within the scene.
### Handling subscriptions
- [func subscribe<E>(to: E.Type, on: (any EventSource)?, (E) -> Void) -> EventSubscription](realityviewcontentprotocol/subscribe(to:on:_:).md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene.
- [func subscribe<E>(to: E.Type, componentType: (any Component.Type)?, (E) -> Void) -> EventSubscription](realityviewcontentprotocol/subscribe(to:componenttype:_:).md)
  Subscribes to an event type, optionally limited to a specific component type for component events.
- [func subscribe<E>(to: E.Type, on: (any EventSource)?, componentType: (any Component.Type)?, (E) -> Void) -> EventSubscription](realityviewcontentprotocol/subscribe(to:on:componenttype:_:).md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene, or a specific component type for component events.

## Relationships

### Conforming Types
- [RealityViewCameraContent](realityviewcameracontent.md)
- [RealityViewContent](realityviewcontent.md)

## See Also

- [struct RealityView](realityview.md)
  A view that contains RealityKit content.
- [struct RealityViewContent](realityviewcontent.md)
  The content of a visionOS reality view.
- [struct RealityViewCameraContent](realityviewcameracontent.md)
  The content of a reality view that is displayed through a camera.
- [struct RealityViewDefaultPlaceholder](realityviewdefaultplaceholder.md)
  A view that represents the default placeholder for a RealityView.
- [struct RealityViewEntityCollection](realityviewentitycollection.md)
  A collection of entities in a RealityView.
- [struct RealityViewLayoutOption](realityviewlayoutoption.md)
  Options that specify the frame sizing and content alignment option for `RealityView`.
- [protocol EntityCollection](entitycollection.md)
  An ordered, mutable collection of entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcontentprotocol)*