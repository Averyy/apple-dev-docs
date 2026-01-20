# MPSScaleTransform

**Framework**: Metal Performance Shaders  
**Kind**: struct

A transform matrix for explicit resampling control with a Lanczos kernel.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MPSScaleTransform
```

## Topics

### Fields
- [var scaleX: Double](mpsscaletransform/scalex.md)
  The horizontal scale factor.
- [var scaleY: Double](mpsscaletransform/scaley.md)
  The vertical scale factor.
- [var translateX: Double](mpsscaletransform/translatex.md)
  The horizontal translation factor.
- [var translateY: Double](mpsscaletransform/translatey.md)
  The vertical translation factor.
### Initializers
- [init()](mpsscaletransform/init.md)
- [init(scaleX: Double, scaleY: Double, translateX: Double, translateY: Double)](mpsscaletransform/init(scalex:scaley:translatex:translatey:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class MPSImageLanczosScale](mpsimagelanczosscale.md)
  A filter that resizes and changes the aspect ratio of an image using Lanczos resampling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsscaletransform)*