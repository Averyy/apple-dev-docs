# density

**Framework**: GLKit  
**Kind**: property

The rate at which the fog exponent increases.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
var density: GLfloat { get set }
```

#### Discussion

This property is ignored when the [`mode`](glkeffectpropertyfog/mode.md) property is set to [`GLKFogMode.linear`](glkfogmode/linear.md).

## See Also

- [var color: GLKVector4](glkeffectpropertyfog/color.md)
  The color of the fog at maximum density.
- [var start: GLfloat](glkeffectpropertyfog/start.md)
  The minimum distance in eye coordinates before fog is applied to the fragment color.
- [var end: GLfloat](glkeffectpropertyfog/end.md)
  The distance in eye coordinates where fog completely covers the color fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertyfog/density)*