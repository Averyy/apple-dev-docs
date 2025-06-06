# image(from:scale:)

**Framework**: PencilKit  
**Kind**: method

Returns an image object that contains the specified portion of the drawing.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func image(from rect: CGRect, scale: CGFloat) -> UIImage
```

#### Return Value

A new image object that contains the rendered content.

#### Discussion

This method creates a new image and renders content from the canvas into that image at the specified scale factor.

## Parameters

- `rect`: The portion of the drawing that you want to capture. Specify a rectangle in the canvas’ coordinate system.
- `scale`: The scale factor at which to create the image. Specifying scale factors greater than   creates an image with more detail. For example, you might specify a scale factor of   or   when displaying the image on a Retina display.

## See Also

- [func image(from: CGRect, scale: CGFloat) -> NSImage](pkdrawing-swift.struct/image(from:scale:)-6p3zc.md)
  Returns an image object that contains the specified portion of the drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawing-swift.struct/image(from:scale:)-220d0)*