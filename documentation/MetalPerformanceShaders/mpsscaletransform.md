# MPSScaleTransform

**Framework**: Metal Performance Shaders  
**Kind**: struct  
**Role**: Structure

A transform matrix for explicit resampling control with a Lanczos kernel.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct MPSScaleTransform
```

```c
typedef struct MPSScaleTransform { ... } MPSScaleTransform;
```

## Topics

### Fields
- [var scaleX: Double](./mpsscaletransform/scalex.md)
  The horizontal scale factor.
- [var scaleY: Double](./mpsscaletransform/scaley.md)
  The vertical scale factor.
- [var translateX: Double](./mpsscaletransform/translatex.md)
  The horizontal translation factor.
- [var translateY: Double](./mpsscaletransform/translatey.md)
  The vertical translation factor.
### Initializers
- [init()](./mpsscaletransform/init%28%29.md)
- [init(scaleX: Double, scaleY: Double, translateX: Double, translateY: Double)](./mpsscaletransform/init%28scalex,scaley,translatex,translatey%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Related Documentation
- [class MPSImageLanczosScale](./mpsimagelanczosscale.md)
  A filter that resizes and changes the aspect ratio of an image using Lanczos resampling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsscaletransform)*