# physicsBody

**Framework**: SceneKit  
**Kind**: property

The physics body associated with the node.

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
var physicsBody: SCNPhysicsBody? { get set }
```

#### Discussion

The default value is `nil`, specifying that the node does not participate in the physics simulation at all. If you provide a physics body, SceneKit updates the node’s position and orientation each time it processes a step of its physics simulation. For more information on SceneKit’s physics system, see [`SCNPhysicsWorld`](scnphysicsworld.md).

## See Also

- [var physicsField: SCNPhysicsField?](scnnode/physicsfield.md)
  The physics field associated with the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/physicsbody)*