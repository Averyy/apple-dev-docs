# start

**Framework**: GLKit  
**Kind**: property

The minimum distance in eye coordinates before fog is applied to the fragment color.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
var start: GLfloat { get set }
```

#### Discussion

This property is ignored when the [`mode`](glkeffectpropertyfog/mode.md) property is set to [`GLKFogMode.exp`](glkfogmode/exp.md) or [`GLKFogMode.exp2`](glkfogmode/exp2.md).

## See Also

- [var color: GLKVector4](glkeffectpropertyfog/color.md)
  The color of the fog at maximum density.
- [var density: GLfloat](glkeffectpropertyfog/density.md)
  The rate at which the fog exponent increases.
- [var end: GLfloat](glkeffectpropertyfog/end.md)
  The distance in eye coordinates where fog completely covers the color fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertyfog/start)*