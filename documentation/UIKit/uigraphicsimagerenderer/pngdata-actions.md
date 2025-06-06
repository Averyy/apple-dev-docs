# pngData(actions:)

**Framework**: UIKit  
**Kind**: method

Creates a PNG-encoded image from a set of drawing instructions.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func pngData(actions: (UIGraphicsImageRendererContext) -> Void) -> Data
```

#### Return Value

A [`Data`](https://developer.apple.com/documentation/Foundation/Data) object representing a PNG-encoded representation of the image created by the supplied drawing actions.

#### Discussion

You provide a set of drawing instructions as the block argument to this method, and the method returns the resulting image as a PNG-encoded [`Data`](https://developer.apple.com/documentation/Foundation/Data) object.

You can call this method repeatedly to create multiple images, each of which has identical dimensions and format.

## Parameters

- `actions`: A   block that, when invoked by the renderer, executes a set of drawing instructions to create the output image.

## See Also

- [func image(actions: (UIGraphicsImageRendererContext) -> Void) -> UIImage](uigraphicsimagerenderer/image(actions:).md)
  Creates an image from a set of drawing instructions.
- [func jpegData(withCompressionQuality: CGFloat, actions: (UIGraphicsImageRendererContext) -> Void) -> Data](uigraphicsimagerenderer/jpegdata(withcompressionquality:actions:).md)
  Creates a JPEG-encoded image from a set of drawing instructions.
- [UIGraphicsImageRenderer.DrawingActions](uigraphicsimagerenderer/drawingactions.md)
  A closure for drawing an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/pngdata(actions:))*