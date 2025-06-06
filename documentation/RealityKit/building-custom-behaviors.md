# Building custom behaviors

**Framework**: RealityKit

Create custom behaviors to control objects in your scene.

#### Overview

Behaviors are composed of two parts: a trigger and an action sequence. A behavior’s trigger defines how and when it fires, and the action sequence defines what actually happens when it does. Common triggers include an object being tapped by the user, coming into proximity with another object in the scene, or receiving a notification sent from code. Common actions include showing, hiding, and moving objects, and playing sounds.

Behaviors give you a versatile way to add interactivity to a Reality Composer scene. To create your own new behavior, select the Custom option when adding a behavior. The behavior is added to your scene with no defined trigger or action sequence.

##### Define a Trigger

Every behavior must contain a trigger, which defines how and when that behavior fires. See [`Creating a Trigger`](creating-a-trigger.md).

##### Build an Action Sequence

A behavior’s action sequence defines what actually happens when the behavior fires. The sequence can consist of one or more actions that you configure to run sequentially or concurrently. See [`Adding interactivity to behaviors`](adding-interactivity-to-behaviors.md).

##### Add Actions

To add the first action to a sequence, tap or click the plus button next to the Action Sequence title, or in the dotted box below it, and choose one of the available actions from the popover that appears. If objects in your scene are selected when you add an action, the new action is automatically configured to affect the selected objects.

If no objects are selected when you create the action, specify the objects that you want it to affect by using the Affected Object section at the top of the action. Tap or click the Choose button to go into selection mode, then click or tap the object or objects you want the action to affect. If an object is already selected, clicking or tapping it removes it from being affected by the action. When you’re finished, press the Done button to finalize your selection.

For more information about using Reality Composer’s Actions, see [`Adding interactivity to behaviors`](adding-interactivity-to-behaviors.md).

##### Configure Multiple Actions to Run Concurrently

For many behaviors, a single action is all you’ll need, but you can also create complex action sequences by combining multiple actions in one sequence. By default, when you add another action to a sequence, it runs sequentially after the existing actions finish.

Sometimes, you want two or more actions to run at the same time instead of running one after the other. For example, you might want one object to flip at the same time that a sound plays. To make multiple actions in a sequence run concurrently, drag one of the actions onto the other. The two actions’ boxes then combine into a single larger box, as shown in the following figure, indicating that they now run at the same time. To run additional actions simultaneously, drag more actions onto the larger box. To make concurrent actions sequential again, drag individual actions outside of the joined box.

![Screenshot of a Reality Composer behavior with two actions configured to run concurrently.](https://docs-assets.developer.apple.com/published/f2e6f4fe8b95d93bad783c1f408f6d0d/building-custom-behaviors-1%402x.png)

## Topics

### Custom behaviors
- [Creating a Trigger](creating-a-trigger.md)
  Define when and how a behavior fires.
- [Adding interactivity to behaviors](adding-interactivity-to-behaviors.md)
  Define what a behavior does by using actions.

## See Also

- [Bringing a Reality Composer scene to life](bringing-a-reality-composer-scene-to-life.md)
  Add animation and handle user input by using behaviors, triggers, and actions.
- [Creating a Trigger](creating-a-trigger.md)
  Define when and how a behavior fires.
- [Adding interactivity to behaviors](adding-interactivity-to-behaviors.md)
  Define what a behavior does by using actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/building-custom-behaviors)*