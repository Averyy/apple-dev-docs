# targetPosition

**Framework**: SceneKit  
**Kind**: property

The desired position for the constrained node, in the scene’s world coordinate space. Animatable.

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
var targetPosition: SCNVector3 { get set }
```

#### Discussion

When you set this property, SceneKit attempts to move the end effector node (the node whose [`constraints`](scnnode/constraints.md) property references the constraint) to this position. SceneKit moves this node toward the target point by rotating it relative to its parent node (and rotating its parent and ancestor nodes, up the chain ending with the `chainRoot` node) until the node is at the target position or until it is as close to the target position as possible given the rotational limits of each joint in the chain.

Typically, you animate changes to this property’s value, creating an animation that shows the chain of nodes moving toward the new target position. See [`Animating SceneKit Content`](animating-scenekit-content.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnikconstraint/targetposition)*