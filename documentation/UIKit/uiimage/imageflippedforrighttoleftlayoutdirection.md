# imageFlippedForRightToLeftLayoutDirection()

**Framework**: UIKit  
**Kind**: method

Returns a new version of the current image that flips horizontally when it’s in a right-to-left layout.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func imageFlippedForRightToLeftLayoutDirection() -> UIImage
```

#### Return Value

The current image, prepared to flip horizontally if it’s in a right-to-left layout.

#### Discussion

Use this method to specify an image that should flip in a right-to-left layout. Note that most images do not need to flip in a right-to-left layout.

This method returns the current [`UIImage`](uiimage.md) object with the [`flipsForRightToLeftLayoutDirection`](uiimage/flipsforrighttoleftlayoutdirection.md) property set to [`true`](https://developer.apple.com/documentation/swift/true); it does  return a flipped image. When the returned image is displayed in a [`UIImageView`](uiimageview.md) object in a right-to-left layout direction (whether the layout direction is set by the system language, or because the image view’s [`semanticContentAttribute`](uiview/semanticcontentattribute.md) property is set to [`UISemanticContentAttribute.forceRightToLeft`](uisemanticcontentattribute/forcerighttoleft.md)), the image appears flipped. When the returned image is displayed in a left-to-right context, it appears unflipped.

## See Also

- [func withConfiguration(UIImage.Configuration) -> UIImage](uiimage/withconfiguration(_:).md)
  Returns a new version of the current image, replacing the current configuration attributes with the specified attributes.
- [func applyingSymbolConfiguration(UIImage.SymbolConfiguration) -> UIImage?](uiimage/applyingsymbolconfiguration(_:).md)
  Returns a new version of the current image, applying the specified configuration attributes on top of the current attributes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/imageflippedforrighttoleftlayoutdirection())*