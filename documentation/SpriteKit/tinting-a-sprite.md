# Tinting a Sprite

**Framework**: SpriteKit

Provide a color and blend factor to additively color your sprite.

#### Overview

You can use the [`color`](skspritenode/color.md) and [`colorBlendFactor`](skspritenode/colorblendfactor.md) properties to colorize the texture applied to a sprite node. The color blend factor defaults to `0.0`, which indicates that the texture should be used unmodified. As you increase this number, more of the texture color is replaced with the blended color. For example, when a monster in your game takes damage, you might want to add a red tint to the character. The following code shows how you would apply a tint to the sprite.

**Swift**:

```swift
monsterSprite.color = .red
monsterSprite.colorBlendFactor = 0.5
```

**Obj-C**:

```objc
monsterSprite.color = [SKColor redColor];
monsterSprite.colorBlendFactor = 0.5;
```

![Colorizing adjusts the color of the texture](https://docs-assets.developer.apple.com/published/a0926f37fe64c298d5bc6a5dd0c6ab48/media-2983062%402x.png)

You can also animate the color and color blend factors using actions. The following code shows how to briefly tint the sprite and then return it to normal.

**Swift**:

```swift
let pulsedRed = SKAction.sequence([
    SKAction.colorize(with: .red, colorBlendFactor: 1.0, duration: 0.15),
    SKAction.wait(forDuration: 0.1),
    SKAction.colorize(withColorBlendFactor: 0.0, duration: 0.15)])
spaceship.run(pulsedRed)
```

**Obj-C**:

```objc
SKAction *pulseRed = [SKAction sequence:@[
                        [SKAction colorizeWithColor:[SKColor redColor] colorBlendFactor:1.0 duration:0.15],
                        [SKAction waitForDuration:0.1],
                        [SKAction colorizeWithColorBlendFactor:0.0 duration:0.15]]];    
 
[monsterSprite runAction: pulseRed];
```

## See Also

- [var color: UIColor](skspritenode/color.md)
  The sprite’s color.
- [var colorBlendFactor: CGFloat](skspritenode/colorblendfactor.md)
  A floating-point value that describes how the color is blended with the sprite’s texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/tinting-a-sprite)*