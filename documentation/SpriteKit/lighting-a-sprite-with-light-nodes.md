# Lighting a Sprite with Light Nodes

**Framework**: SpriteKit

Add lighting and shadows to your scene with light nodes.

#### Overview

You can use a sprite’s lighting properties, [`lightingBitMask`](skspritenode/lightingbitmask.md), [`shadowCastBitMask`](skspritenode/shadowcastbitmask.md) and [`shadowedBitMask`](skspritenode/shadowedbitmask.md), to apply effects such as illumination and shadow casting and receiving. These can be used in conjunction with normal mapping to simulate 3D lighting.

The following figure shows a normal mapped sprite node acting as background and two shadow casting sprite nodes (each with a rabbit texture).

The [`SKLightNode`](sklightnode.md) object’s [`categoryBitMask`](sklightnode/categorybitmask.md) matches the lighting bit mask of the background, and the lighting and shadow bit masks of the two rabbits:

```swift
// Create the background sprite node
let background = SKSpriteNode(texture: noiseTexture,
                              normalMap: noiseTexture.generatingNormalMap())
background.position = spriteKitViewController.center
background.lightingBitMask = 0b0001
scene.addChild(background)
     
let x: CGFloat = 150
let y = spriteKitViewController.scene.size.width - 150
     
// Create a light
let lightNode = SKLightNode()
lightNode.position = CGPoint(x: scene.size.width / 2, y: y)
lightNode.categoryBitMask = 0b0001
lightNode.lightColor = .white
scene.addChild(lightNode)
     
// Create two rabbit sprite nodes and assign them with both a lighting and a shadow cast bit mask.
for position in [CGPoint(x: x, y: y), CGPoint(x: y, y: y)] {
                    let rabbit = SKSpriteNode(imageNamed: "rabbit")
                    rabbit.position = position
                    spriteKitViewController.scene.addChild(rabbit)
                    rabbit.lightingBitMask = 0b0001
                    rabbit.shadowCastBitMask = 0b0001
}
```

The resulting scene shows the two rabbits casting shadows over the background (the light is rendered as a white circle). The noise texture gains a 3D look from the normal mapping:

![Shadow casting and normal mapping](https://docs-assets.developer.apple.com/published/261e62e59e1061db0683dbf9c6d3e2ef/media-2983060%402x.png)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/lighting-a-sprite-with-light-nodes)*