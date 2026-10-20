# init(source:)

**Framework**: SpriteKit  
**Kind**: init

Initializes a new shader object using the specified source code.

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
init(source: String)
```

#### Return Value

An initialized shader object.

## Parameters

- `source`: A string that holds the initial source for the shader.

## See Also

- [Creating a Custom Fragment Shader](creating-a-custom-fragment-shader.md)
  Write a fragment shader using the set of SpriteKit-exposed symbols, and supply it with custom data.
- [convenience init(fileNamed: String)](skshader/init(filenamed:).md)
  Creates a new shader object by loading the source for a fragment shader from a file stored in the app’s bundle.
- [init(source: String, uniforms: [SKUniform])](skshader/init(source:uniforms:).md)
  Initializes a new shader object using the specified source and uniform data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshader/init(source:))*