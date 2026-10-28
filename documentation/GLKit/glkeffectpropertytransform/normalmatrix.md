# normalMatrix

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The matrix used to transform normal coordinates from world space to eye space.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var normalMatrix: GLKMatrix3 { get }
```

```objc
@property (nonatomic, readonly) GLKMatrix3 normalMatrix;
```

## Discussion

The normal matrix is derived from the [`modelviewMatrix`](./modelviewmatrix.md) property and is automatically calculated when needed.

## See Also

### Configuring Modelview Properties
- [var modelviewMatrix: GLKMatrix4](./modelviewmatrix.md)
  The matrix used to transform position coordinates from world space to eye space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertytransform/normalmatrix)*