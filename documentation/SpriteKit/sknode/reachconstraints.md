# reachConstraints

**Framework**: SpriteKit  
**Kind**: property

The reach constraints to apply to the node when executing a reach action.

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
@NSCopying
@MainActor var reachConstraints: SKReachConstraints? { get set }
```

#### Discussion

To use inverse kinematics, create a new [`SKReachConstraints`](skreachconstraints.md) object and assign it to this property. When a reach action calculates the new positions of this node, the possible values for this node are restricted to the constraints defined by this object. For more information on the inverse kinematic actions, see [`SKAction`](skaction.md).

## See Also

- [var constraints: [SKConstraint]?](sknode/constraints.md)
  A list of constraints to apply to the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/reachconstraints)*