# fadeOut(withDuration:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that changes the alpha value of the node to `0.0`.

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
class func fadeOut(withDuration duration: TimeInterval) -> SKAction
```

## Mentions

- [Getting Started with Actions](getting-started-with-actions.md)

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`alpha`](sknode/alpha.md) property animates from its current value to `0.0`. This causes the node to disappear.

This action is reversible; the reverse is created as if the following code is executed:

## Parameters

- `duration`: The duration of the animation.

## See Also

- [class func fadeIn(withDuration: TimeInterval) -> SKAction](skaction/fadein(withduration:).md)
  Creates an action that changes the alpha value of the node to `1.0`.
- [class func fadeAlpha(by: CGFloat, duration: TimeInterval) -> SKAction](skaction/fadealpha(by:duration:).md)
  Creates an action that adjusts the alpha value of a node by a relative value.
- [class func fadeAlpha(to: CGFloat, duration: TimeInterval) -> SKAction](skaction/fadealpha(to:duration:).md)
  Creates an action that adjusts the alpha value of a node to a new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/fadeout(withduration:))*