# start

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The minimum distance in eye coordinates before fog is applied to the fragment color.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var start: GLfloat { get set }
```

```objc
@property (nonatomic, assign) GLfloat start;
```

#### Discussion

This property is ignored when the [`mode`](./mode.md) property is set to [`GLKFogMode.exp`](../glkfogmode/exp.md) or [`GLKFogMode.exp2`](../glkfogmode/exp2.md).

## See Also

### Fog Properties
- [var color: GLKVector4](./color.md)
  The color of the fog at maximum density.
- [var density: GLfloat](./density.md)
  The rate at which the fog exponent increases.
- [var end: GLfloat](./end.md)
  The distance in eye coordinates where fog completely covers the color fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertyfog/start)*