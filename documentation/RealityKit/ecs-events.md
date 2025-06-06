# Events

**Framework**: RealityKit

Respond to things happening in your RealityKit scene by subscribing to specific event types.

#### Overview

You can receive notifications to specific RealityKit events — all of which conform to the Event protocol — by subscribing to specific events. The kinds of events you can subscribe to include the following:

- Two entities colliding
- An entity receiving a new component
- Audio playback reaching the end of its content

For example, you can receive a notification:

- When two objects begin colliding by subscribing to [`CollisionEvents.Began`](collisionevents/began.md) event
- When the scene redraws by subscribing to the [`SceneEvents.Update`](sceneevents/update.md) event

## Topics

### Core event types
- [protocol Event](event.md)
  A type that can be sent as an event.
- [protocol EventSource](eventsource.md)
  A type on which events can be published and subscribed.
- [struct EventSubscription](eventsubscription.md)
  A subscription to an event.
- [enum SceneEvents](sceneevents.md)
  Events the scene invokes.
- [enum ComponentEvents](componentevents.md)
  Provides the events related to components.
### Physics and motion events
- [enum AnimationEvents](animationevents.md)
  Notable milestones that the framework signals during animation playback.
- [enum CollisionEvents](collisionevents.md)
- [enum PhysicsSimulationEvents](physicssimulationevents.md)
  Types of events that fire during physics simulations
### Media events
- [enum AudioEvents](audioevents.md)
  Events associated with audio playback.
- [enum VideoPlayerEvents](videoplayerevents.md)
  Events associated with video playback for VideoPlayerComponent.
### Accessibility events
- [enum AccessibilityEvents](accessibilityevents.md)
### Network synchronization events
- [enum SynchronizationEvents](synchronizationevents.md)
  Events associated with network synchronization of scene information.

## See Also

- [Scenes](ecs-scenes.md)
  The context that holds all RealityKit entities.
- [Systems](ecs-systems.md)
  Apply behaviors and physical effects to the entities in a RealityKit scene.
- [Entity actions](ecs-entity-actions.md)
  Create simple, reusable actions that can change your app state, RealityKit scene, or animate an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ecs-events)*