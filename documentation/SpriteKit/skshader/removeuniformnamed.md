# removeUniformNamed(_:)

**Framework**: SpriteKit  
**Kind**: method

Removes a uniform from the shader.

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
func removeUniformNamed(_ name: String)
```

#### Discussion

If a uniform with that name does not exist in the shader, nothing happens.

## Parameters

- `name`: The name of the uniform to remove.

## See Also

- [func addUniform(SKUniform)](skshader/adduniform(_:).md)
  Adds a uniform to the shader.
- [var uniforms: [SKUniform]](skshader/uniforms.md)
  The list of uniforms associated with the shader.
- [func uniformNamed(String) -> SKUniform?](skshader/uniformnamed(_:).md)
  Returns the uniform object corresponding to a particular uniform variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshader/removeuniformnamed(_:))*