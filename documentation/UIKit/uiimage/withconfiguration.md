# withConfiguration(_:)

**Framework**: UIKit  
**Kind**: method

Returns a new version of the current image, replacing the current configuration attributes with the specified attributes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func withConfiguration(_ configuration: UIImage.Configuration) -> UIImage
```

#### Return Value

A new version of the image object that contains the specified configuration details.

#### Discussion

This method creates a new image object, replacing the image’s current configuration with the values specified in the `configuration` parameter.

## Parameters

- `configuration`: The new configuration attributes to associate with the image.

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/withconfiguration(_:))*