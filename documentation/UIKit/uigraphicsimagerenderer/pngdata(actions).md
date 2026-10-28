# pngData(actions:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSData *) PNGDataWithActions:(UIGraphicsImageDrawingActions) actions;
```

## Return Value

A [`Data`](../../Foundation/data.md) object representing a PNG-encoded representation of the image created by the supplied drawing actions.

## Discussion

You provide a set of drawing instructions as the block argument to this method, and the method returns the resulting image as a PNG-encoded [`Data`](../../Foundation/data.md) object.

You can call this method repeatedly to create multiple images, each of which has identical dimensions and format.

## Parameters

- `actions`: A [`UIGraphicsImageRenderer.DrawingActions`](./drawingactions.md) block that, when invoked by the renderer, executes a set of drawing instructions to create the output image.

## See Also

### Creating images
- [func image(actions: (UIGraphicsImageRendererContext) -> Void) -> UIImage](./image%28actions%29.md)
  Creates an image from a set of drawing instructions.
- [func jpegData(withCompressionQuality: CGFloat, actions: (UIGraphicsImageRendererContext) -> Void) -> Data](./jpegdata%28withcompressionquality,actions%29.md)
  Creates a JPEG-encoded image from a set of drawing instructions.
- [UIGraphicsImageRenderer.DrawingActions](./drawingactions.md)
  A closure for drawing an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/pngdata(actions:))*