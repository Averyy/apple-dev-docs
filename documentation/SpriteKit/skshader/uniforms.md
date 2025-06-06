# uniforms

**Framework**: SpriteKit  
**Kind**: property

The list of uniforms associated with the shader.

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
var uniforms: [SKUniform] { get set }
```

## Mentions

- [Creating a Custom Fragment Shader](creating-a-custom-fragment-shader.md)

#### Discussion

This property is not read-only, so you can also use it to provide all of the uniforms in a single operation. Each of the uniforms should be uniquely named.

## See Also

- [func addUniform(SKUniform)](skshader/adduniform(_:).md)
  Adds a uniform to the shader.
- [func removeUniformNamed(String)](skshader/removeuniformnamed(_:).md)
  Removes a uniform from the shader.
- [func uniformNamed(String) -> SKUniform?](skshader/uniformnamed(_:).md)
  Returns the uniform object corresponding to a particular uniform variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshader/uniforms)*