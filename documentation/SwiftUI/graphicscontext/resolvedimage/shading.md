# shading

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

The value of this property defaults to [`foreground`](../shading/foreground.md) for template images, and to `nil` otherwise.

## See Also

### Getting the image properties
- [var size: CGSize](./size.md)
  The size of the image.
- [let baseline: CGFloat](./baseline.md)
  The distance from the top of the image to its baseline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/resolvedimage/shading)*