# EntityAction

**Framework**: RealityKit  
**Kind**: protocol

A protocol that defines an action for an entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
protocol EntityAction
```

#### Overview

Structures that conform to `EntityAction` can contain data that an [`ActionAnimation`](actionanimation.md) stores. If your apps needs to serialize the animation resource to a file, the structure also needs to adopt and conform to the [`Codable`](https://developer.apple.com/documentation/Swift/Codable) protocol.

As action animation playback occurs, unique action events are raised for its associated `EntityAction` conforming type.

These events allow application code to animate target values (see [`AnimationStateProtocol`](animationstateprotocol.md)), and perform custom operations in lock step with animation playback.

The action data stored within an action animation is available to the action’s event handler.

> **Note**: Custom actions don’t support animating [`BlendShapeWeights`](blendshapeweights.md).

## Topics

### Associated Types
- [associatedtype EventParameterType = Never](entityaction/eventparametertype.md)
  The associated event parameter type.
### Instance Properties
- [var animatedValueType: (any AnimatableData.Type)?](entityaction/animatedvaluetype.md)
  A value that defines the type that the action animates, if the action animates a target value.
- [var isAdditive: Bool](entityaction/isadditive.md)
  A Boolean value that determines whether this action additively blends with the prior stage.
- [var isReversible: Bool](entityaction/isreversible.md)
  A Boolean value that determines whether the action reverses prior operations when playback is reverses.
### Type Methods
- [static registerAction()](entityaction/registeraction.md)
  Registers the action into the action-types registry.
- [static subscribe(to:_:)](entityaction/subscribe(to:_:).md)
  Subscribes to an action event.
- [static func unsubscribe(from: ActionEventType)](entityaction/unsubscribe(from:).md)
  Unsubscribes from an action event.
- [static func unsubscribeAll()](entityaction/unsubscribeall.md)
  Unsubscribes from all action events.

## Relationships

### Conforming Types
- [BillboardAction](billboardaction.md)
- [EmphasizeAction](emphasizeaction.md)
- [FromToByAction](fromtobyaction.md)
- [ImpulseAction](impulseaction.md)
- [OrbitEntityAction](orbitentityaction.md)
- [PlayAnimationAction](playanimationaction.md)
- [PlayAudioAction](playaudioaction.md)
- [SetEntityEnabledAction](setentityenabledaction.md)
- [SpinAction](spinaction.md)

## See Also

- [struct ActionAnimation](actionanimation.md)
  Defines an an action animation.
- [enum ActionEntityResolution](actionentityresolution.md)
  Options available to determine the resolution method for a target entity in an action.
- [protocol ActionHandlerProtocol](actionhandlerprotocol.md)
  The base protocol for action handlers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entityaction)*