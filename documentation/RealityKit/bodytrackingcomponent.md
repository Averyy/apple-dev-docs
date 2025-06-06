# BodyTrackingComponent

**Framework**: RealityKit  
**Kind**: struct

A component for tracking people in an AR session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
struct BodyTrackingComponent
```

#### Overview

Body tracking requires a compatible rigged model. For more information on creating a compatible model, see [`Rigging a Model for Motion Capture`](https://developer.apple.com/documentation/ARKit/rigging-a-model-for-motion-capture).

For a sample app that uses body tracking, see [`Capturing Body Motion in 3D`](https://developer.apple.com/documentation/ARKit/capturing-body-motion-in-3d)

## Topics

### Creating a body tracking component
- [init()](bodytrackingcomponent/init.md)
  Creates a body-tracking component.
- [init(BodyTrackingComponent.Target)](bodytrackingcomponent/init(_:).md)
  Creates a body-tracking component for the given target.
### Pausing body tracking
- [var isPaused: Bool](bodytrackingcomponent/ispaused.md)
  A Boolean that you can set to temporarily stop applying body tracking to the model and freeze the model in its current pose.
### Selecting a body to track
- [var target: BodyTrackingComponent.Target](bodytrackingcomponent/target-swift.property.md)
  The body-tracking setting.
- [BodyTrackingComponent.Target](bodytrackingcomponent/target-swift.enum.md)
  Body-tracking settings for selecting a person to track.
### Registering a component type
- [static func registerComponent()](bodytrackingcomponent/registercomponent.md)
  Registers a new component type.
### Comparing body tracking components
- [static func == (BodyTrackingComponent, BodyTrackingComponent) -> Bool](bodytrackingcomponent/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](bodytrackingcomponent/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Default Implementations
- [Component Implementations](bodytrackingcomponent/component-implementations.md)
- [Equatable Implementations](bodytrackingcomponent/equatable-implementations.md)

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [Creating an App for Face-Painting in AR](creating-an-app-for-face-painting-in-ar.md)
  Combine RealityKit’s face detection with PencilKit to implement virtual face-painting.
- [Occluding virtual content with people](../ARKit/occluding-virtual-content-with-people.md)
  Cover your app’s virtual content with people that ARKit perceives in the camera feed.
- [class BodyTrackedEntity](bodytrackedentity.md)
  An entity used to animate a virtual character in an AR scene by tracking a real person.
- [protocol HasBodyTracking](hasbodytracking.md)
  An interface that enables the animation of a virtual character by tracking a real person in AR.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bodytrackingcomponent)*