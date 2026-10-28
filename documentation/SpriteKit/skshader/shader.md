# shader

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates a new empty shader object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) shader;
```

## Return Value

A newly initialized shader object.

## Discussion

The shader is initialized without any source code or uniform data. You must assign source code to the shader before using it.

## See Also

### Creating a Shader
- [Creating a Custom Fragment Shader](../creating-a-custom-fragment-shader.md)
  Write a fragment shader using the set of SpriteKit-exposed symbols, and supply it with custom data.
- [convenience init(fileNamed: String)](./init%28filenamed%29.md)
  Creates a new shader object by loading the source for a fragment shader from a file stored in the app’s bundle.
- [+ shaderWithSource:uniforms:](./shaderwithsource_uniforms_.md)
  Creates a new shader object using the specified source and uniform data.
- [+ shaderWithSource:](./shaderwithsource_.md)
  Creates a new shader object using the specified source code.
- [init(source: String, uniforms: [SKUniform])](./init%28source,uniforms%29.md)
  Initializes a new shader object using the specified source and uniform data.
- [init(source: String)](./init%28source%29.md)
  Initializes a new shader object using the specified source code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshader/shader)*