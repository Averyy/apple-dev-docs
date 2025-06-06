# init(fileNamed:)

**Framework**: SpriteKit  
**Kind**: init

Creates a new shader object by loading the source for a fragment shader from a file stored in the app’s bundle.

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
convenience init(fileNamed name: String)
```

#### Return Value

A newly initialized shader object whose initial source is loaded from the shader file.

## Parameters

- `name`: The name of the fragment shader to load. The file must be present in your app bundle with the same name and a   file extension.

## See Also

- [Creating a Custom Fragment Shader](creating-a-custom-fragment-shader.md)
  Write a fragment shader using the set of SpriteKit-exposed symbols, and supply it with custom data.
- [init(source: String, uniforms: [SKUniform])](skshader/init(source:uniforms:).md)
  Initializes a new shader object using the specified source and uniform data.
- [init(source: String)](skshader/init(source:).md)
  Initializes a new shader object using the specified source code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshader/init(filenamed:))*