# useConstantColor

**Framework**: GLKit  
**Kind**: property

A Boolean value that indicates whether or not to use the constant color.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
var useConstantColor: GLboolean { get set }
```

#### Discussion

If the value is set to `GL_TRUE`, then the value stored in the [`constantColor`](glkbaseeffect/constantcolor.md) property is used as the color value for each vertex. If the value is set to `GL_FALSE`, then your application is expected to enable the [`GLKVertexAttrib.color`](glkvertexattrib/color.md) attribute and provide per-vertex color data. The default value is `GL_FALSE`.

## See Also

- [var colorMaterialEnabled: GLboolean](glkbaseeffect/colormaterialenabled.md)
  A Boolean value that indicates whether or not to use the color vertex attribute when calculating the light’s interaction with the material.
- [var constantColor: GLKVector4](glkbaseeffect/constantcolor.md)
  A constant color, used when per-vertex color data is not provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkbaseeffect/useconstantcolor)*