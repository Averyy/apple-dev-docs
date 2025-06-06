# SCNAction

**Framework**: SceneKit  
**Kind**: class

A simple, reusable animation that changes attributes of any node you attach it to.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class SCNAction
```

#### Overview

You use actions most often to change the structure and content of the [`SCNNode`](scnnode.md) object to which they are attached, but you can also use actions to make other changes to the scene. In SceneKit, actions provide an easy way to implement animated behaviors that frequently change in response to user input.

##### Working with Actions

To create an action, call the class method for the action you are interested in. Then, configure the action’s properties. Finally, to execute the action, call a node object’s [`run(_:)`](https://developer.apple.com/documentation/SpriteKit/SKNode/run(_:)) method (or a similar method from the [`SCNActionable`](scnactionable.md) protocol) and pass it the action object.

Most actions allow you to change a node’s properties, such as its position, rotation, or scale. Many of these actions are animated by SceneKit, meaning that they change the properties of the associated node over more than one frame of animation rendered by the scene. When an action is animated, the [`duration`](scnaction/duration.md) property states how long that action takes to complete in seconds and its [`timingMode`](scnaction/timingmode.md) property defines the rate at which the animation executes. The action’s [`speed`](scnaction/speed.md) property allows you to adjust the timing of the animation by increasing or decreasing its playback speed.

Many actions can be , allowing you to create another action object that reverses the effect of that action. For example, if an action object moves a node `20` units in the positive X direction of its parent’s local coordinate space, the reversed action moves the node `20` units in the negative X direction. To create a reversed action object, call an action object’s [`reversed()`](scnaction/reversed().md) method.

Some actions include other actions as children:

- A  has multiple child actions. Each action in the sequence begins after the previous action ends.
- A  has multiple child actions. All actions stored in the group begin executing at the same time.
- A  stores a single child action. When the child action completes, it is restarted.

You can nest groups, sequences, and repeating actions. By combining actions together, you can add sophisticated behaviors to a node.

##### Using Actions for Scene Animation

Actions are easily reused, can be added and removed while running, and directly affect presented nodes. For these reasons, actions work well when your scene changes frequently in response to user input—such as when building a game. Not all elements of a scene can be animated using actions. For other kinds of animation, use implicitly animated object properties (see the [`SCNTransaction`](scntransaction.md) class) or explicitly created Core Animation objects (see the [`SCNAnimatable`](scnanimatable.md) protocol), or change the scene graph directly for each rendered frame (see the [`SCNSceneRendererDelegate`](scnscenerendererdelegate.md) protocol).

##### Subclassing Notes

You never subclass [`SCNAction`](scnaction.md) directly. Instead, create actions that call methods on arbitrary objects or execute blocks of code. See Creating Custom Actions.

## Topics

### Creating Actions That Move a Node
- [class func moveBy(x: CGFloat, y: CGFloat, z: CGFloat, duration: TimeInterval) -> SCNAction](scnaction/moveby(x:y:z:duration:).md)
  Creates an action that moves a node relative to its current position.
- [class func move(by: SCNVector3, duration: TimeInterval) -> SCNAction](scnaction/move(by:duration:).md)
  Creates an action that moves a node relative to its current position.
- [class func move(to: SCNVector3, duration: TimeInterval) -> SCNAction](scnaction/move(to:duration:).md)
  Creates an action that moves a node to a new position.
### Creating Actions That Rotate a Node
- [class func rotateBy(x: CGFloat, y: CGFloat, z: CGFloat, duration: TimeInterval) -> SCNAction](scnaction/rotateby(x:y:z:duration:).md)
  Creates an action that rotates the node in each of the three principal axes by angles relative to its current orientation.
- [class func rotateTo(x: CGFloat, y: CGFloat, z: CGFloat, duration: TimeInterval) -> SCNAction](scnaction/rotateto(x:y:z:duration:).md)
  Creates an action that rotates the node to absolute angles in each of the three principal axes.
- [class func rotateTo(x: CGFloat, y: CGFloat, z: CGFloat, duration: TimeInterval, usesShortestUnitArc: Bool) -> SCNAction](scnaction/rotateto(x:y:z:duration:usesshortestunitarc:).md)
  Creates an action that rotates the node to absolute angles in each of the three principal axes.
- [class func rotate(by: CGFloat, around: SCNVector3, duration: TimeInterval) -> SCNAction](scnaction/rotate(by:around:duration:).md)
  Creates an action that rotates the node by an angle around a specified axis.
- [class func rotate(toAxisAngle: SCNVector4, duration: TimeInterval) -> SCNAction](scnaction/rotate(toaxisangle:duration:).md)
  Creates an action that rotates the node to an absolute angle around a specified axis.
### Creating Actions That Change a Node’s Scale
- [class func scale(by: CGFloat, duration: TimeInterval) -> SCNAction](scnaction/scale(by:duration:).md)
  Creates an action that uniformly changes the scale factor of a node by a relative value.
- [class func scale(to: CGFloat, duration: TimeInterval) -> SCNAction](scnaction/scale(to:duration:).md)
  Creates an action that uniformly changes the scale factor of a node to an absolute value.
### Creating Actions That Change a Node’s Opacity
- [class func fadeIn(duration: TimeInterval) -> SCNAction](scnaction/fadein(duration:).md)
  Creates an action that changes the opacity of the node to `1.0`.
- [class func fadeOut(duration: TimeInterval) -> SCNAction](scnaction/fadeout(duration:).md)
  Creates an action that changes the opacity of the node to `0.0`.
- [class func fadeOpacity(by: CGFloat, duration: TimeInterval) -> SCNAction](scnaction/fadeopacity(by:duration:).md)
  Creates an action that adjusts the opacity of a node by a relative value.
- [class func fadeOpacity(to: CGFloat, duration: TimeInterval) -> SCNAction](scnaction/fadeopacity(to:duration:).md)
  Creates an action that adjusts the opacity of a node to a new value.
### Creating Actions That Change a Node’s Visibility
- [class func hide() -> SCNAction](scnaction/hide.md)
  Creates an action that hides a node.
- [class func unhide() -> SCNAction](scnaction/unhide.md)
  Creates an action that ensures a node is not hidden.
### Creating Actions That Remove Nodes from the Scene
- [class func removeFromParentNode() -> SCNAction](scnaction/removefromparentnode.md)
  Creates an action that removes the node from its parent.
### Creating Actions That Play Audio
- [class func playAudio(SCNAudioSource, waitForCompletion: Bool) -> SCNAction](scnaction/playaudio(_:waitforcompletion:).md)
  Creates an action that plays an audio source.
### Creating Actions That Combine or Repeat Other Actions
- [class func group([SCNAction]) -> SCNAction](scnaction/group(_:).md)
  Creates an action that runs a collection of actions in parallel.
- [class func sequence([SCNAction]) -> SCNAction](scnaction/sequence(_:).md)
  Creates an action that runs a collection of actions sequentially.
- [class func `repeat`(SCNAction, count: Int) -> SCNAction](scnaction/repeat(_:count:).md)
  Creates an action that repeats another action a specified number of times.
- [class func repeatForever(SCNAction) -> SCNAction](scnaction/repeatforever(_:).md)
  Creates an action that repeats another action forever.
### Creating Actions That Add Delays to Action Sequences
- [class func wait(duration: TimeInterval) -> SCNAction](scnaction/wait(duration:).md)
  Creates an action that idles for a specified period of time.
- [class func wait(duration: TimeInterval, withRange: TimeInterval) -> SCNAction](scnaction/wait(duration:withrange:).md)
  Creates an action that idles for a randomized period of time.
### Creating Custom Actions
- [class func run((SCNNode) -> Void) -> SCNAction](scnaction/run(_:).md)
  Creates an action that executes a block.
- [class func run((SCNNode) -> Void, queue: dispatch_queue_t) -> SCNAction](scnaction/run(_:queue:).md)
  Creates an action that executes a block on a specific dispatch queue.
- [class func customAction(duration: TimeInterval, action: (SCNNode, CGFloat) -> Void) -> SCNAction](scnaction/customaction(duration:action:).md)
  Creates an action that executes a block periodically over a specified duration.
- [class func javaScriptAction(withScript: String, duration: TimeInterval) -> SCNAction](scnaction/javascriptaction(withscript:duration:).md)
  Creates an action that executes a JavaScript script periodically over a specified duration.
### Reversing an Action
- [func reversed() -> SCNAction](scnaction/reversed.md)
  Creates an action that reverses the behavior of another action.
### Adjusting an Action’s Animation Properties
- [var duration: TimeInterval](scnaction/duration.md)
  The duration required to complete an action.
- [var speed: CGFloat](scnaction/speed.md)
  A speed factor that modifies how fast an action runs.
- [var timingMode: SCNActionTimingMode](scnaction/timingmode.md)
  The timing mode used to execute an action.
- [var timingFunction: SCNActionTimingFunction?](scnaction/timingfunction.md)
  A block SceneKit calls to determine the action’s animation timing.
### Constants
- [enum SCNActionTimingMode](scnactiontimingmode.md)
  Constants affecting the animation curve of an action, used by the [`timingMode`](scnaction/timingmode.md) property.
- [typealias SCNActionTimingFunction](scnactiontimingfunction.md)
  The signature for a block that manages animation timing, used by the [`timingFunction`](scnaction/timingfunction.md) property.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [protocol SCNActionable](scnactionable.md)
  Methods for running actions on nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction)*