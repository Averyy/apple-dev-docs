# init(source:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Initializes a new shader object using the specified source code.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(source: String)
```

```objc
- (instancetype) initWithSource:(NSString *) source;
```

#### Return Value

An initialized shader object.

## Parameters

- `source`: A string that holds the initial source for the shader.

## See Also

### Creating a Shader
- [Creating a Custom Fragment Shader](../creating-a-custom-fragment-shader.md)
  Write a fragment shader using the set of SpriteKit-exposed symbols, and supply it with custom data.
- [convenience init(fileNamed: String)](./init%28filenamed%29.md)
  Creates a new shader object by loading the source for a fragment shader from a file stored in the app’s bundle.
- [init(source: String, uniforms: [SKUniform])](./init%28source,uniforms%29.md)
  Initializes a new shader object using the specified source and uniform data.
- [+ shaderWithSource:uniforms:](./shaderwithsource_uniforms_.md)
  Creates a new shader object using the specified source and uniform data.
- [+ shaderWithSource:](./shaderwithsource_.md)
  Creates a new shader object using the specified source code.
- [+ shader](./shader.md)
  Creates a new empty shader object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshader/init(source:))*