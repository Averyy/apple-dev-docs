# speed(to:duration:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that changes how fast the node executes actions.

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
class func speed(to speed: CGFloat, duration: TimeInterval) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`speed`](sknode/speed.md) property animates to the new value.

This action is not reversible; the reverse of this action has the same duration but does not change anything.

## Parameters

- `speed`: The new value for the node’s speed.
- `duration`: The duration of the animation.

## See Also

- [class func speed(by: CGFloat, duration: TimeInterval) -> SKAction](skaction/speed(by:duration:).md)
  Creates an action that changes how fast the node executes actions by a relative value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/speed(to:duration:))*