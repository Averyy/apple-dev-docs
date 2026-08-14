# init(inWorldSpace:with:)

**Framework**: SceneKit  
**Kind**: init

Creates a new transform constraint.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
convenience init(inWorldSpace world: Bool, with block: @escaping (SCNNode, SCNMatrix4) -> SCNMatrix4)
```

#### Return Value

A constraint object.

#### Discussion

The `world` parameter determines the coordinate space of the transformations passed to and returned by the `block` parameter.

## Parameters

- `world`: [`true`](https://developer.apple.com/documentation/swift/true) to evaluate the constraint in the scene’s world coordinate space, or [`false`](https://developer.apple.com/documentation/swift/false) to evaluate it relative to the local coordinate space of each constrained node.
- `block`: A block to be called when Scene Kit evaluates the constraint. The block takes the following parameters: - **node**: The constrained node.
- **transform**: The constrained node’s current presentation transformation—the value of the [`transform`](scnnode/transform.md) property of the constrained node’s [`presentation`](scnnode/presentation.md) object. If the node is affected by an in-progress animation, this value reflects the currently visible state of the node during the animation (rather than its target state that will be visible when the animation completes). The block returns a transformation matrix, which Scene Kit then applies to the node. If you return the `transform` value passed to the block, your constraint has no effect on the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransformconstraint/init(inworldspace:with:))*