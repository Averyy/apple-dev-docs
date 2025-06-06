# speed(by:duration:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that changes how fast the node executes actions by a relative value.

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
class func speed(by speed: CGFloat, duration: TimeInterval) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`speed`](sknode/speed.md) property animates to the new value.

This action is reversible; the reverse is created as if the following code is executed:

## Parameters

- `speed`: The amount to add to the node’s speed.
- `duration`: The duration of the animation.

## See Also

- [class func speed(to: CGFloat, duration: TimeInterval) -> SKAction](skaction/speed(to:duration:).md)
  Creates an action that changes how fast the node executes actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/speed(by:duration:))*