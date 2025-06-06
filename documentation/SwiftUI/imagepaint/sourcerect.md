# sourceRect

**Framework**: SwiftUI  
**Kind**: property

A unit-space rectangle defining how much of the source image to draw.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var sourceRect: CGRect
```

#### Discussion

The results are undefined if this rectangle selects areas outside the `[0, 1]` range in either axis.

## See Also

- [var image: Image](imagepaint/image.md)
  The image to be drawn.
- [var scale: CGFloat](imagepaint/scale.md)
  A scale factor applied to the image while being drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/imagepaint/sourcerect)*