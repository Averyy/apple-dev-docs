# Shaping a Physics Body to Match a Node’s Graphics

**Framework**: SpriteKit  
**Role**: Article

Shape a physics body to your graphics for the right blend of collision accuracy and performance.

## Overview

In most cases, a physics body should have a size and shape that closely approximates the visual representation of the corresponding node. For example, the rocket shown below has a narrow shape that is not well represented by either a circle or a rectangle. A convex polygon shape is chosen and fitted to match the sprite’s artwork.

![Match the shape with a close representation](https://developer.apple.com/tutorials/images/com.apple.spritekit/media-2984898@2x.png)

### Shape a Physics Body Using a Texture’s Alpha Channel

If you do not want to create your own shapes, you can use SpriteKit to create a shape for you based on the sprite’s texture.

**Swift**:

```swift
let sprite = SKSpriteNode(imageNamed: "Spaceship")
sprite.physicsBody = SKPhysicsBody(texture: sprite.texture!,
                                   size: sprite.texture!.size())
```

**Obj-C**:

```objc
SKSpriteNode *sprite = [SKSpriteNode spriteNodeWithImageNamed:@"Spaceship"];
sprite.physicsBody = [SKPhysicsBody bodyWithTexture:sprite.texture size:sprite.texture.size];
```

### Choose a Simple Geometric Physics Body Shape

When choosing a shape for your physics body, do not be overly precise. More complex shapes require more work to be properly simulated. For volume-based bodies, use the following guidelines:

- A circle is the most efficient shape ([`init(circleOfRadius:)`](./skphysicsbody/init%28circleofradius%29.md))
- A path-based polygon is the least efficient shape, and the computational work scales with the complexity of the polygon ([`init(polygonFrom:)`](./skphysicsbody/init%28polygonfrom%29.md))

### Use Edge-Based Physics Bodies Only When Needed

An edge-based body is more expensive to compute than a volume-based body. This is because the bodies it interacts with can potentially be on either side of an open edge or on the inside or outside of a closed shape. Use these guidelines:

- Lines and rectangles are the most efficient edge-based bodies ([`init(edgeFrom:to:)`](./skphysicsbody/init%28edgefrom,to%29.md) and [`init(edgeLoopFrom:)`](./skphysicsbody/init%28edgeloopfrom%29-8sqfy.md))
- Edge loops and edge chains are the most expensive edge-based bodies, and the computational work scales with the complexity of the path ([`init(edgeLoopFrom:)`](./skphysicsbody/init%28edgeloopfrom%29-5grxu.md) and [`init(edgeChainFrom:)`](./skphysicsbody/init%28edgechainfrom%29.md)).

## See Also

### Creating a Body from a Texture
- [init(texture: SKTexture, size: CGSize)](./skphysicsbody/init%28texture,size%29.md)
  Creates a physics body from the contents of a texture.
- [init(texture: SKTexture, alphaThreshold: Float, size: CGSize)](./skphysicsbody/init%28texture,alphathreshold,size%29.md)
  Creates a physics body from the contents of a texture, capturing only the texels that exceed a specified transparency value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/shaping-a-physics-body-to-match-a-node-s-graphics)*