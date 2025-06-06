# Cropping Nodes

**Framework**: SpriteKit

Use a texture or a shape to mask pixels out of a crop node’s children.

#### Overview

A  is useful for implementing cockpit views, controls, and other game indicators, as well as any effect where a set of nodes should be drawn only inside a specific part of a scene. The following image shows how a crop node works. It uses the rocket ship art shown on the left as a mask for a sprite drawn as a child of the crop node shown on the right.

![None](https://docs-assets.developer.apple.com/published/255f9c4449360e9a0add38e18f36b6a9/media-2984794%402x.png)

The cropped area is specified using a mask. The mask is not a fixed image. The mask is rendered from a node, just like other content in SpriteKit. This means a crop node can use simple masks derived from a piece of artwork, but it can also use more sophisticated masks.

To use a crop node, add child nodes as you would for any other node. Then set the crop node’s [`maskNode`](skcropnode/masknode.md) property to point to another node. When the scene is rendered, the crop mask renders its mask node and uses the resulting mask to determine which pixels of its children should be rendered to the parent’s framebuffer.

The example code below shows a simple use of a mask. This code loads a mask image from a texture in the app bundle. A portion of the scene’s content is then rendered as children of the crop node, using the mask to prevent it from overdrawing the portion of the screen that the game uses to show controls.

```objc
SKCropNode *cropNode = [[SKCropNode alloc] init];
cropNode.maskNode = [[SKSpriteNode alloc] initWithImageNamed:@"cockpitMask"];
[cropNode addChild: sceneContentNode];
[self addChild:cropNode];
[self addChild:gameControlNodes];
```

When the crop node’s children are rendered, the mask node is first rendered and used to crop the node’s children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/cropping-nodes)*