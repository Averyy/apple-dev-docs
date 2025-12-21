# AnimationLibraryComponent

**Framework**: RealityKit  
**Kind**: struct

A component that represents a collection of animations that an entity can play.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct AnimationLibraryComponent
```

#### Overview

You use an `AnimationLibraryComponent` to access an entity’s animation resources. You can store animations with an entity by packaging them together into a `.reality` file. You can do this with Reality Composer Pro or by building a custom tool.

##### Create an Animation Library with Reality Composer Pro

Follow these steps to create an animation library for an entity:

1. In the hierarchy view, select the entity you want to add animations to.
2. In the inspector, click Add Component and select Animation Library from the list of components.
3. Click the Add button (+) and select the USD files with animations.

![A screenshot of Reality Composer Pro showing the Animation Library in the Inspector. It contains two elements representing animations that have been added to the animation library. The animations are named walk and idle.](https://docs-assets.developer.apple.com/published/8615e96e7de1b7b88efee5c00ce42b04/realitycomposerpro-animationlibrary.jpg)

> 💡 **Tip**: See doc://com.apple.documentation/documentation/visionos/designing-realitykit-content-with-reality-composer-pro  for more details on working with components in Reality Composer Pro.

At runtime, your app can access and play the animations that the entity stores.

```swift
// Load the entity you want to animate.
let robot = try await Entity(named: "robot")

// Access the animation library associated with the entity.
let animationLibrary = robot.components[AnimationLibraryComponent.self]

// Play the walk animation.
if let walkAnimation = animationLibrary.animations["walk"] {
    robot.playAnimation(walkAnimation)
}
```

##### Create an Animation Library By Building Your Own Tool

If you need to build a custom tool to create `.reality` files, you can use RealityKit to programmatically create an animation library by following these steps:

1. Load an animation entity with [`init(named:in:)`](entity/init(named:in:).md).
2. Retrieve the entity’s animation resources from its [`availableAnimations`](entity/availableanimations.md) property.
3. Add the animations to an animation library.

The following example shows how you can set up an animation library:

```swift
// Create an empty animation library component.
var animationLibrary = AnimationLibraryComponent()

// Load the entities containing the animations.
let entityIdleAnimation = try await Entity(named: "idle")
let entityWalkAnimation = try await Entity(named: "walk")

// Assign the animations to the library by name.
animationLibrary.animations["idle"] = entityIdleAnimation.availableAnimations.first
animationLibrary.animations["walk"] = entityWalkAnimation.availableAnimations.first
```

After you configure the animation library, you can assign it to an entity and serialize the entity to a file. RealityKit packages the animations for that entity when you save it to a `.reality` file.

```swift
// Load the entity you want to animate.
let robot = try! await Entity(named: "robot")

// Assign the animation library to the entity.
robot.components.set(animationLibrary)

// Write the entity with its animations to a file.
robot.write(to: fileURL)
```

To play one of the animations in your app, create an entity from the `.reality` file and then call its [`playAnimation(_:transitionDuration:startsPaused:)`](entity/playanimation(_:transitionduration:startspaused:).md) method.

## Topics

### Creating an animation library component
- [init()](animationlibrarycomponent/init.md)
  Creates an empty animation library.
- [init(animations: [String : AnimationResource])](animationlibrarycomponent/init(animations:).md)
  Creates an animation library from a dictionary that associates an animation’s data with its name.
- [init(dictionaryLiteral: (String, AnimationResource)...)](animationlibrarycomponent/init(dictionaryliteral:).md)
  Creates an animation library from a variadic list of key-value pairs.
### Accessing animations
- [var animations: AnimationLibraryComponent.AnimationCollection](animationlibrarycomponent/animations.md)
  The collection of animations an entity can play.
- [var unkeyedResources: [AnimationResource]?](animationlibrarycomponent/unkeyedresources.md)
  The library’s animation resources that don’t have a queryable name.
- [var defaultAnimation: AnimationResource?](animationlibrarycomponent/defaultanimation.md)
  The default animation resource.
- [var defaultKey: String?](animationlibrarycomponent/defaultkey.md)
  The name of the default animation resource.
### Managing references to animations
- [func removeAll(resource: AnimationResource)](animationlibrarycomponent/removeall(resource:).md)
  Removes all the component’s references to an animation resource.
### Structures
- [AnimationLibraryComponent.AnimationCollection](animationlibrarycomponent/animationcollection.md)
  A collection of animations an entity can play.

## Relationships

### Conforms To
- [Component](component.md)
- [ExpressibleByDictionaryLiteral](../Swift/ExpressibleByDictionaryLiteral.md)

## See Also

- [class AnimationResource](animationresource.md)
  An animation for the properties of scenes or entities.
- [AnimationLibraryComponent.AnimationCollection](animationlibrarycomponent/animationcollection.md)
  A collection of animations an entity can play.
- [enum AnimationEvents](animationevents.md)
  Notable milestones that the framework signals during animation playback.
- [class AnimationPlaybackController](animationplaybackcontroller.md)
  A controller that manages animation playback.
- [enum AnimationRepeatMode](animationrepeatmode.md)
  Options that determine whether an animation replays after completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent)*