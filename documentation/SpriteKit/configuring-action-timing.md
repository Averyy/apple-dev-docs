# Configuring Action Timing

**Framework**: SpriteKit

Time an action in a scene, by adding or modifying timing properties, or cancel an action.

#### Overview

By default, an action with a duration applies its changes linearly over the duration you specify. However, you can adjust the timing of actions.

##### Add or Change Properties to Adjust the Timing of an Action

These options are available:

- Use an action’s [`timingMode`](skaction/timingmode.md) property to choose a nonlinear timing mode for an animation. For example, you can have the action start quickly and then slow down over the remainder of the run (see [`SKActionTimingMode`](skactiontimingmode.md)).
- Create a custom timing function if you want finer control over an action’s timing. See [`timingFunction`](skaction/timingfunction.md).
- Speed up or slow down an animation from its default timing using an action’s `speed` property, which changes the rate at which an animation plays. A `speed` value of `1.0` is the normal rate, but if you set an action’s speed property to, for example, `2.0`, SpriteKit plays the animation twice as fast. To pause the action, set the `speed` to `0`. If you adjust the speed of an action that contains other actions (such as a group, sequence, or repeating action), the rate is applied to the actions contained within. The contained actions are also affected by their own speed property.

> **Note**:  A node’s speed property has the same effect as the action’s speed property, but the rate is applied to all actions processed by the node or any of its descendants in the scene tree.

Because there are multiple rates involved in an animation’s speed, SpriteKit finds all the rates that apply to the action and multiplies them to determine the final rate.

##### Cancel Actions That Should Be Stopped

To cancel actions that a node is running, call its [`removeAllActions()`](sknode/removeallactions().md) method. All actions are removed from the node immediately. If a removed action had a duration, any changes it already made to the node remain intact, but further changes are not executed.

## See Also

- [var duration: TimeInterval](skaction/duration.md)
  The duration required to complete an action.
- [var timingMode: SKActionTimingMode](skaction/timingmode.md)
  A setting that controls the speed curve of an animation.
- [enum SKActionTimingMode](skactiontimingmode.md)
  The modes that an action can use to adjust the apparent timing of the action.
- [var timingFunction: SKActionTimingFunction](skaction/timingfunction.md)
  A block used to customize the timing function.
- [typealias SKActionTimingFunction](skactiontimingfunction.md)
  The signature for the custom timing block.
- [var speed: CGFloat](skaction/speed.md)
  A speed factor that modifies how fast an action runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/configuring-action-timing)*