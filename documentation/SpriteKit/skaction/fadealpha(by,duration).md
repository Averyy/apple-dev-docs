# fadeAlpha(by:duration:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an action that adjusts the alpha value of a node by a relative value.

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
class func fadeAlpha(by factor: CGFloat, duration: TimeInterval) -> SKAction
```

```objc
+ (SKAction *) fadeAlphaBy:(CGFloat) factor duration:(NSTimeInterval) duration;
```

## Return Value

A new action object.

## Discussion

When the action executes, the node’s [`alpha`](../sknode/alpha.md) property animates to its new value.

This action is reversible; the reverse is created as if the following code is executed:

**Swift**:

```swift
let action = SKAction.fadeAlpha(by: -factor, duration: sec)
```

**Obj-C**:

```objc
[SKAction fadeAlphaBy: -factor duration: sec];
```

## Parameters

- `factor`: The amount to add to the node’s alpha value.
- `duration`: The duration of the animation.

## See Also

### Animating the Transparency of a Node
- [class func fadeIn(withDuration: TimeInterval) -> SKAction](./fadein%28withduration%29.md)
  Creates an action that changes the alpha value of the node to `1.0`.
- [class func fadeOut(withDuration: TimeInterval) -> SKAction](./fadeout%28withduration%29.md)
  Creates an action that changes the alpha value of the node to `0.0`.
- [class func fadeAlpha(to: CGFloat, duration: TimeInterval) -> SKAction](./fadealpha%28to,duration%29.md)
  Creates an action that adjusts the alpha value of a node to a new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/fadealpha(by:duration:))*