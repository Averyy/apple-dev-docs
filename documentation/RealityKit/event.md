# Event

**Framework**: RealityKit  
**Kind**: protocol

A type that can be sent as an event.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
protocol Event : Sendable
```

#### Overview

RealityKit provides a number of events you can subscribe to. The system notifies you whenever the event type occurs.

For example, you can subscribe to [`CollisionEvents.Began`](collisionevents/began.md) to know when two objects begin colliding, or [`SceneEvents.Update`](sceneevents/update.md) every time the scene redraws.

To subscribe to an event from inside of a [`RealityView`](realityview.md) builder, call one of the [`RealityViewContentProtocol`](realityviewcontentprotocol.md) `subscribe` methods, for example [`subscribe(to:on:_:)`](realityviewcontentprotocol/subscribe(to:on:_:).md).

Here’s an example of subscribing to the event [`CollisionEvents.Began`](collisionevents/began.md), which occurs when two entities collide:

```swift
struct RealityGame: View {

    @State var collisionSubscription: EventSubscription?

    var body: some View {
        RealityView { content in
            // Create an entity with model and collision components.
            let model = ModelComponent(
                mesh: MeshResource.generateBox(size: .one / 10),
                materials: [SimpleMaterial(color: .red, isMetallic: false)]
            )
            let collision = CollisionComponent(shapes: [ShapeResource.generateBox(size: .one / 10)])
            let collisionEntity = Entity(components: model, collision)
            content.add(collisionEntity)

            // Subscribe to collision began event.
            collisionSubscription = content.subscribe(
               to: CollisionEvents.Began.self,
               on: collisionEntity,
               self.onCollisionBegan
           )
        }
    }
    private func onCollisionBegan(_ event: CollisionEvents.Began) {
        print("collision started")
        let firstEntity = event.entityA // The entity whose collisions you're subscribing to.
        let secondEntity = event.entityB // Another entity in the scene.
        // Respond to collision event...
    }
}
```

> **Note**: Add a [`CollisionComponent`](collisioncomponent.md) to any entities you want to detect collisions for.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [AccessibilityEvents.Activate](accessibilityevents/activate.md)
- [AccessibilityEvents.CustomAction](accessibilityevents/customaction.md)
- [AccessibilityEvents.Decrement](accessibilityevents/decrement.md)
- [AccessibilityEvents.Increment](accessibilityevents/increment.md)
- [AccessibilityEvents.RotorNavigation](accessibilityevents/rotornavigation.md)
- [AnchorStateEvents.DidAnchor](anchorstateevents/didanchor.md)
- [AnchorStateEvents.DidFailToAnchor](anchorstateevents/didfailtoanchor.md)
- [AnchorStateEvents.WillUnanchor](anchorstateevents/willunanchor.md)
- [AnimationEvents.PlaybackCompleted](animationevents/playbackcompleted.md)
- [AnimationEvents.PlaybackLooped](animationevents/playbacklooped.md)
- [AnimationEvents.PlaybackStarted](animationevents/playbackstarted-6pxcp.md)
- [AnimationEvents.PlaybackStarted](animationevents/playbackstarted-876gy.md)
- [AnimationEvents.PlaybackTerminated](animationevents/playbackterminated.md)
- [AnimationEvents.SkeletalPoseUpdateComplete](animationevents/skeletalposeupdatecomplete-o560.md)
- [AnimationEvents.SkeletalPoseUpdateComplete](animationevents/skeletalposeupdatecomplete-88hp5.md)
- [AudioEvents.PlaybackCompleted](audioevents/playbackcompleted.md)
- [CollisionEvents.Began](collisionevents/began.md)
- [CollisionEvents.Ended](collisionevents/ended.md)
- [CollisionEvents.Updated](collisionevents/updated.md)
- [ComponentEvents.DidActivate](componentevents/didactivate.md)
- [ComponentEvents.DidAdd](componentevents/didadd.md)
- [ComponentEvents.DidChange](componentevents/didchange.md)
- [ComponentEvents.WillDeactivate](componentevents/willdeactivate.md)
- [ComponentEvents.WillRemove](componentevents/willremove.md)
- [ImagePresentationEvents.TransitionCompleted](imagepresentationevents/transitioncompleted.md)
- [ImagePresentationEvents.TransitionStarted](imagepresentationevents/transitionstarted.md)
- [ManipulationEvents.DidHandOff](manipulationevents/didhandoff.md)
- [ManipulationEvents.DidUpdateTransform](manipulationevents/didupdatetransform.md)
- [ManipulationEvents.WillBegin](manipulationevents/willbegin.md)
- [ManipulationEvents.WillEnd](manipulationevents/willend.md)
- [ManipulationEvents.WillRelease](manipulationevents/willrelease.md)
- [PhysicsSimulationEvents.DidSimulate](physicssimulationevents/didsimulate.md)
- [PhysicsSimulationEvents.WillSimulate](physicssimulationevents/willsimulate.md)
- [SceneEvents.AnchoredStateChanged](sceneevents/anchoredstatechanged.md)
- [SceneEvents.DidActivateEntity](sceneevents/didactivateentity-5jy9a.md)
- [SceneEvents.DidActivateEntity](sceneevents/didactivateentity-8my6.md)
- [SceneEvents.DidAddEntity](sceneevents/didaddentity-9sx4i.md)
- [SceneEvents.DidAddEntity](sceneevents/didaddentity-6yi7l.md)
- [SceneEvents.DidReparentEntity](sceneevents/didreparententity-8xr41.md)
- [SceneEvents.DidReparentEntity](sceneevents/didreparententity-2rsns.md)
- [SceneEvents.TrackingStateUpdate](sceneevents/trackingstateupdate.md)
- [SceneEvents.Update](sceneevents/update.md)
- [SceneEvents.WillDeactivateEntity](sceneevents/willdeactivateentity-4vvwc.md)
- [SceneEvents.WillDeactivateEntity](sceneevents/willdeactivateentity-3mahl.md)
- [SceneEvents.WillRemoveEntity](sceneevents/willremoveentity-2fca3.md)
- [SceneEvents.WillRemoveEntity](sceneevents/willremoveentity-83c6c.md)
- [SynchronizationEvents.OwnershipChanged](synchronizationevents/ownershipchanged.md)
- [SynchronizationEvents.OwnershipRequest](synchronizationevents/ownershiprequest.md)
- [VideoPlayerEvents.ContentTypeDidChange](videoplayerevents/contenttypedidchange.md)
- [VideoPlayerEvents.ImmersiveViewingModeDidChange](videoplayerevents/immersiveviewingmodedidchange.md)
- [VideoPlayerEvents.ImmersiveViewingModeDidTransition](videoplayerevents/immersiveviewingmodedidtransition.md)
- [VideoPlayerEvents.ImmersiveViewingModeWillTransition](videoplayerevents/immersiveviewingmodewilltransition.md)
- [VideoPlayerEvents.RenderingStatusDidChange](videoplayerevents/renderingstatusdidchange.md)
- [VideoPlayerEvents.SpatialVideoModeDidChange](videoplayerevents/spatialvideomodedidchange.md)
- [VideoPlayerEvents.VideoComfortMitigationDidOccur](videoplayerevents/videocomfortmitigationdidoccur.md)
- [VideoPlayerEvents.VideoSizeDidChange](videoplayerevents/videosizedidchange.md)
- [VideoPlayerEvents.ViewingModeDidChange](videoplayerevents/viewingmodedidchange.md)

## See Also

- [protocol EventSource](eventsource.md)
  A type on which events can be published and subscribed.
- [struct EventSubscription](eventsubscription.md)
  A subscription to an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/event)*