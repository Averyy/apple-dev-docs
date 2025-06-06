# Getting Started with Shape Nodes

**Framework**: SpriteKit

Create a filled or stroked shape from a path object.

#### Overview

A graphics path is a collection of straight lines and curves that can define either open or closed subpaths. You can specify separate rendering behavior for the filled and stroked portion of the path. Each part can be rendered using either a solid color or a texture; if you need to render more sophisticated effects, you can also use a custom shader.

Shape nodes are useful for content that cannot be easily decomposed into simple textured sprites. They’re also useful for building and displaying debugging information on top of your game content. However, the [`SKSpriteNode`](skspritenode.md) class offers higher performance than this class, so use shape nodes sparingly.

##### Create a Shape Node

The following code demonstrates how to create a shape node. The example creates a circle with a blue interior and a white outline. The path is created and attached to the shape node’s [`path`](skshapenode/path.md) property.

You can see from the code that the shape has three essential elements:

- The interior of the shape is filled. The [`fillColor`](skshapenode/fillcolor.md) property specifies the color used to fill the interior.
- The outline of the shape is rendered as a line. The [`strokeColor`](skshapenode/strokecolor.md) and [`lineWidth`](skshapenode/linewidth.md) properties define how the line is stroked.
- A glow extends from the outline. The [`glowWidth`](skshapenode/glowwidth.md) and [`strokeColor`](skshapenode/strokecolor.md) properties define the glow.

You can disable any of these elements by setting its color to `[SKColor clearColor]`.

The shape node provides properties that let you control how the shape is blended into the framebuffer. You use these properties the same way as the properties of the [`SKSpriteNode`](skspritenode.md) class. See [`SKShapeNode`](skshapenode.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/getting-started-with-shape-nodes)*