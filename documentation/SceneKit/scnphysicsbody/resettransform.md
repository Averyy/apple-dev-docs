# resetTransform()

**Framework**: SceneKit  
**Kind**: method

Updates the position and orientation of a body in the physics simulation to match that of the node to which the body is attached.

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
func resetTransform()
```

#### Discussion

If you change the position or orientation of a node with an attached static or dynamic physics body, call this method afterward to ensure that the physics simulation incorporates the change. You need not call this method for kinematic bodies.

Note that dynamic and physics bodies are designed to be moved only by the physics simulation or not at all. You may use this method to move them regardless of this restriction, but at a cost to performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/resettransform())*