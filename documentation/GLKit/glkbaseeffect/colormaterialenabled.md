# colorMaterialEnabled

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether or not to use the color vertex attribute when calculating the light’s interaction with the material.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var colorMaterialEnabled: GLboolean { get set }
```

```objc
@property (nonatomic, assign) GLboolean colorMaterialEnabled;
```

## Discussion

If the value is set to `GL_TRUE`, then the color attribute provided in the vertex data is used as the material’s color when performing any lighting calculations. If the value is set to `GL_FALSE` then the colors stored in the [`material`](./material.md) property are used to light the primitive. The default value is `GL_FALSE`.

## See Also

### Configuring Color Information
- [var useConstantColor: GLboolean](./useconstantcolor.md)
  A Boolean value that indicates whether or not to use the constant color.
- [var constantColor: GLKVector4](./constantcolor.md)
  A constant color, used when per-vertex color data is not provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkbaseeffect/colormaterialenabled)*