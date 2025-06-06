# constraints

**Framework**: SpriteKit  
**Kind**: property

A list of constraints to apply to the node.

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
var constraints: [SKConstraint]? { get set }
```

#### Discussion

Assign an array of [`SKConstraint`](skconstraint.md) objects to the node. The scene processes these constraints before the scene is rendered. The constraints are processed in array order. If multiple nodes in the node tree have constraints, there is no guaranteed order that the nodes are processed in.

## See Also

- [var reachConstraints: SKReachConstraints?](sknode/reachconstraints.md)
  The reach constraints to apply to the node when executing a reach action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/constraints)*