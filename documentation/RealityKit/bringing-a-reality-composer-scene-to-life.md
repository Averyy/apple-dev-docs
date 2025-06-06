# Bringing a Reality Composer scene to life

**Framework**: RealityKit

Add animation and handle user input by using behaviors, triggers, and actions.

#### Overview

Users can interact with your  scenes in a number of different ways without you having to explicitly code for them using Reality Composer’s behaviors. You can, for example, allow a user’s touch to affect objects in your scene, or let objects respond when the user moves close to them.

Reality Composer includes a number of behavior presets that let you easily add common forms of interactivity to your scene. You can also build your own custom behaviors or use a preset as a starting point for building more complex behaviors. For more information, see [`Building custom behaviors`](building-custom-behaviors.md).

##### Add a Behavior Preset

Reality Composer provides six behavior presets that simplify adding common forms of interactivity to your scenes. If any objects in your scene are selected when you add a behavior from a preset, the new behavior is automatically configured to affect the selected object or objects. This list describes each of the behavior presets:

To add a behavior preset to your scene, select the object or objects you want as the target of the behavior, tap the Behaviors button in the toolbar to bring up the Behaviors pane, then tap the plus button to reveal a popover that shows all of the available behavior presets as well as an option to create a custom behavior. Select a preset and Reality Composer adds a new behavior to your scene based on that preset. If, for example, you select an object and add the “Tap and Flip” behavior, a new behavior is added to your scene. This behavior is automatically configured so that the selected object flips over whenever a user taps it. To test the behavior, select the Play button in the toolbar, then tap the selected object.

##### Rename a Behavior

A newly added behavior is named “Behavior.” Immediately rename behaviors to reflect what they actually do. On an iOS device, press and hold the behavior’s name and select Rename from the menu that appears. On a Mac, select a behavior, and choose Rename from the Edit menu or press the Return key.

## See Also

- [Building custom behaviors](building-custom-behaviors.md)
  Create custom behaviors to control objects in your scene.
- [Creating a Trigger](creating-a-trigger.md)
  Define when and how a behavior fires.
- [Adding interactivity to behaviors](adding-interactivity-to-behaviors.md)
  Define what a behavior does by using actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bringing-a-reality-composer-scene-to-life)*