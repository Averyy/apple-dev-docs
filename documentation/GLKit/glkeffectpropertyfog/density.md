# density

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The rate at which the fog exponent increases.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var density: GLfloat { get set }
```

```objc
@property (nonatomic, assign) GLfloat density;
```

## Discussion

This property is ignored when the [`mode`](./mode.md) property is set to [`GLKFogMode.linear`](../glkfogmode/linear.md).

## See Also

### Fog Properties
- [var color: GLKVector4](./color.md)
  The color of the fog at maximum density.
- [var start: GLfloat](./start.md)
  The minimum distance in eye coordinates before fog is applied to the fragment color.
- [var end: GLfloat](./end.md)
  The distance in eye coordinates where fog completely covers the color fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertyfog/density)*