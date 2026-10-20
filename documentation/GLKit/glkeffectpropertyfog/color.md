# color

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The color of the fog at maximum density.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var color: GLKVector4 { get set }
```

```objc
@property (nonatomic, assign) GLKVector4 color;
```

## See Also

### Fog Properties
- [var density: GLfloat](./density.md)
  The rate at which the fog exponent increases.
- [var start: GLfloat](./start.md)
  The minimum distance in eye coordinates before fog is applied to the fragment color.
- [var end: GLfloat](./end.md)
  The distance in eye coordinates where fog completely covers the color fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertyfog/color)*