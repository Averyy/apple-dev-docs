# fadeAlpha(to:duration:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that adjusts the alpha value of a node to a new value.

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
class func fadeAlpha(to alpha: CGFloat, duration: TimeInterval) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`alpha`](sknode/alpha.md) property animates to its new value.

This action is not reversible; the reverse of this action has the same duration but does not change anything.

## Parameters

- `alpha`: The new value of the node’s alpha.
- `duration`: The duration of the animation.

## See Also

- [class func fadeIn(withDuration: TimeInterval) -> SKAction](skaction/fadein(withduration:).md)
  Creates an action that changes the alpha value of the node to `1.0`.
- [class func fadeOut(withDuration: TimeInterval) -> SKAction](skaction/fadeout(withduration:).md)
  Creates an action that changes the alpha value of the node to `0.0`.
- [class func fadeAlpha(by: CGFloat, duration: TimeInterval) -> SKAction](skaction/fadealpha(by:duration:).md)
  Creates an action that adjusts the alpha value of a node by a relative value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/fadealpha(to:duration:))*