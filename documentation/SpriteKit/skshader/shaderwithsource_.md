# shaderWithSource:

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates a new shader object using the specified source code.

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
+ (instancetype) shaderWithSource:(NSString *) source;
```

#### Return Value

A newly initialized shader object.

## Parameters

- `source`: A string that holds the source code for a fragment shader.

## See Also

### Creating a Shader
- [Creating a Custom Fragment Shader](../creating-a-custom-fragment-shader.md)
  Write a fragment shader using the set of SpriteKit-exposed symbols, and supply it with custom data.
- [convenience init(fileNamed: String)](./init%28filenamed%29.md)
  Creates a new shader object by loading the source for a fragment shader from a file stored in the app’s bundle.
- [+ shaderWithSource:uniforms:](./shaderwithsource_uniforms_.md)
  Creates a new shader object using the specified source and uniform data.
- [+ shader](./shader.md)
  Creates a new empty shader object.
- [init(source: String, uniforms: [SKUniform])](./init%28source,uniforms%29.md)
  Initializes a new shader object using the specified source and uniform data.
- [init(source: String)](./init%28source%29.md)
  Initializes a new shader object using the specified source code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshader/shaderwithsource:)*