# withBaselineOffset(fromBottom:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Creates a new image with a baseline at the specified offset from the bottom of the image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func withBaselineOffset(fromBottom baselineOffset: CGFloat) -> UIImage
```

```objc
- (UIImage *) imageWithBaselineOffsetFromBottom:(CGFloat) baselineOffset;
```

## Mentions

- [Configuring and displaying symbol images in your UI](../configuring-and-displaying-symbol-images-in-your-ui.md)

#### Return Value

A new image object containing the baseline information.

#### Discussion

Use this method to create an image with the specified baseline information. You might add a baseline to your custom images so that you can incorporate them into text-based layouts. You can also use this method to change the baseline information on an image.

## Parameters

- `baselineOffset`: The position of the baseline, relative to the bottom of the image. Specify this value in points, where positive values move the baseline up from the bottom of the image and negative values move the baseline down.

## See Also

### Changing the image attributes
- [func withConfiguration(UIImage.Configuration) -> UIImage](./withconfiguration%28_%29.md)
  Returns a new version of the current image, replacing the current configuration attributes with the specified attributes.
- [func applyingSymbolConfiguration(UIImage.SymbolConfiguration) -> UIImage?](./applyingsymbolconfiguration%28_%29.md)
  Returns a new version of the current image, applying the specified configuration attributes on top of the current attributes.
- [func imageFlippedForRightToLeftLayoutDirection() -> UIImage](./imageflippedforrighttoleftlayoutdirection%28%29.md)
  Returns a new version of the current image that flips horizontally when it’s in a right-to-left layout.
- [func withHorizontallyFlippedOrientation() -> UIImage](./withhorizontallyflippedorientation%28%29.md)
  Returns a new version of the image that’s a mirror of the original image.
- [func withRenderingMode(UIImage.RenderingMode) -> UIImage](./withrenderingmode%28_%29.md)
  Returns a new version of the image that uses the specified rendering mode.
- [func withAlignmentRectInsets(UIEdgeInsets) -> UIImage](./withalignmentrectinsets%28_%29.md)
  Returns a new version of the image that uses the specified alignment insets.
- [func resizableImage(withCapInsets: UIEdgeInsets) -> UIImage](./resizableimage%28withcapinsets%29.md)
  Returns a new version of the image with the specified cap insets.
- [func resizableImage(withCapInsets: UIEdgeInsets, resizingMode: UIImage.ResizingMode) -> UIImage](./resizableimage%28withcapinsets,resizingmode%29.md)
  Returns a new version of the image with the specified cap insets and options.
- [func imageWithoutBaseline() -> UIImage](./imagewithoutbaseline%28%29.md)
  Creates a copy of the current image object without any baseline information.
- [UIImage.Configuration](./configuration-swift.class.md)
  A configuration object that contains the traits that the system uses when selecting the current image variant.
- [UIImage.SymbolConfiguration](./symbolconfiguration-swift.class.md)
  An object that contains the specific font, size, style, and weight attributes to apply to a symbol image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/withbaselineoffset(frombottom:))*