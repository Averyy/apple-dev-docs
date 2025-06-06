# colorMaterialEnabled

**Framework**: GLKit  
**Kind**: property

A Boolean value that indicates whether or not to use the color vertex attribute when calculating the light’s interaction with the material.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
var colorMaterialEnabled: GLboolean { get set }
```

#### Discussion

If the value is set to `GL_TRUE`, then the color attribute provided in the vertex data is used as the material’s color when performing any lighting calculations. If the value is set to `GL_FALSE` then the colors stored in the [`material`](glkbaseeffect/material.md) property are used to light the primitive. The default value is `GL_FALSE`.

## See Also

- [var useConstantColor: GLboolean](glkbaseeffect/useconstantcolor.md)
  A Boolean value that indicates whether or not to use the constant color.
- [var constantColor: GLKVector4](glkbaseeffect/constantcolor.md)
  A constant color, used when per-vertex color data is not provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkbaseeffect/colormaterialenabled)*