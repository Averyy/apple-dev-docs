# NSDrawNinePartImage(_:_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: AppKit  
**Kind**: func

Draws a nine-part tiled image.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func NSDrawNinePartImage(_ frame: NSRect, _ topLeftCorner: NSImage?, _ topEdgeFill: NSImage?, _ topRightCorner: NSImage?, _ leftEdgeFill: NSImage?, _ centerFill: NSImage?, _ rightEdgeFill: NSImage?, _ bottomLeftCorner: NSImage?, _ bottomEdgeFill: NSImage?, _ bottomRightCorner: NSImage?, _ op: NSCompositingOperation, _ alphaFraction: CGFloat, _ flipped: Bool)
```

#### Discussion

This function is typically used to draw custom cells that are capable of being resized both vertically and horizontally. Cells of this type are comprised of four fixed-size corner images along and a set of edge and center images that are used to fill the gaps between the corners. These cells allow you to create sophisticated looking controls that can grow and shrink in any direction without distorting the control’s overall appearance.

You should prefer the use of this function over your own custom code for handling multi-part images whose size can change. This function correctly manages the subtle behaviors needed to handle resolution independence issues and to avoid visual artifacts caused by tiling the various images.

This function uses the top-left and bottom-right corner images to determine the widths and heights of the edge areas that need to be filled. If the width or height of the bottom-left and top-right images are not sized appropriately, they may be scaled to fill their corner area. Edge areas between the corners are tiled using the corresponding image. Similarly, the center area is tiled using the specified center image.

The `flipped` parameter lets you reorient the contents of each image when drawing in a flipped coordinate system. By default, images use an internal coordinate system that is not flipped. Rendering such an image in a flipped coordinate system would therefore cause the image to appear upside down. Passing [`true`](https://developer.apple.com/documentation/swift/true) for the `flipped` parameter adjusts the image’s internal coordinate system to draw it correctly in a flipped environment.

## Parameters

- `frame`: The rectangle (specified in the current coordinate system) in which to draw the images.
- `topLeftCorner`: The image to display in the top-left corner.
- `topEdgeFill`: The image used to tile the space between the   and   images.
- `topRightCorner`: The image to display in the top-right corner.
- `leftEdgeFill`: The image used to tile the space between the   and   images.
- `centerFill`: The image used to tile the center area between the other eight images.
- `rightEdgeFill`: The image used to tile the space between the   and   images.
- `bottomLeftCorner`: The image to display in the bottom-left corner.
- `bottomEdgeFill`: The image used to tile the space between the   and   images.
- `bottomRightCorner`: The image to display in the bottom-right corner.
- `op`: The compositing operation to use when rendering the images.
- `alphaFraction`: The alpha value to apply to the rendered image. This value can range between 0.0 and 1.0, with 0.0 being fully transparent and 1.0 being fully opaque.
- `flipped`: Specify   if you are drawing the images in a flipped coordinate system; otherwise, specify  .

## See Also

- [func NSDrawThreePartImage(NSRect, NSImage?, NSImage?, NSImage?, Bool, NSCompositingOperation, CGFloat, Bool)](nsdrawthreepartimage(_:_:_:_:_:_:_:_:).md)
  Draws a three-part tiled image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawninepartimage(_:_:_:_:_:_:_:_:_:_:_:_:_:))*