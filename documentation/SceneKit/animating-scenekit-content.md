# Animating SceneKit Content

**Framework**: SceneKit

Learn about implicit animations, explicit animations, and actions, and when to choose each in your app.

#### Overview

SceneKit animation support is based on the Core Animation framework. (For more about Core Animation, read [`Core Animation Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514).) Several SceneKit classes define  properties, meaning that in addition to simply assigning a new value to the property, you can create animations that transition smoothly between two values of the property. For example, animating a node’s [`opacity`](scnnode/opacity.md) property fades the node’s visible content in or out. You can animate content  or .

##### Animate Content Changes Implicitly

You create an animation implicitly by changing the value of an animatable property. Implicit animation is useful when you want to quickly animate a one-time change or animate several property changes together without writing a lot of animation code.

The [`SCNTransaction`](scntransaction.md) class defines SceneKit’s architecture for scene content changes, including implicit animations: A transaction is a single atomic operation that combines multiple changes to nodes, geometries, materials, or other scene content. By default, SceneKit automatically creates a default transaction for all changes you make to a scene during one pass through the run loop.

The default transaction’s duration is zero, so the changes you make to animatable properties occur immediately. However, if you increase the transaction’s [`animationDuration`](scntransaction/animationduration.md), all changes to animatable properties automatically animate. For example, changing the animation duration in an `IBAction` method causes both the position and opacity changes in that method to animate together.

Listing 1. Implicit animation that makes a block of text fall out of the scene while fading away

##### Explicitly Create an Animation

For more complex animations, you can explicitly create an animation object and attach it to the scene element being animated. Creating an animation object also makes an animation reusable, so you can play the same animation at any time on demand or apply it to different elements of your scene.

Choose a [`CAAnimation`](https://developer.apple.com/documentation/QuartzCore/CAAnimation) subclass for the type of animation you want to create, specify the property to be animated using key-value coding, and set animation parameters. You then set the animation in motion by attaching it to one or more elements of your scene, as shown in [`Animating SceneKit Content`](animating-scenekit-content.md).

By using different Core Animation classes, you can combine or sequence several animations or create animations that interpolate a property’s value between several keyframe values. For more about creating animation objects, see [`Core Animation Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514). For more about attaching animations to SceneKit objects, see [`SCNAnimatable`](scnanimatable.md).

Listing 2. Explicit animation to vary the 3D extrusion depth of a block of text

SceneKit also uses [`CAAnimation`](https://developer.apple.com/documentation/QuartzCore/CAAnimation) objects for animations created using external 3D authoring tools and saved in scene files. For example, an artist might create a game character with animations for walking, jumping, and other actions. You incorporate these animations into your game by loading animation objects from the scene file using the [`SCNSceneSource`](scnscenesource.md) class and attaching them to the [`SCNNode`](scnnode.md) object that represents the game character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/animating-scenekit-content)*