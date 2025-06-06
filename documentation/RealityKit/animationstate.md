# AnimationState

**Framework**: RealityKit  
**Kind**: struct

The concretely typed animation state structure.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct AnimationState<Value> where Value : AnimatableData
```

#### Overview

Access the animation state structure from the event structure returned to  the action’s `.updated` event handler. Define a valid bind target and matching animation type for the action animation to make the state structure available and non-nil.

(See: [`AnimationStateProtocol`](animationstateprotocol.md))

## Topics

### Instance Properties
- [var defaultSource: Value?](animationstate/defaultsource-3pn6r.md)
  See: [`defaultSource`](animationstateprotocol/defaultsource.md)
- [var defaultSource: JointTransforms?](animationstate/defaultsource-5ddek.md)
  Returns the  joint transforms representing the default source value.
- [var defaultTarget: JointTransforms?](animationstate/defaulttarget-9kxlt.md)
  Returns the joint transforms representing the default target value.
- [var defaultTarget: Value?](animationstate/defaulttarget-gdi6.md)
  See: [`defaultTarget`](animationstateprotocol/defaulttarget.md)
- [let deltaTime: TimeInterval](animationstate/deltatime.md)
  See: [`deltaTime`](animationstateprotocol/deltatime.md)
- [let evaluationTime: TimeInterval](animationstate/evaluationtime.md)
  See [`evaluationTime`](animationstateprotocol/evaluationtime.md)
- [let normalizedTime: TimeInterval](animationstate/normalizedtime.md)
  See [`normalizedTime`](animationstateprotocol/normalizedtime.md)
### Instance Methods
- [func defaultSourceJoints(index: Int, count: Int, transforms: inout [Transform]) -> Bool](animationstate/defaultsourcejoints(index:count:transforms:).md)
  Retrieves a subset of default source joints, and stores them in the output transform array.
- [func defaultTargetJoints(index: Int, count: Int, transforms: inout [Transform]) -> Bool](animationstate/defaulttargetjoints(index:count:transforms:).md)
  Retrieves a subset of default target joints, and stores them in the output transform array.
- [func storeAnimatedJoints(transforms: [Transform], jointIndex: Int) -> Bool](animationstate/storeanimatedjoints(transforms:jointindex:).md)
  Stores a subset of animated joints.
- [func storeAnimatedValue<ValueType>(ValueType) -> Bool](animationstate/storeanimatedvalue(_:).md)
  See: [`storeAnimatedValue(_:)`](animationstateprotocol/storeanimatedvalue(_:).md)
### Type Aliases
- [AnimationState.ValueType](animationstate/valuetype.md)

## Relationships

### Conforms To
- [AnimationStateProtocol](animationstateprotocol.md)

## See Also

- [struct ActionEvent](actionevent.md)
  The structure returned to all action event handlers.
- [struct ActionEventType](actioneventtype.md)
  A set of events that an action responds to.
- [struct ActionEventDefinition](actioneventdefinition.md)
  Defines an action event interval, and any associated parameters.
- [protocol AnimationStateProtocol](animationstateprotocol.md)
  The protocol representing the current animation state of an action animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationstate)*