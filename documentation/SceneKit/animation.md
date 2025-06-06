# Animation

**Framework**: SceneKit

Create declarative animations that move elements of a scene in predetermined ways, or manage animations imported with external authoring tools.

## Topics

### First Steps
- [Animating SceneKit Content](animating-scenekit-content.md)
  Learn about implicit animations, explicit animations, and actions, and when to choose each in your app.
### Actions
- [class SCNAction](scnaction.md)
  A simple, reusable animation that changes attributes of any node you attach it to.
- [protocol SCNActionable](scnactionable.md)
  Methods for running actions on nodes.
### Implicit Animation
- [class SCNTransaction](scntransaction.md)
  A mechanism for creating implicit animations and combining scene graph changes into atomic updates.
### Explicit Animation
- [protocol SCNAnimatable](scnanimatable.md)
  The common interface for attaching animations to nodes, geometries, materials, and other SceneKit objects.
- [class SCNAnimationEvent](scnanimationevent.md)
  A container for a closure, a block in Objective-C, to be executed at a specific time during playback of an animation.
- [class SCNAnimation](scnanimation-swift.class.md)
- [class SCNAnimationPlayer](scnanimationplayer.md)
- [class SCNTimingFunction](scntimingfunction.md)
- [protocol SCNAnimationProtocol](scnanimationprotocol.md)
- [class SCNAnimation](scnanimation-swift.class.md)

## See Also

- [Constraints](constraints.md)
  Automatically adjust the position or orientation of a node based on specified rules.
- [class SCNSkinner](scnskinner.md)
  An object that manages the relationship between skeletal animations and the nodes and geometries they animate.
- [class SCNMorpher](scnmorpher.md)
  An object that manages smooth transitions between a node’s base geometry and one or more target geometries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/animation)*