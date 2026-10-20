# constantColor

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

A constant color, used when per-vertex color data is not provided.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var constantColor: GLKVector4 { get set }
```

```objc
@property (nonatomic, assign) GLKVector4 constantColor;
```

## See Also

### Configuring Color Information
- [var colorMaterialEnabled: GLboolean](./colormaterialenabled.md)
  A Boolean value that indicates whether or not to use the color vertex attribute when calculating the light’s interaction with the material.
- [var useConstantColor: GLboolean](./useconstantcolor.md)
  A Boolean value that indicates whether or not to use the constant color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkbaseeffect/constantcolor)*