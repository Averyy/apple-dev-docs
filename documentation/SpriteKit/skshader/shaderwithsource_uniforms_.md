# shaderWithSource:uniforms:

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates a new shader object using the specified source and uniform data.

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
+ (instancetype) shaderWithSource:(NSString *) source uniforms:(NSArray<SKUniform *> *) uniforms;
```

## Return Value

A newly initialized shader object.

## Discussion

> ❗ **Important**:  Even if their source code is identical, SpriteKit treats two shaders created with [`init(source:uniforms:)`](./init%28source,uniforms%29.md) as two separate shaders. To improve the performance of multiple instances of the same fragment shader code, create [`SKShader`](../skshader.md) instances using [`init(fileNamed:)`](./init%28filenamed%29.md).

## Parameters

- `source`: A string that holds the source for a fragment shader.
- `uniforms`: A list of uniforms to add to the shader object.

## See Also

### Creating a Shader
- [Creating a Custom Fragment Shader](../creating-a-custom-fragment-shader.md)
  Write a fragment shader using the set of SpriteKit-exposed symbols, and supply it with custom data.
- [convenience init(fileNamed: String)](./init%28filenamed%29.md)
  Creates a new shader object by loading the source for a fragment shader from a file stored in the app’s bundle.
- [+ shaderWithSource:](./shaderwithsource_.md)
  Creates a new shader object using the specified source code.
- [+ shader](./shader.md)
  Creates a new empty shader object.
- [init(source: String, uniforms: [SKUniform])](./init%28source,uniforms%29.md)
  Initializes a new shader object using the specified source and uniform data.
- [init(source: String)](./init%28source%29.md)
  Initializes a new shader object using the specified source code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshader/shaderwithsource:uniforms:)*