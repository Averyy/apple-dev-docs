# Adding interactivity to behaviors

**Framework**: RealityKit

Define what a behavior does by using actions.

#### Overview

Reality Composer provides many actions that you can use as building blocks when constructing a behavior’s action sequence. Common actions include moving objects in your scene, animating objects in a variety of ways, playing sounds, adding force to objects that participate in the physics simulation, and transitioning to a completely different scene. You can also call functions written in Xcode to accomplish additional tasks beyond what the built-in actions can do.

##### Move Rotate or Scale an Object From a Behavior

Behaviors can transform objects to a specific location, rotation, and scale using the Move, Rotate, Scale To action, which animates objects smoothly to a specified world position, orientation, and size. The end result of using a Move, Rotate, Scale To action is the same regardless of its targets’ starting transform values. For example, if you create a behavior with a Move, Rotate, Scale To action configured with a scale value of 0.5, all of its targeted objects end up with a scale value of 0.5, regardless of what their starting scale value was.

![Screenshot showing the Move, Rotate, Scale To action](https://docs-assets.developer.apple.com/published/b7dac6038abbd75ab7c67a65dfb8eb6e/adding-interactivity-to-behaviors-1%402x.png)

Behaviors can also transform objects relative to their starting position, orientation, and size using the Move, Rotate, Scale By action. With this action, the values you enter into the transform fields are applied to the objects’ current transform values instead of being used as absolute values. As a result, a Move, Rotate, Scale By action has a different effect when run against objects with different starting transform values. The action’s position and rotation values are added to an object’s starting position and rotation values, while its scale value is multiplied by the object’s starting scale value.

For example, a Move, Rotate, Scale By action with a Location X value of 5 cm results in each of its target objects moving 5 centimeters from its starting position along the scene’s X-axis. Similarly, configuring a Move, Rotate, Scale By action with a scale value of 0.5, and running it against an object with a starting scale value of 10.0, results in an object with a scale value of 5.0 when the action finishes. That same action run against an object with a starting scale value of 2.0, however, results in an object with a scale value of 1.0 after the behavior runs.

![Screenshot showing the Move, Rotate, Scale By action](https://docs-assets.developer.apple.com/published/1de942cd5e9a0ef7dd8cb0e4b47a0f7d/adding-interactivity-to-behaviors-2%402x.png)

With both of these actions, you can enter the move, rotate, or scale amount into the action’s text fields, or use the manipulator to make the transform changes visually in the scene. With the Behaviors pane visible and a behavior selected, clicking or tapping a Move, Rotate, Scale By or Move, Rotate, Scale To action puts the scene into interactive mode, as shown in the following figure. Interactive mode lets you use the manipulator to transform the object to the desired location, orientation, and scale. While in interactive mode, the scene view shows both the starting and ending location, orientation, and scale.

![Screenshot of a Reality Composer window with a behavior’s Move, Rotate, Scale By action selected.](https://docs-assets.developer.apple.com/published/e4b01be7d836bd7dc7c32e3b902429ff/adding-interactivity-to-behaviors-3.png)

##### Draw Attention to an Object

To draw attention to an object, use the Emphasize action, which causes one or more objects in your scene to animate in place in a variety of ways, such as shaking, flipping, jiggling, spinning, or bouncing.

##### Add Force to an Object

Behaviors can add forces to any object in your scene that participates in the physics simulation, by using the Add Force action to simulate the effects of being pushed, kicked, tossed, or blown by wind. Once you’ve selected the object or objects that the force applies to, a manipulator that represents the direction and intensity of the force to be added appears in your scene. To change the direction of the force, move the blue cone or rotate the blue ring. To change the amount of force to apply, use the Velocity slider on the action.

![Screenshot of a Reality Composer window with an Add Force action selected and showing the Add Force manipulator in the scene view.](https://docs-assets.developer.apple.com/published/76793b5bbc4b303884ab9b7a7d6b7894/adding-interactivity-to-behaviors-4.png)

##### Play Sounds From a Behavior

There are three actions that play audio files in Reality Composer scenes: Play Sound, Play Ambience, and Play Music. All three actions function similarly, but are designed for slightly different purposes:

- The  action plays a sound as if it were coming from a specific object in your scene. The volume of the sound changes based on the camera position relative to the object, and whether the camera is pointed toward or away from it. When the user is near the object, the sound plays louder, and when the user is far from the object, the sound is softer.
- The  action plays sounds anchored to your scene. These sounds track change in orientation but don’t attenuate, so the volume of an ambient sound doesn’t change based on the user’s position relative to any object in the scene. Play Ambience actions are designed for playing background noise that sounds as if it’s coming from far away.
- The  action plays sounds at a constant volume, completely independent of the user’s position and orientation, and is designed for playing background music and voice narration.

##### Transition to Another Scene

For games and complex AR experiences, you might choose to split up your app’s content into multiple scenes to keep things better organized and to reduce load time and the amount of memory required. You might, for example, choose to have a separate scene for every level in a game.

To switch to a different scene, use a Change Scene action, specifying the new scene you wish to load. To reset the current scene to its starting state, select the current scene instead of a different scene.

##### Call Code From a Behavior

To call code you’ve written in Xcode from a behavior, use the Notify action. Notify actions have a single configurable parameter called Identifier that is used to uniquely identify the notification this action sends. By default, a Notify action’s identifier is the same as the behavior name, but you can change it to any string value that makes sense for your project. Xcode’s code generation uses the identifier value to automatically create a notification that you use to respond to this action.

![Screenshot showing a closeup of a Notify action in Reality Composer’s Behaviors pane. ](https://docs-assets.developer.apple.com/published/7aef5611aba0a13e8906cf6198b43c07/adding-interactivity-to-behaviors-5%402x.png)

To write code that responds to a Notify action, first write a code function that takes an [`Entity`](entity.md) parameter. This function should contain the code that you want your behavior to call:

```swift
    func handleTapOnEntity(_ entity: Entity?) {
        guard let entity = entity else { return }        
        // Do something with entity...
    }
```

Once you have your function, you register it as the action’s `onAction` handler. Because the Notify action in the preceding figure specifies an identifier value of `Tapped`, Xcode automatically creates an action called `tapped` on the class representing its scene. Assign the new function as the generated action’s `onAction` handler to call that function whenever the behavior is triggered.

```swift
    // Register an onAction handler for the notification
    // action you created in Reality Composer
    boxAnchor.actions.tapped.onAction = handleTapOnEntity(_:)
```

## See Also

- [Bringing a Reality Composer scene to life](bringing-a-reality-composer-scene-to-life.md)
  Add animation and handle user input by using behaviors, triggers, and actions.
- [Building custom behaviors](building-custom-behaviors.md)
  Create custom behaviors to control objects in your scene.
- [Creating a Trigger](creating-a-trigger.md)
  Define when and how a behavior fires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/adding-interactivity-to-behaviors)*