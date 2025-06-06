# Applying Shaders to a Sprite

**Framework**: SpriteKit

Write custom GLSL code that modifies the look of your sprite.

#### Overview

You can use the [`shader`](skspritenode/shader.md) property of a sprite node to change the appearance of a texture with a custom OpenGL ES fragment shader embedded within a [`SKShader`](skshader.md) object. Custom shaders offer almost limitless possibilities, from adding blurs and color treatments to textures to generating imagery such as random noise.

The following code shows a small custom shader which inverts the color of a texture while leaving the alpha or transparency unaffected:

The following figure illustrates the effect of the shader. The original image, on the left, has its colors inverted by the shader:

![Example of a color inverted sprite](https://docs-assets.developer.apple.com/published/76d703dd22169b7ddbe4bb0b0de38a55/media-2983067%402x.png)

## See Also

- [var shader: SKShader?](skspritenode/shader.md)
  A text file that defines code that does custom per-pixel drawing or colorization.
- [var attributeValues: [String : SKAttributeValue]](skspritenode/attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](skspritenode/setvalue(_:forattribute:).md)
  Sets an attribute value for an attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](skspritenode/value(forattributenamed:).md)
  Sets the value of a shader attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/applying-shaders-to-a-sprite)*