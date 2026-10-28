# UIGraphicsImageRenderer.DrawingActions

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

A closure for drawing an image.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
typealias DrawingActions = (UIGraphicsImageRendererContext) -> Void
```

```c
typedef void (^)(UIGraphicsImageRendererContext *) UIGraphicsImageDrawingActions;
```

## Discussion

`UIGraphicsImageDrawingActions` defines a block type that takes a [`UIGraphicsImageRendererContext`](../uigraphicsimagerenderercontext.md) object as an argument and has no return value.

You provide a block of this type as an argument to the image drawing methods on [`UIGraphicsImageRenderer`](../uigraphicsimagerenderer.md). Your block should use the provided image renderer context to perform the drawing operations you want the renderer to execute.

See [Creating an image with an image renderer](../uigraphicsimagerenderer.md#Creating-an-image-with-an-image-renderer) for an example use of a `UIGraphicsImageDrawingActions` block.

## See Also

### Creating images
- [func image(actions: (UIGraphicsImageRendererContext) -> Void) -> UIImage](./image%28actions%29.md)
  Creates an image from a set of drawing instructions.
- [func jpegData(withCompressionQuality: CGFloat, actions: (UIGraphicsImageRendererContext) -> Void) -> Data](./jpegdata%28withcompressionquality,actions%29.md)
  Creates a JPEG-encoded image from a set of drawing instructions.
- [func pngData(actions: (UIGraphicsImageRendererContext) -> Void) -> Data](./pngdata%28actions%29.md)
  Creates a PNG-encoded image from a set of drawing instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/drawingactions)*