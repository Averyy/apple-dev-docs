# colorize(with:colorBlendFactor:duration:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an animation that animates a sprite’s color and blend factor.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
class func colorize(with color: UIColor, colorBlendFactor: CGFloat, duration: TimeInterval) -> SKAction
```

*macOS*

```swift
class func colorize(with color: NSColor, colorBlendFactor: CGFloat, duration: TimeInterval) -> SKAction
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
+ (SKAction *) colorizeWithColor:(UIColor *) color colorBlendFactor:(CGFloat) colorBlendFactor duration:(NSTimeInterval) duration;
```

*macOS*

```objc
+ (SKAction *) colorizeWithColor:(NSColor *) color colorBlendFactor:(CGFloat) colorBlendFactor duration:(NSTimeInterval) duration;
```

## Return Value

A new action object.

## Discussion

This action can only be executed by an [`SKSpriteNode`](../skspritenode.md) object. When the action executes, the sprite’s [`color`](../skspritenode/color.md) and [`colorBlendFactor`](../skspritenode/colorblendfactor.md) properties are animated to their new values.

This action is not reversible; the reverse of this action does nothing.

## Parameters

- `color`: The new color for the sprite.
- `colorBlendFactor`: The new blend factor for the sprite.
- `duration`: The duration of the animation.

## See Also

### Animating a Node’s Texture
- [class func resize(byWidth: CGFloat, height: CGFloat, duration: TimeInterval) -> SKAction](./resize%28bywidth,height,duration%29.md)
  Creates an action that adjusts the size of a sprite.
- [class func resize(toHeight: CGFloat, duration: TimeInterval) -> SKAction](./resize%28toheight,duration%29.md)
  Creates an action that changes the height of a sprite to a new absolute value.
- [class func resize(toWidth: CGFloat, duration: TimeInterval) -> SKAction](./resize%28towidth,duration%29.md)
  Creates an action that changes the width of a sprite to a new absolute value.
- [class func resize(toWidth: CGFloat, height: CGFloat, duration: TimeInterval) -> SKAction](./resize%28towidth,height,duration%29.md)
  Creates an action that changes the width and height of a sprite to a new absolute value.
- [class func setTexture(SKTexture) -> SKAction](./settexture%28_%29.md)
  Creates an action that changes a sprite’s texture.
- [class func setTexture(SKTexture, resize: Bool) -> SKAction](./settexture%28_,resize%29.md)
  Creates an action that changes a sprite’s texture, possibly resizing the sprite.
- [class func animate(with: [SKTexture], timePerFrame: TimeInterval) -> SKAction](./animate%28with,timeperframe%29.md)
  Creates an action that animates changes to a sprite’s texture.
- [class func animate(with: [SKTexture], timePerFrame: TimeInterval, resize: Bool, restore: Bool) -> SKAction](./animate%28with,timeperframe,resize,restore%29.md)
  Creates an action that animates changes to a sprite’s texture, possibly resizing the sprite.
- [class func setNormalTexture(SKTexture) -> SKAction](./setnormaltexture%28_%29.md)
  Creates an action that changes a sprite’s normal texture.
- [class func setNormalTexture(SKTexture, resize: Bool) -> SKAction](./setnormaltexture%28_,resize%29.md)
  Creates an action that changes a sprite’s normal texture, possibly resizing the sprite.
- [class func animate(withNormalTextures: [SKTexture], timePerFrame: TimeInterval) -> SKAction](./animate%28withnormaltextures,timeperframe%29.md)
  Creates an action that animates changes to a sprite’s normal texture.
- [class func animate(withNormalTextures: [SKTexture], timePerFrame: TimeInterval, resize: Bool, restore: Bool) -> SKAction](./animate%28withnormaltextures,timeperframe,resize,restore%29.md)
  Creates an action that animates changes to a sprite’s texture.
- [class func colorize(withColorBlendFactor: CGFloat, duration: TimeInterval) -> SKAction](./colorize%28withcolorblendfactor,duration%29.md)
  Creates an action that animates a sprite’s blend factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/colorize(with:colorblendfactor:duration:))*