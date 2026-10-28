# animate(with:timePerFrame:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an action that animates changes to a sprite’s texture.

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
class func animate(with textures: [SKTexture], timePerFrame sec: TimeInterval) -> SKAction
```

```objc
+ (SKAction *) animateWithTextures:(NSArray<SKTexture *> *) textures timePerFrame:(NSTimeInterval) sec;
```

## Return Value

A new action object.

## Discussion

This action can only be executed by an [`SKSpriteNode`](../skspritenode.md) object. When the action executes, the sprite’s [`texture`](../skspritenode/texture.md) property animates through the array of textures. The sprite’s [`texture`](../skspritenode/texture.md) property is changed to the next texture in the array. The action then pauses for the specified time before continuing. The action continues until it has finished animating through all of the textures in the array. The total duration of the action is the number of textures multiplied by the frame interval.

This action is reversible; the resulting action animates through the same textures from last to first.

## Parameters

- `textures`: An array of textures to use when animating a sprite.
- `sec`: The duration, in seconds, that each texture is displayed.

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
- [class func colorize(with: UIColor, colorBlendFactor: CGFloat, duration: TimeInterval) -> SKAction](./colorize%28with,colorblendfactor,duration%29.md)
  Creates an animation that animates a sprite’s color and blend factor.
- [class func colorize(withColorBlendFactor: CGFloat, duration: TimeInterval) -> SKAction](./colorize%28withcolorblendfactor,duration%29.md)
  Creates an action that animates a sprite’s blend factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/animate(with:timeperframe:))*