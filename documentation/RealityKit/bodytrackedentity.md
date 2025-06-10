# BodyTrackedEntity

**Framework**: RealityKit  
**Kind**: class

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

- [Loading entities from a file](loading-entities-from-a-file.md)

#### Overview

Like a [`ModelEntity`](modelentity.md), a [`BodyTrackedEntity`](bodytrackedentity.md) has a [`ModelComponent`](modelcomponent.md) that defines its physical appearance. Unlike a model entity, a body-tracked entity lacks the components required to participate in collisions or physics simulations. Instead, a [`BodyTrackingComponent`](bodytrackingcomponent.md) drives the positioning and arrangement of the entity based on tracking information from the AR session.

![Diagram showing the components present in the body-tracked](https://docs-assets.developer.apple.com/published/a7ef445bb1ab998fb177db5aa1f926fa/BodyTrackedEntity-1%402x.png)

For an example of how to use a body-tracked entity, see [`Capturing Body Motion in 3D`](https://developer.apple.com/documentation/ARKit/capturing-body-motion-in-3d).

## Relationships

### Inherits From
- [Entity](entity.md)
### Conforms To
- [CoordinateSpace3D](../Spatial/CoordinateSpace3D.md)
- [CoordinateSpace3DFloat](../Spatial/CoordinateSpace3DFloat.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [EventSource](eventsource.md)
- [HasBodyTracking](hasbodytracking.md)
- [HasHierarchy](hashierarchy.md)
- [HasModel](hasmodel.md)
- [HasSynchronization](hassynchronization.md)
- [HasTransform](hastransform.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Observable](../Observation/Observable.md)
- [RealityCoordinateSpace](realitycoordinatespace.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Creating an App for Face-Painting in AR](creating-an-app-for-face-painting-in-ar.md)
  Combine RealityKit’s face detection with PencilKit to implement virtual face-painting.
- [Occluding virtual content with people](../ARKit/occluding-virtual-content-with-people.md)
  Cover your app’s virtual content with people that ARKit perceives in the camera feed.
- [struct BodyTrackingComponent](bodytrackingcomponent.md)
  A component for tracking people in an AR session.
- [protocol HasBodyTracking](hasbodytracking.md)
  An interface that enables the animation of a virtual character by tracking a real person in AR.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bodytrackedentity)*