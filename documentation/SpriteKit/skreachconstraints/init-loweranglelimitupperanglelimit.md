# init(lowerAngleLimit:upperAngleLimit:)

**Framework**: SpriteKit  
**Kind**: init

Initializes a new reach constraint object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
init(lowerAngleLimit: CGFloat, upperAngleLimit: CGFloat)
```

#### Return Value

A newly initialized reach constraint.

#### Discussion

When a reach action is executed, a node’s [`zRotation`](sknode/zrotation.md) property may be changed by the action to satisfy the reach action. Any value calculated by the reach action for a node is always inside the range specified by the reach constraint attached to the node’s [`reachConstraints`](sknode/reachconstraints.md) property.

## Parameters

- `lowerAngleLimit`: The minimum angle that the node can have when it is rotated by a reach event.
- `upperAngleLimit`: The maximum angle that the node can have when it is rotated by a reach event.

## See Also

- [var lowerAngleLimit: CGFloat](skreachconstraints/loweranglelimit.md)
  The minimum angle that the node can have after it is rotated by a reach event.
- [var upperAngleLimit: CGFloat](skreachconstraints/upperanglelimit.md)
  The maximum angle that the node can have after it is rotated by a reach event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skreachconstraints/init(loweranglelimit:upperanglelimit:))*