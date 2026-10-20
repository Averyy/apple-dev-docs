# addUniform(_:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Adds a uniform to the shader.

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
func addUniform(_ uniform: SKUniform)
```

```objc
- (void) addUniform:(SKUniform *) uniform;
```

#### Discussion

The uniform variable is automatically accessible inside your shader; do not add a declaration for it in your shader’s source code. The uniform *must* be accessed in the fragment shader.

## Parameters

- `uniform`: The new uniform object to add. The uniform object’s name must not already be in use by another uniform attached to the shader.

## See Also

### Providing Uniform Data to a Shader
- [func removeUniformNamed(String)](./removeuniformnamed%28_%29.md)
  Removes a uniform from the shader.
- [var uniforms: [SKUniform]](./uniforms.md)
  The list of uniforms associated with the shader.
- [func uniformNamed(String) -> SKUniform?](./uniformnamed%28_%29.md)
  Returns the uniform object corresponding to a particular uniform variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshader/adduniform(_:))*