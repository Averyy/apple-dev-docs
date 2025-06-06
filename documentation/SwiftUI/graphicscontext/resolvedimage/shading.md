# shading

**Framework**: SwiftUI  
**Kind**: property

An optional shading to fill the image with.

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
var shading: GraphicsContext.Shading?
```

#### Discussion

The value of this property defaults to [`foreground`](graphicscontext/shading/foreground.md) for template images, and to `nil` otherwise.

## See Also

- [var size: CGSize](graphicscontext/resolvedimage/size.md)
  The size of the image.
- [let baseline: CGFloat](graphicscontext/resolvedimage/baseline.md)
  The distance from the top of the image to its baseline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/resolvedimage/shading)*