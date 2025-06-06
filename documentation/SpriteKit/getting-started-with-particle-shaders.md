# Getting Started with Particle Shaders

**Framework**: SpriteKit

Provide custom shader code to alter a particle’s look.

#### Overview

Use the shader property of an emitter node to change the appearance of a texture with a custom OpenGL ES fragment shader embedded within an [`SKShader`](skshader.md). Custom shaders offer almost limitless possibilities, from adding blurs and color treatments to textures, to generating imagery such as random noise.

The following code shows a custom shader that renders particles with a radial gradient. The center of each particle is opaque white and the edges are transparent black.

```swift
let emitter = SKEmitterNode()
    
let radialGradientShader = SKShader(source: "void main() {" +
    "    vec2 coord = (v_tex_coord - 0.5) * 2.0;" +
    "    gl_FragColor = vec4(1.0 - length(coord));" +
    "}")  
      
emitter.shader = radialGradientShader
```

## See Also

- [var shader: SKShader?](skemitternode/shader.md)
  A custom shader used to determine how particles are rendered.
- [var attributeValues: [String : SKAttributeValue]](skemitternode/attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](skemitternode/setvalue(_:forattribute:).md)
  Sets an attribute value for an attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](skemitternode/value(forattributenamed:).md)
  Gets the value of a shader attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/getting-started-with-particle-shaders)*