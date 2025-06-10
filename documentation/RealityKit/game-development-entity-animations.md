# Entity animations

**Framework**: RealityKit

Dynamically move, rotate, and scale entities at runtime.

## Topics

### Animation playback
- [class AnimationResource](animationresource.md)
  An animation for the properties of scenes or entities.
- [struct AnimationLibraryComponent](animationlibrarycomponent.md)
  A component that represents a collection of animations that an entity can play.
- [AnimationLibraryComponent.AnimationCollection](animationlibrarycomponent/animationcollection.md)
  A collection of animations an entity can play.
- [enum AnimationEvents](animationevents.md)
  Notable milestones that the framework signals during animation playback.
- [class AnimationPlaybackController](animationplaybackcontroller.md)
  A controller that manages animation playback.
- [enum AnimationRepeatMode](animationrepeatmode.md)
  Options that determine whether an animation replays after completion.
### Animation definitions
- [struct SampledAnimation](sampledanimation.md)
  An animation that cycles through a series of frames at a constant interval.
- [enum TweenMode](tweenmode.md)
  Options that determine whether an animation switches between frames gradually or abruptly.
- [struct FromToByAnimation](fromtobyanimation.md)
  An animation that starts, stops, or increments by a specific value.
- [struct AnimationTimingFunction](animationtimingfunction.md)
  The pacing of an animation transition.
- [struct AnimationView](animationview.md)
  An animation that represents a variation of another animation.
- [struct OrbitAnimation](orbitanimation.md)
  An animation that revolves an entity around its origin.
- [protocol AnimationDefinition](animationdefinition.md)
  The configuration, including target object, timeframe, and visual semantics, of an animation.
- [struct AnimationFillMode](animationfillmode.md)
  Options that determine which animation frames display outside of the normal duration.
- [struct AnimationGroup](animationgroup.md)
  A collection of animations that play simultaneously.
- [struct AnimationHandoffType](animationhandofftype.md)
  The type of handoff the play animation method performs between a current animation and a new animation.
### Bindable animation targets
- [struct BindPath](bindpath.md)
  The components of a target’s path that refer to the animation properties of a nested scene or entity.
- [enum BindTarget](bindtarget.md)
  A reference to a particular scene, entity, or property that animates.
- [struct BindableValue](bindablevalue.md)
  The value of a bindable target.
- [struct BindableValuesReference](bindablevaluesreference.md)
  A reference to a bindable value of an animation.
- [struct ComponentAnimatableData](componentanimatabledata.md)
- [struct ParameterSet](parameterset.md)
  A reference to general-purpose entity parameters for animations.
- [struct InternalBindPath](internalbindpath.md)
  A bind target for framework-provided properties.
### Compliance-related protocols
- [protocol AnimatableData](animatabledata.md)
  A functionality specification that animatable data types adopt.
- [protocol BindableData](bindabledata.md)
  An opaque base protocol for bindable data objects.
### Blend trees
- [struct BlendTreeAnimation](blendtreeanimation.md)
  A collection of animations on the same property that the framework blends to a single animation.
- [protocol BlendTreeNode](blendtreenode.md)
  An interface for a node that’s a member of a blend tree.
- [struct BlendTreeBlendNode](blendtreeblendnode.md)
  A source node for an animation that mixes several animations to form a single animation.
- [struct BlendTreeSourceNode](blendtreesourcenode.md)
  A blend node that contains an animation.
- [struct BlendTreeInvalidNode](blendtreeinvalidnode.md)
  A blend tree node that’s internal only or sources from an invalid definition.
- [enum BlendWeight](blendweight.md)
  A numerical representation of the impact an animation has on a scene or entity.

## See Also

- [Gaming sample code projects](game-development-sample-code.md)
  Explore a collection of projects relating to game development.
- [Character control, skeletons, and inverse kinematics](game-development-character-skeletons.md)
  Direct the movements and animation of models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/game-development-entity-animations)*