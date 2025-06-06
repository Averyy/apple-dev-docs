# Using the Anchor Point to Move a Sprite

**Framework**: SpriteKit

Learn how the anchor point affects a sprite’s position.

#### Overview

By default, the sprite node’s frame—and thus its texture—is centered on its position. However, you might want a different part of the texture to appear at the node’s position; for example, when the game element depicted in the texture is not centered in the texture image.

A sprite node’s [`anchorPoint`](skspritenode/anchorpoint.md) determines which point within its frame corresponds to its [`position`](sknode/position.md). Anchor points are specified in the unit coordinate system, shown in the following illustration. The unit coordinate system places the origin at the bottom left corner of the frame and `(1,1)` at the top right corner of the frame. A sprite’s anchor point defaults to `(0.5,0.5)`, which corresponds to the center of the frame.

![The unit coordinate system](https://docs-assets.developer.apple.com/published/f7ba39c84ef7f3106c4ca9d54a163845/media-2983051%402x.png)

Although you are moving the frame, you do this because you want the corresponding portion of the texture to be centered on the node’s position. The following figure shows two pairs of texture images. In the first, the default anchor point centers the texture on the node position. In the second, a point at the top of the image is selected instead. You can see that when the node is rotated, the texture image rotates around this point.

![Changing a sprite node’s anchor point](https://docs-assets.developer.apple.com/published/f00395a8ab78714b59df2b6a440b83a9/media-2983050%402x.png)

The following code shows how to place the anchor point on the rocket’s nose cone. Usually, you set the anchor point when the sprite node is initialized, because it corresponds to the artwork. However, you can set this property at any time. The frame is immediately updated, and the node onscreen is updated the next time the scene is rendered.

## See Also

- [var size: CGSize](skspritenode/size.md)
  The dimensions of the sprite, in points.
- [func scale(to: CGSize)](skspritenode/scale(to:).md)
  Scales the sprite node to a specified size.
- [var anchorPoint: CGPoint](skspritenode/anchorpoint.md)
  Defines the point in the sprite that corresponds to the node’s position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/using-the-anchor-point-to-move-a-sprite)*