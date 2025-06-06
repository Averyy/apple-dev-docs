# resize(toWidth:duration:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that changes the width of a sprite to a new absolute value.

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
class func resize(toWidth width: CGFloat, duration: TimeInterval) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

This action can only be executed by an [`SKSpriteNode`](skspritenode.md) object. When the action executes, the sprite’s [`size`](skspritenode/size.md) property animates to its new value.

This action is not reversible; the reverse of this action has the same duration but does not change anything.

## Parameters

- `width`: The new width of the sprite.
- `duration`: The duration of the animation.

## See Also

- [class func resize(byWidth: CGFloat, height: CGFloat, duration: TimeInterval) -> SKAction](skaction/resize(bywidth:height:duration:).md)
  Creates an action that adjusts the size of a sprite.
- [class func resize(toHeight: CGFloat, duration: TimeInterval) -> SKAction](skaction/resize(toheight:duration:).md)
  Creates an action that changes the height of a sprite to a new absolute value.
- [class func resize(toWidth: CGFloat, height: CGFloat, duration: TimeInterval) -> SKAction](skaction/resize(towidth:height:duration:).md)
  Creates an action that changes the width and height of a sprite to a new absolute value.
- [class func setTexture(SKTexture) -> SKAction](skaction/settexture(_:).md)
  Creates an action that changes a sprite’s texture.
- [class func setTexture(SKTexture, resize: Bool) -> SKAction](skaction/settexture(_:resize:).md)
  Creates an action that changes a sprite’s texture, possibly resizing the sprite.
- [class func animate(with: [SKTexture], timePerFrame: TimeInterval) -> SKAction](skaction/animate(with:timeperframe:).md)
  Creates an action that animates changes to a sprite’s texture.
- [class func animate(with: [SKTexture], timePerFrame: TimeInterval, resize: Bool, restore: Bool) -> SKAction](skaction/animate(with:timeperframe:resize:restore:).md)
  Creates an action that animates changes to a sprite’s texture, possibly resizing the sprite.
- [class func setNormalTexture(SKTexture) -> SKAction](skaction/setnormaltexture(_:).md)
  Creates an action that changes a sprite’s normal texture.
- [class func setNormalTexture(SKTexture, resize: Bool) -> SKAction](skaction/setnormaltexture(_:resize:).md)
  Creates an action that changes a sprite’s normal texture, possibly resizing the sprite.
- [class func animate(withNormalTextures: [SKTexture], timePerFrame: TimeInterval) -> SKAction](skaction/animate(withnormaltextures:timeperframe:).md)
  Creates an action that animates changes to a sprite’s normal texture.
- [class func animate(withNormalTextures: [SKTexture], timePerFrame: TimeInterval, resize: Bool, restore: Bool) -> SKAction](skaction/animate(withnormaltextures:timeperframe:resize:restore:).md)
  Creates an action that animates changes to a sprite’s texture.
- [class func colorize(with: UIColor, colorBlendFactor: CGFloat, duration: TimeInterval) -> SKAction](skaction/colorize(with:colorblendfactor:duration:).md)
  Creates an animation that animates a sprite’s color and blend factor.
- [class func colorize(withColorBlendFactor: CGFloat, duration: TimeInterval) -> SKAction](skaction/colorize(withcolorblendfactor:duration:).md)
  Creates an action that animates a sprite’s blend factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/resize(towidth:duration:))*