# withHorizontallyFlippedOrientation()

**Framework**: UIKit  
**Kind**: method

Returns a new version of the image that’s a mirror of the original image.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func withHorizontallyFlippedOrientation() -> UIImage
```

#### Return Value

The new [`UIImage`](uiimage.md) object.

#### Discussion

The returned image’s [`imageOrientation`](uiimage/imageorientation.md) property contains the mirrored version of the original image’s orientation. For example, if the original orientation is [`UIImage.Orientation.left`](uiimage/orientation/left.md), the new orientation is [`UIImage.Orientation.leftMirrored`](uiimage/orientation/leftmirrored.md). This method does not affect the value of the [`flipsForRightToLeftLayoutDirection`](uiimage/flipsforrighttoleftlayoutdirection.md) property.

## See Also

- [func withConfiguration(UIImage.Configuration) -> UIImage](uiimage/withconfiguration(_:).md)
  Returns a new version of the current image, replacing the current configuration attributes with the specified attributes.
- [func applyingSymbolConfiguration(UIImage.SymbolConfiguration) -> UIImage?](uiimage/applyingsymbolconfiguration(_:).md)
  Returns a new version of the current image, applying the specified configuration attributes on top of the current attributes.
- [func imageFlippedForRightToLeftLayoutDirection() -> UIImage](uiimage/imageflippedforrighttoleftlayoutdirection.md)
  Returns a new version of the current image that flips horizontally when it’s in a right-to-left layout.
- [func withRenderingMode(UIImage.RenderingMode) -> UIImage](uiimage/withrenderingmode(_:).md)
  Returns a new version of the image that uses the specified rendering mode.
- [func withAlignmentRectInsets(UIEdgeInsets) -> UIImage](uiimage/withalignmentrectinsets(_:).md)
  Returns a new version of the image that uses the specified alignment insets.
- [func resizableImage(withCapInsets: UIEdgeInsets) -> UIImage](uiimage/resizableimage(withcapinsets:).md)
  Returns a new version of the image with the specified cap insets.
- [func resizableImage(withCapInsets: UIEdgeInsets, resizingMode: UIImage.ResizingMode) -> UIImage](uiimage/resizableimage(withcapinsets:resizingmode:).md)
  Returns a new version of the image with the specified cap insets and options.
- [func imageWithoutBaseline() -> UIImage](uiimage/imagewithoutbaseline.md)
  Creates a copy of the current image object without any baseline information.
- [func withBaselineOffset(fromBottom: CGFloat) -> UIImage](uiimage/withbaselineoffset(frombottom:).md)
  Creates a new image with a baseline at the specified offset from the bottom of the image.
- [UIImage.Configuration](uiimage/configuration-swift.class.md)
  A configuration object that contains the traits that the system uses when selecting the current image variant.
- [UIImage.SymbolConfiguration](uiimage/symbolconfiguration-swift.class.md)
  An object that contains the specific font, size, style, and weight attributes to apply to a symbol image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/withhorizontallyflippedorientation())*