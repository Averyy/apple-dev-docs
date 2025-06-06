# resizableImage(withCapInsets:resizingMode:)

**Framework**: UIKit  
**Kind**: method

Returns a new version of the image with the specified cap insets and options.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func resizableImage(withCapInsets capInsets: UIEdgeInsets, resizingMode: UIImage.ResizingMode) -> UIImage
```

#### Return Value

A new image object with the specified cap insets and resizing mode.

#### Discussion

This method is exactly the same as its counterpart [`resizableImage(withCapInsets:)`](uiimage/resizableimage(withcapinsets:).md) except that the resizing mode of the new image object can be explicitly declared. You should only call this method in place of its counterpart if you specifically want your image to be resized with the [`UIImage.ResizingMode.stretch`](uiimage/resizingmode-swift.enum/stretch.md) resizing mode.

## Parameters

- `capInsets`: The values to use for the cap insets.
- `resizingMode`: The mode with which the interior of the image is resized.

## See Also

- [func withConfiguration(UIImage.Configuration) -> UIImage](uiimage/withconfiguration(_:).md)
  Returns a new version of the current image, replacing the current configuration attributes with the specified attributes.
- [func applyingSymbolConfiguration(UIImage.SymbolConfiguration) -> UIImage?](uiimage/applyingsymbolconfiguration(_:).md)
  Returns a new version of the current image, applying the specified configuration attributes on top of the current attributes.
- [func imageFlippedForRightToLeftLayoutDirection() -> UIImage](uiimage/imageflippedforrighttoleftlayoutdirection.md)
  Returns a new version of the current image that flips horizontally when it’s in a right-to-left layout.
- [func withHorizontallyFlippedOrientation() -> UIImage](uiimage/withhorizontallyflippedorientation.md)
  Returns a new version of the image that’s a mirror of the original image.
- [func withRenderingMode(UIImage.RenderingMode) -> UIImage](uiimage/withrenderingmode(_:).md)
  Returns a new version of the image that uses the specified rendering mode.
- [func withAlignmentRectInsets(UIEdgeInsets) -> UIImage](uiimage/withalignmentrectinsets(_:).md)
  Returns a new version of the image that uses the specified alignment insets.
- [func resizableImage(withCapInsets: UIEdgeInsets) -> UIImage](uiimage/resizableimage(withcapinsets:).md)
  Returns a new version of the image with the specified cap insets.
- [func imageWithoutBaseline() -> UIImage](uiimage/imagewithoutbaseline.md)
  Creates a copy of the current image object without any baseline information.
- [func withBaselineOffset(fromBottom: CGFloat) -> UIImage](uiimage/withbaselineoffset(frombottom:).md)
  Creates a new image with a baseline at the specified offset from the bottom of the image.
- [UIImage.Configuration](uiimage/configuration-swift.class.md)
  A configuration object that contains the traits that the system uses when selecting the current image variant.
- [UIImage.SymbolConfiguration](uiimage/symbolconfiguration-swift.class.md)
  An object that contains the specific font, size, style, and weight attributes to apply to a symbol image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/resizableimage(withcapinsets:resizingmode:))*