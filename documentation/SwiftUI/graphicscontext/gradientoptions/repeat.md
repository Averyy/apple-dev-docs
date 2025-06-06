# repeat

**Framework**: SwiftUI  
**Kind**: property

An option that repeats the gradient outside its nominal range.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var `repeat`: GraphicsContext.GradientOptions { get }
```

#### Discussion

Use this option to cause the gradient to repeat its pattern in areas that exceed the bounds of its start and end points. The repetitions use the same start and end value for each repetition.

Without this option or [`mirror`](graphicscontext/gradientoptions/mirror.md), the gradient stops at the end of its range. The [`mirror`](graphicscontext/gradientoptions/mirror.md) option takes precendence if you set both this one and that one.

## See Also

- [static var linearColor: GraphicsContext.GradientOptions](graphicscontext/gradientoptions/linearcolor.md)
  An option that interpolates between colors in a linear color space.
- [static var mirror: GraphicsContext.GradientOptions](graphicscontext/gradientoptions/mirror.md)
  An option that repeats the gradient outside its nominal range, reflecting every other instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/gradientoptions/repeat)*