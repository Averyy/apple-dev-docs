# fadeOut(withDuration:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an action that changes the alpha value of the node to `0.0`.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class func fadeOut(withDuration duration: TimeInterval) -> SKAction
```

```objc
+ (SKAction *) fadeOutWithDuration:(NSTimeInterval) duration;
```

## Mentions

- [Getting Started with Actions](../getting-started-with-actions.md)

## Return Value

A new action object.

## Discussion

When the action executes, the node’s [`alpha`](../sknode/alpha.md) property animates from its current value to `0.0`. This causes the node to disappear.

This action is reversible; the reverse is created as if the following code is executed:

**Swift**:

```swift
let action = SKAction.fadeIn(withDuration: sec)
```

**Obj-C**:

```objc
[SKAction fadeInWithDuration: sec];
```

## Parameters

- `duration`: The duration of the animation.

## See Also

### Animating the Transparency of a Node
- [class func fadeIn(withDuration: TimeInterval) -> SKAction](./fadein%28withduration%29.md)
  Creates an action that changes the alpha value of the node to `1.0`.
- [class func fadeAlpha(by: CGFloat, duration: TimeInterval) -> SKAction](./fadealpha%28by,duration%29.md)
  Creates an action that adjusts the alpha value of a node by a relative value.
- [class func fadeAlpha(to: CGFloat, duration: TimeInterval) -> SKAction](./fadealpha%28to,duration%29.md)
  Creates an action that adjusts the alpha value of a node to a new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/fadeout(withduration:))*