# Controlling Shape Drawing with Shaders

**Framework**: SpriteKit

Change a shape node’s appearance by supplying custom shader code.

#### Overview

When you want to go beyond the effects provided by a shape node’s properties, you can take full control of its stroking or filling by using the [`strokeShader`](skshapenode/strokeshader.md) and [`fillShader`](skshapenode/fillshader.md) properties, respectively. To do that, you supply custom OpenGL ES shader code embedded within a [`SKShader`](skshader.md) object. Custom shaders allow you to create custom effects, such as dashed lines and gradient strokes, and custom fills, such as checkerboards and random patterns.

##### Customize a Shape Nodes Stroke

Shape nodes have two additional stroke-related properties that extend the properties defined by [`SKShader`](skshader.md):

| Symbol declaration | Type | Description |
| --- | --- | --- |
| float u_path_length; | Uniform | The total length of the path, in points. |
| float v_path_distance; | Varying | The distance along the path, in points. |

By dividing the distance along the path by the total length of the path, you get the normalized position (between `0` and `1`) of each point along a shape node’s path and use it to construct the color of each pixel along the shape node’s stroke. The following code shows how you create a custom shader to do this:

The generated shape node looks like this:

![Shape node with graduated stroke](https://docs-assets.developer.apple.com/published/35f8287ee6831d82f4014a12c6c0af3f/media-2647280%402x.png)

Alternatively, by casting both symbols to integers and using the modulo operator, you get the same shape node with a shader that generates a dashed line, as shown in the following code:

The generated shape node looks like this:

![Shape node with dashed stroke](https://docs-assets.developer.apple.com/published/4ab86f1c90bda856996e41f7eb5fae69/media-2647282%402x.png)

##### Customize a Shape Nodes Fill

You create a custom fill for a shape node by writing shader code and embedding it within an [`SKShader`](skshader.md) object. Assigning the shader to the [`fillShader`](skshapenode/fillshader.md) property overrides the appearance that would otherwise be defined by [`fillColor`](skshapenode/fillcolor.md) and [`fillTexture`](skshapenode/filltexture.md).

The following shader code demonstrates filling a shape node with a simple checkerboard texture. Inside the shader, the variables `h` and `v` would, on their own, form horizontal and vertical stripes. The exclusive or operator, `^`, creates the checkerboard pattern from those stripes.

The generated shape node looks like this:

![Shape node with checkerboard fill](https://docs-assets.developer.apple.com/published/9a7d57d88b73855f8b577da52d571a3e/media-2647284%402x.png)

## See Also

- [var strokeShader: SKShader?](skshapenode/strokeshader.md)
  A custom shader used to determine the color of the stroked portion of the shape node.
- [var fillShader: SKShader?](skshapenode/fillshader.md)
  A custom shader used to determine the color of the filled portion of the shape node.
- [var attributeValues: [String : SKAttributeValue]](skshapenode/attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](skshapenode/setvalue(_:forattribute:).md)
  Sets an attribute value for an attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](skshapenode/value(forattributenamed:).md)
  The value of a shader attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/controlling-shape-drawing-with-shaders)*