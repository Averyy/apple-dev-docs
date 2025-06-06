# AnimationResource

**Framework**: RealityKit  
**Kind**: class

An animation for the properties of scenes or entities.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class AnimationResource
```

#### Overview

You find animation resources in an entity’s [`availableAnimations`](entity/availableanimations.md) array. Animation resources come bundled with an entity when you load the entity from a file. They describe an animation that’s specific to the entity to which they are attached.

Use the entity’s [`playAnimation(_:transitionDuration:startsPaused:)`](entity/playanimation(_:transitionduration:startspaused:).md) method to play a particular item in its animation resource array, or the `playAnimation(named:transitionDuration:startsPaused:)` method to play all of the animations with a given name. From both methods, you receive an [`AnimationPlaybackController`](animationplaybackcontroller.md) instance that lets you manage playback of the resource.

If you want to loop an animation, call the resource’s [`repeat(count:)`](animationresource/repeat(count:).md) method to create a new resource that plays a given number of times in a row, or call the [`repeat(duration:)`](animationresource/repeat(duration:).md) method to create a new resource that loops for the given duration. The latter loops indefinitely if you omit the duration parameter. You use the new animation resource that these methods return just as you would any other.

## Topics

### Creating an animation resource
- [static func generate(with: any AnimationDefinition) throws -> AnimationResource](animationresource/generate(with:).md)
  Creates an animation resource from a definition.
- [static func sequence(with: [AnimationResource]) throws -> AnimationResource](animationresource/sequence(with:).md)
  Creates an animation resource that plays a collection of animations in a specified sequence.
- [static func group(with: [AnimationResource]) throws -> AnimationResource](animationresource/group(with:).md)
  Creates an animation resource that simultaneously plays back a collection of animations.
- [func `repeat`(count: Int) -> AnimationResource](animationresource/repeat(count:).md)
  Creates an animation that repeats the specified number of times.
- [func `repeat`(duration: TimeInterval) -> AnimationResource](animationresource/repeat(duration:).md)
  Repeats an animation for the specified amount of time.
### Inspecting animation information
- [let name: String?](animationresource/name.md)
  The name of the animation resource.
- [var definition: any AnimationDefinition](animationresource/definition.md)
  The timeframe, target object, and visual semantics of the animation.
- [struct AnimationFillMode](animationfillmode.md)
  Options that determine which animation frames display outside of the normal duration.
### Associating an animation with an entity
- [func store(in: Entity)](animationresource/store(in:).md)
  Adds the animation to an entity without playing it.
### Type Methods
- [static func makeActionAnimation<T>(for: T, duration: TimeInterval, name: String, bindTarget: BindTarget?, blendLayer: Int32, repeatMode: AnimationRepeatMode, fillMode: AnimationFillMode, trimStart: TimeInterval?, trimEnd: TimeInterval?, trimDuration: TimeInterval?, offset: TimeInterval, delay: TimeInterval, speed: Float) throws -> AnimationResource](animationresource/makeactionanimation(for:duration:name:bindtarget:blendlayer:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:).md)
  Creates an action animation containing a single event definition from an action.

## Relationships

### Conforms To
- [Resource](resource.md)
- [Sendable](../Swift/Sendable.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationresource)*