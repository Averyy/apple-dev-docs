# NSDrawThreePartImage(_:_:_:_:_:_:_:_:)

**Framework**: AppKit  
**Kind**: func

Draws a three-part tiled image.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func NSDrawThreePartImage(_ frame: NSRect, _ startCap: NSImage?, _ centerFill: NSImage?, _ endCap: NSImage?, _ vertical: Bool, _ op: NSCompositingOperation, _ alphaFraction: CGFloat, _ flipped: Bool)
```

#### Discussion

This function is typically used to draw custom cells (such as the backgrounds for push button and slider controls) that are capable of being resized along a single axis only. Cells of this type are comprised of fixed-size end cap images and a center area that is filled by tiling the specified center image as many times as needed to fill the gap. These cells allow you to create sophisticated looking controls that can grow and shrink without distorting the control’s overall appearance.

You should prefer the use of this function over your own custom code for handling multi-part images whose size can change. This function correctly manages the subtle behaviors needed to handle resolution independence issues and to avoid visual artifacts caused by tiling the various images.

When drawing a horizontally oriented control, the images in the `startCap`, `centerFill`, and `endCap` parameters should all have the same height, and that height should match the height of the frame rectangle. If an image’s height does not match the height of the frame rectangle, it is scaled until it does match, which might yield less desirable results. For vertically oriented controls, the image widths are scaled instead of the heights.

The `flipped` parameter lets you reorient the contents of each image when drawing in a flipped coordinate system. By default, images use an internal coordinate system that is not flipped. Rendering such an image in a flipped coordinate system would therefore cause the image to appear upside down. Passing [`true`](https://developer.apple.com/documentation/Swift/true) for the `flipped` parameter adjusts the image’s internal coordinate system to draw it correctly in a flipped environment.

## Parameters

- `frame`: The rectangle (specified in the current coordinate system) in which to draw the images.
- `startCap`: For a horizontal three-part image, this is the image located at the left edge of the frame rectangle. For a vertical three-part image, this image appears at the top of the screen in an unflipped coordinate system and at the bottom of the screen in a flipped coordinate system.
- `centerFill`: The image used to tile the space between the   and   images.
- `endCap`: For a horizontal three-part image, this is the image located at the right edge of the frame rectangle. For a vertical three-part image, this image appears at the bottom of the screen in an unflipped coordinate system and at the top of the screen in a flipped coordinate system.
- `vertical`: Specify   if the images should be stacked on top of one another to create a vertically oriented element. Specify   if the images should be laid out side-by-side to create a horizontally oriented element.
- `op`: The compositing operation to use when rendering the images.
- `alphaFraction`: The alpha value to apply to the rendered image. This value can range between 0.0 and 1.0, with 0.0 being fully transparent and 1.0 being fully opaque.
- `flipped`: Specify   if you are drawing the images in a flipped coordinate system; otherwise, specify  .

## See Also

- [func NSDrawNinePartImage(NSRect, NSImage?, NSImage?, NSImage?, NSImage?, NSImage?, NSImage?, NSImage?, NSImage?, NSImage?, NSCompositingOperation, CGFloat, Bool)](nsdrawninepartimage(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Draws a nine-part tiled image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawthreepartimage(_:_:_:_:_:_:_:_:))*