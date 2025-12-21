# AnimationStateProtocol

**Framework**: RealityKit  
**Kind**: protocol

The protocol representing the current animation state of an action animation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
protocol AnimationStateProtocol
```

#### Overview

The animation state allows actions to animate a target value using RealityKit’s animation engine.

Animating values with the animation engine allows for cross-fading and additive compositing with other RealityKit animations targeting the same value.

Access the animation state structure from the event structure returned to `.updated` event handlers. Define a valid bind target and matching animation type to make the state structure available and non nil.

> **Note**: Custom actions don’t support animating [`BlendShapeWeights`](blendshapeweights.md).

## Topics

### Associated Types
- [associatedtype ValueType : AnimatableData](animationstateprotocol/valuetype.md)
### Instance Properties
- [var defaultSource: Self.ValueType?](animationstateprotocol/defaultsource.md)
  The previous blend stage value.
- [var defaultTarget: Self.ValueType?](animationstateprotocol/defaulttarget.md)
  The default unanimated value of the target.
- [var deltaTime: TimeInterval](animationstateprotocol/deltatime.md)
  The time that has elapsed since the most recent evaluation, or 0 if animation is paused.
- [var evaluationTime: TimeInterval](animationstateprotocol/evaluationtime.md)
  The time at which the animation result should be evaluated.
- [var normalizedTime: TimeInterval](animationstateprotocol/normalizedtime.md)
  The normalized time ranges from 0 to 1, and is the time at which the animation result should be evaluated.
### Instance Methods
- [func storeAnimatedValue<ValueType>(ValueType) -> Bool](animationstateprotocol/storeanimatedvalue(_:).md)
  Stores the action’s animated value, which the animation manager uses to produce a final animated result. Returns true on success, otherwise false.

## Relationships

### Conforming Types
- [AnimationState](animationstate.md)

## See Also

- [struct ActionEvent](actionevent.md)
  The structure returned to all action event handlers.
- [struct AnimationState](animationstate.md)
  The concretely typed animation state structure.
- [struct ActionEventType](actioneventtype.md)
  A set of events that an action responds to.
- [struct ActionEventDefinition](actioneventdefinition.md)
  Defines an action event interval, and any associated parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationstateprotocol)*