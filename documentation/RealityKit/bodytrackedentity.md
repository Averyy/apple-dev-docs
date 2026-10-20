# BodyTrackedEntity

**Framework**: RealityKit  
**Kind**: class  
**Role**: Class

An entity used to animate a virtual character in an AR scene by tracking a real person.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+

## Declaration

```swift
@MainActor
@preconcurrency class BodyTrackedEntity
```

## Mentions

- [Loading entities from a file](./loading-entities-from-a-file.md)

#### Overview

Like a [`ModelEntity`](./modelentity.md), a [`BodyTrackedEntity`](./bodytrackedentity.md) has a [`ModelComponent`](./modelcomponent.md) that defines its physical appearance. Unlike a model entity, a body-tracked entity lacks the components required to participate in collisions or physics simulations. Instead, a [`BodyTrackingComponent`](./bodytrackingcomponent.md) drives the positioning and arrangement of the entity based on tracking information from the AR session.

![Diagram showing the components present in the body-tracked](https://developer.apple.com/tutorials/images/com.apple.RealityKit/BodyTrackedEntity-1@2x.png)

For an example of how to use a body-tracked entity, see [Capturing Body Motion in 3D](../ARKit/capturing-body-motion-in-3d.md).

## Topics

### Loading a body-tracked entity
- [static func loadBodyTracked(named: String, in: Bundle?) throws -> BodyTrackedEntity](./entity/loadbodytracked%28named,in%29.md)
  Synchronously loads a body-tracked entity from a bundle.
- [static func loadBodyTracked(contentsOf: URL, withName: String?) throws -> BodyTrackedEntity](./entity/loadbodytracked%28contentsof,withname%29.md)
  Synchronously loads a body-tracked entity from a file URL.
- [static func loadBodyTrackedAsync(named: String, in: Bundle?) -> LoadRequest<BodyTrackedEntity>](./entity/loadbodytrackedasync%28named,in%29.md)
  Asynchronously loads a body-tracked entity from a bundle.
- [static func loadBodyTrackedAsync(contentsOf: URL, withName: String?) -> LoadRequest<BodyTrackedEntity>](./entity/loadbodytrackedasync%28contentsof,withname%29.md)
  Asynchronously loads a body-tracked entity from a file URL.

## Relationships

### Inherits From
- [Entity](./entity.md)
### Conforms To
- [CoordinateSpace3D](../Spatial/coordinatespace3d.md)
- [CoordinateSpace3DFloat](../Spatial/coordinatespace3dfloat.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [EventSource](./eventsource.md)
- [HasBodyTracking](./hasbodytracking.md)
- [HasHierarchy](./hashierarchy.md)
- [HasModel](./hasmodel.md)
- [HasSynchronization](./hassynchronization.md)
- [HasTransform](./hastransform.md)
- [Hashable](../Swift/hashable.md)
- [Identifiable](../Swift/identifiable.md)
- [Observable](../Observation/observable.md)
- [RealityCoordinateSpace](./realitycoordinatespace.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Body and face tracking
- [Creating an App for Face-Painting in AR](./creating-an-app-for-face-painting-in-ar.md)
  Combine RealityKit’s face detection with PencilKit to implement virtual face-painting.
- [Occluding virtual content with people](../ARKit/occluding-virtual-content-with-people.md)
  Cover your app’s virtual content with people that ARKit perceives in the camera feed.
- [Placing entities using head and device transform](../visionOS/placing-entities-using-head-and-device-transform.md)
  Query and react to changes in the position and rotation of Apple Vision Pro.
- [struct BodyTrackingComponent](./bodytrackingcomponent.md)
  A component for tracking people in an AR session.
- [protocol HasBodyTracking](./hasbodytracking.md)
  An interface that enables the animation of a virtual character by tracking a real person in AR.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bodytrackedentity)*