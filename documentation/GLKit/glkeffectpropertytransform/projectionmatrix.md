# projectionMatrix

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The matrix used to transform position coordinates from eye space to projection space.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var projectionMatrix: GLKMatrix4 { get set }
```

```objc
@property (nonatomic, assign) GLKMatrix4 projectionMatrix;
```

## Discussion

Convenience functions for creating perspective and orthographic projection matrices can be found in [GLKMatrix4](../glkmatrix4-pce.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertytransform/projectionmatrix)*