# RealityViewCameraContent

**Framework**: RealityKit  
**Kind**: struct

The content of a reality view that is displayed through a camera.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
struct RealityViewCameraContent
```

#### Overview

On iOS, `RealityViewCameraContent` displays content in an AR camera view by default, and can display in a “non-AR” mode when requested or when AR or the device’s camera is unavailable. On macOS, `RealityViewCameraContent` always displays its content in a non-AR mode.

You can use `RealityViewCameraContent` to add and remove entities, subscribe to RealityKit events, configure the AR environment, and perform coordinate conversions such as projections and raycasts between the [`RealityView`](realityview.md) space and a SwiftUI View coordinate space.

## Topics

### Structures
- [RealityViewCameraContent.Body](realityviewcameracontent/body.md)
  The default view contents of a [`RealityView`](realityview.md) using [`RealityViewCameraContent`](realityviewcameracontent.md).
### Instance Properties
- [var audioListener: Entity?](realityviewcameracontent/audiolistener.md)
  The entity which defines the listener position and orientation for spatial audio.
- [var camera: RealityViewCamera](realityviewcameracontent/camera.md)
  The active camera for the RealityKit scene.
- [var cameraTarget: Entity?](realityviewcameracontent/cameratarget.md)
  The entity which an orbit camera targets.
- [var entities: RealityViewEntityCollection](realityviewcameracontent/entities.md)
  A collection of RealityKit entities that this view content renders within the scene.
- [var environment: RealityViewEnvironment](realityviewcameracontent/environment.md)
  The view’s background and default lighting properties.
- [var renderingEffects: RealityViewRenderingEffects](realityviewcameracontent/renderingeffects.md)
  The rendering options that you use to selectively enable or disable certain rendering effects.
### Instance Methods
- [func animate(body: () -> Void, completion: (() -> Void)?)](realityviewcameracontent/animate(body:completion:).md)
- [func subscribe<E>(to: E.Type, on: (any EventSource)?, componentType: (any Component.Type)?, (E) -> Void) -> EventSubscription](realityviewcameracontent/subscribe(to:on:componenttype:_:).md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene, or a specific component type for component events.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [RealityCoordinateSpaceProjecting](realitycoordinatespaceprojecting.md)
- [RealityViewContentProtocol](realityviewcontentprotocol.md)

## See Also

- [struct RealityView](realityview.md)
  A view that contains RealityKit content.
- [struct RealityViewContent](realityviewcontent.md)
  The content of a visionOS reality view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcameracontent)*