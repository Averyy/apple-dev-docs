# RealityViewContent

**Framework**: RealityKit  
**Kind**: struct

The content of a visionOS reality view.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct RealityViewContent
```

#### Overview

Add content that you want your visionOS app to display to a `RealityViewContent`.

You can use `RealityViewContent` to add and remove entities, subscribe to RealityKit events, and perform coordinate conversions between RealityKit entity space and a SwiftUI View’s coordinate space.

## Topics

### Structures
- [RealityViewContent.Body](realityviewcontent/body.md)
  The default view contents of a reality view, using reality view content.
### Instance Methods
- [func animate(body: () -> Void, completion: (() -> Void)?)](realityviewcontent/animate(body:completion:).md)
- [func subscribe<E>(to: E.Type, on: (any EventSource)?, componentType: (any Component.Type)?, (E) -> Void) -> EventSubscription](realityviewcontent/subscribe(to:on:componenttype:_:).md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene, or a specific component type for component events.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [RealityCoordinateSpace](realitycoordinatespace.md)
- [RealityCoordinateSpaceConverting](realitycoordinatespaceconverting.md)
- [RealityViewContentProtocol](realityviewcontentprotocol.md)

## See Also

- [struct RealityView](realityview.md)
  A view that contains RealityKit content.
- [struct RealityViewCameraContent](realityviewcameracontent.md)
  The content of a reality view that is displayed through a camera.
- [protocol RealityViewContentProtocol](realityviewcontentprotocol.md)
  A protocol representing the content of a reality view.
- [struct RealityViewDefaultPlaceholder](realityviewdefaultplaceholder.md)
  A view that represents the default placeholder for a RealityView.
- [struct RealityViewEntityCollection](realityviewentitycollection.md)
  A collection of entities in a RealityView.
- [struct RealityViewLayoutOption](realityviewlayoutoption.md)
  Options that specify the frame sizing and content alignment option for `RealityView`.
- [protocol EntityCollection](entitycollection.md)
  An ordered, mutable collection of entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcontent)*