# cgContext

**Framework**: UIKit  
**Kind**: property

The underlying Core Graphics context.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var cgContext: CGContext { get }
```

#### Discussion

Use this property to gain access to the underlying Core Graphics context when you need more drawing functionality than is offered by UIKit and `UIGraphicsRendererContext`.

For an example of how and when to use the Core Graphics context in an image renderer, see [`Using Core Graphics rendering functions`](uigraphicsimagerenderer#Using-Core-Graphics-rendering-functions.md) in [`UIGraphicsImageRenderer`](uigraphicsimagerenderer.md).

## See Also

- [var format: UIGraphicsRendererFormat](uigraphicsrenderercontext/format.md)
  The format used to create the associated graphics renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext/cgcontext)*