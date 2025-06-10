# HasBodyTracking

**Framework**: RealityKit  
**Kind**: protocol

An interface that enables the animation of a virtual character by tracking a real person in AR.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol HasBodyTracking : HasTransform
```

#### Overview

> ❗ **Important**: Body tracking requires a compatible rigged model. For more information on creating a compatible model, see [`Rigging a Model for Motion Capture`](https://developer.apple.com/documentation/ARKit/rigging-a-model-for-motion-capture).

## Topics

### Accessing the component
- [var bodyTracking: BodyTrackingComponent](hasbodytracking/bodytracking.md)
  The body-tracking component for the body-tracked entity.

## Relationships

### Inherits From
- [HasTransform](hastransform.md)
### Conforming Types
- [BodyTrackedEntity](bodytrackedentity.md)

## See Also

- [Creating an App for Face-Painting in AR](creating-an-app-for-face-painting-in-ar.md)
  Combine RealityKit’s face detection with PencilKit to implement virtual face-painting.
- [Occluding virtual content with people](../ARKit/occluding-virtual-content-with-people.md)
  Cover your app’s virtual content with people that ARKit perceives in the camera feed.
- [struct BodyTrackingComponent](bodytrackingcomponent.md)
  A component for tracking people in an AR session.
- [class BodyTrackedEntity](bodytrackedentity.md)
  An entity used to animate a virtual character in an AR scene by tracking a real person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hasbodytracking)*