# uniformNamed(_:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Returns the uniform object corresponding to a particular uniform variable.

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
func uniformNamed(_ name: String) -> SKUniform?
```

```objc
- (SKUniform *) uniformNamed:(NSString *) name;
```

## Return Value

The uniform object corresponding to the name, or `nil` if that uniform cannot be found.

## Parameters

- `name`: The name of the uniform to search for.

## See Also

### Providing Uniform Data to a Shader
- [func addUniform(SKUniform)](./adduniform%28_%29.md)
  Adds a uniform to the shader.
- [func removeUniformNamed(String)](./removeuniformnamed%28_%29.md)
  Removes a uniform from the shader.
- [var uniforms: [SKUniform]](./uniforms.md)
  The list of uniforms associated with the shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshader/uniformnamed(_:))*