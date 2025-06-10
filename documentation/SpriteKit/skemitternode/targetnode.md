# targetNode

**Framework**: SpriteKit  
**Kind**: property

The target node that renders the emitter’s particles.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
@MainActor
weak var targetNode: SKNode? { get set }
```

#### Discussion

The default value is `nil`, which means that particles are treated as if they were children of the emitter node. In future frames of animation, the particle positions are affected by the emitter node’s properties. If you specify a different target node, the initial properties of new particles are calculated based on the emitter node’s properties, but in future frames of animation the particles are treated as if they were children of the target node.

For example, assume you have an emitter node as a child of the scene node and the node is being rotated by changing its [`zRotation`](sknode/zrotation.md) property. The behavior of the emitter node changes based on the value of the target node:

- If the [`targetNode`](skemitternode/targetnode.md) property is `nil`, then the positions of both previously generated and new particles are rotated.
- If the [`targetNode`](skemitternode/targetnode.md) property points to the scene node, then new particles are adjusted when the emitter node rotates, but previously generated particles are not.

By spawning the particles inside the scene node, they have behavior independent of the emitter’s properties.

## See Also

- [Changing the Location of Particles in Your Scene](changing-the-location-of-particles-in-your-scene.md)
  Set a target node from which SpriteKit creates particles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/targetnode)*