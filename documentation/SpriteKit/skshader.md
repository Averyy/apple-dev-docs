# SKShader

**Framework**: SpriteKit  
**Kind**: class

An object that allows you to apply a custom fragment shader.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class SKShader
```

## Mentions

- [Controlling Shape Drawing with Shaders](controlling-shape-drawing-with-shaders.md)
- [Applying Shaders to a Sprite](applying-shaders-to-a-sprite.md)
- [Executing Shaders in Metal and OpenGL](executing-shaders-in-metal-and-opengl.md)
- [Creating a Custom Fragment Shader](creating-a-custom-fragment-shader.md)
- [Customizing the Behavior of a Node](customizing-the-behavior-of-a-node.md)
- [Creating a New Node By Rendering To a Texture](creating-a-new-node-by-rendering-to-a-texture.md)
- [Getting Started with Particle Shaders](getting-started-with-particle-shaders.md)

#### Overview

An [`SKShader`](skshader.md) object holds a custom OpenGL ES fragment shader. Shader objects are used to customize the drawing behavior of many different kinds of nodes in SpriteKit.

To use a custom shader, create an [`SKShader`](skshader.md) object and provide the source for the custom fragment shader. If your shader needs to provide uniform data to the shader, create one or more [`SKUniform`](skuniform.md) objects and associate them with the shader object. If your shader needs to provide per-node data to the shader, create one or more [`SKAttribute`](skattribute.md) objects and associate them with the relevant nodes. Then, assign the shader object to the [`shader`](skspritenode/shader.md) property of any sprites that need the custom behavior.

Compiling a shader and the uniform data associated with it can be expensive. Because of this, you should:

- Initialize shader objects when your game launches, not while the game is running.
- Avoid changing the shader’s source or changing the list of uniforms or attributes while your game is running. Either of these things recompiles the shader.
- Share shader objects whenever possible. If multiple sprites need the same behavior, create one shader object and associate it with every sprite that needs that behavior. Do not create a separate shader for each sprite.

> ❗ **Important**:  [`SKShader`](skshader.md) does not support OpenGL Extensions. SpriteKit will return an error if you compile a project containing a fragment shader using extensions.

## Topics

### Creating a Shader
- [Creating a Custom Fragment Shader](creating-a-custom-fragment-shader.md)
  Write a fragment shader using the set of SpriteKit-exposed symbols, and supply it with custom data.
- [convenience init(fileNamed: String)](skshader/init(filenamed:).md)
  Creates a new shader object by loading the source for a fragment shader from a file stored in the app’s bundle.
- [init(source: String, uniforms: [SKUniform])](skshader/init(source:uniforms:).md)
  Initializes a new shader object using the specified source and uniform data.
- [init(source: String)](skshader/init(source:).md)
  Initializes a new shader object using the specified source code.
### Providing Uniform Data to a Shader
- [func addUniform(SKUniform)](skshader/adduniform(_:).md)
  Adds a uniform to the shader.
- [func removeUniformNamed(String)](skshader/removeuniformnamed(_:).md)
  Removes a uniform from the shader.
- [var uniforms: [SKUniform]](skshader/uniforms.md)
  The list of uniforms associated with the shader.
- [func uniformNamed(String) -> SKUniform?](skshader/uniformnamed(_:).md)
  Returns the uniform object corresponding to a particular uniform variable.
### Providing Attribute Data to a Shader
- [var attributes: [SKAttribute]](skshader/attributes.md)
  The list of attributes associated with the shader.
### Accessing or Setting a Shader’s Source Code
- [var source: String?](skshader/source.md)
  The source code for the shader.
### Executing Shaders in Metal and OpenGL
- [Executing Shaders in Metal and OpenGL](executing-shaders-in-metal-and-opengl.md)
  Toggle between renderers to make sure your shader code compiles in both the Metal and OpenGL environments.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class SKAttribute](skattribute.md)
  A specification for dynamic per-node data used with a custom shader.
- [class SKAttributeValue](skattributevalue.md)
  A container for dynamic shader data associated with a node.
- [class SKUniform](skuniform.md)
  A container for uniform shader data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshader)*