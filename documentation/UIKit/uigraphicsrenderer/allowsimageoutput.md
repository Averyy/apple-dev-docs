# allowsImageOutput

**Framework**: UIKit  
**Kind**: property

A Boolean value specifying whether the renderer can create output images.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var allowsImageOutput: Bool { get }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), this renderer can be used to generate [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) objects.

## See Also

- [var format: UIGraphicsRendererFormat](uigraphicsrenderer/format.md)
  The format used to create the graphics renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrenderer/allowsimageoutput)*