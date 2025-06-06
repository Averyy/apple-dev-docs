# ActionAnimation

**Framework**: RealityKit  
**Kind**: struct

Defines an an action animation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct ActionAnimation<ActionType> where ActionType : EntityAction
```

#### Overview

The definition is used to generate an action animation based `AnimationResource` that can then be played by calling [`playAnimation(_:transitionDuration:blendLayerOffset:separateAnimatedValue:startsPaused:clock:handoffType:)`](entity/playanimation(_:transitionduration:blendlayeroffset:separateanimatedvalue:startspaused:clock:handofftype:).md)

Action animations can be used to perform operations in lock-step with playback.

Actions can be grouped or sequenced with pre-existing animation resources or be stand alone. For example an action that triggers sound can be grouped with a sampled animation to trigger sound effects at the appropriate times during playback. See: [`group(with:)`](animationresource/group(with:).md)

Stand alone action animations can animate target values using RealityKit’s animation engine with cross fade, and additive compositing support.

(See: [`AnimationStateProtocol`](animationstateprotocol.md))

## Topics

### Initializers
- [init(for: ActionType, events: [ActionAnimation<ActionType>.EventDefinitionType], name: String, bindTarget: BindTarget?, blendLayer: Int32, repeatMode: AnimationRepeatMode, fillMode: AnimationFillMode, trimStart: TimeInterval?, trimEnd: TimeInterval?, trimDuration: TimeInterval?, offset: TimeInterval, delay: TimeInterval, speed: Float)](actionanimation/init(for:events:name:bindtarget:blendlayer:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:).md)
  Constructs an action animation that generates events at user defined times.
### Instance Properties
- [var action: ActionType?](actionanimation/action.md)
  The action for which an animation is being defined.
- [var bindTarget: BindTarget](actionanimation/bindtarget.md)
  [`bindTarget`](animationdefinition/bindtarget.md) is not used.
- [var blendLayer: Int32](actionanimation/blendlayer.md)
  [`blendLayer`](animationdefinition/blendlayer.md) is not used.
- [var delay: TimeInterval](actionanimation/delay.md)
  An amount of time that lapses before the animation plays.
- [var duration: TimeInterval](actionanimation/duration.md)
  The elapsed time for one complete rotation.
- [var eventDefinitions: [ActionEventDefinition<ActionType>]](actionanimation/eventdefinitions.md)
  The event interval definitions, and their associated parameter data.
- [var fillMode: AnimationFillMode](actionanimation/fillmode.md)
  An option that determines which data displays outside of the normal duration.
- [var name: String](actionanimation/name.md)
  A textual name for the animation.
- [var offset: TimeInterval](actionanimation/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var repeatMode: AnimationRepeatMode](actionanimation/repeatmode.md)
  An option that determines how the animation repeats.
- [var speed: Float](actionanimation/speed.md)
  A factor that changes the animation’s rate of playback.
- [var trimDuration: TimeInterval?](actionanimation/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimEnd: TimeInterval?](actionanimation/trimend.md)
  The optional time, in seconds, at which the animation stops.
- [var trimStart: TimeInterval?](actionanimation/trimstart.md)
  The optional time, in seconds, at which the animation plays.
### Type Aliases
- [ActionAnimation.EventDefinitionType](actionanimation/eventdefinitiontype.md)
- [ActionAnimation.EventParameterType](actionanimation/eventparametertype.md)
### Default Implementations
- [AnimationDefinition Implementations](actionanimation/animationdefinition-implementations.md)

## Relationships

### Conforms To
- [AnimationDefinition](animationdefinition.md)

## See Also

- [protocol EntityAction](entityaction.md)
  A protocol that defines an action for an entity.
- [enum ActionEntityResolution](actionentityresolution.md)
  Options available to determine the resolution method for a target entity in an action.
- [protocol ActionHandlerProtocol](actionhandlerprotocol.md)
  The base protocol for action handlers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionanimation)*