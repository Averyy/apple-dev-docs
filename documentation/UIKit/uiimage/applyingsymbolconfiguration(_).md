# applyingSymbolConfiguration(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a new version of the current image, applying the specified configuration attributes on top of the current attributes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func applyingSymbolConfiguration(_ configuration: UIImage.SymbolConfiguration) -> UIImage?
```

```objc
- (UIImage *) imageByApplyingSymbolConfiguration:(UIImageSymbolConfiguration *) configuration;
```

## Mentions

- [Configuring and displaying symbol images in your UI](../configuring-and-displaying-symbol-images-in-your-ui.md)

## Return Value

A new version of the image object that contains the merged configuration details.

## Discussion

This method creates a new image object, merging the traits of `configuration` with the new image’s traits. During the merge, this method gives precedence to explicitly set values in the `configuration` parameter. This method then replaces the current image-related attributes with the attributes in `configuration`. If an attribute in `configuration` contains an unspecified value, this method leaves the current image’s setting intact.

## Parameters

- `configuration`: The configuration attributes to apply on top of the existing attributes. Values in this object take precedence over the image’s current configuration values.

## See Also

### Changing the image attributes
- [func withConfiguration(UIImage.Configuration) -> UIImage](./withconfiguration%28_%29.md)
  Returns a new version of the current image, replacing the current configuration attributes with the specified attributes.
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
- [func withBaselineOffset(fromBottom: CGFloat) -> UIImage](./withbaselineoffset%28frombottom%29.md)
  Creates a new image with a baseline at the specified offset from the bottom of the image.
- [UIImage.Configuration](./configuration-swift.class.md)
  A configuration object that contains the traits that the system uses when selecting the current image variant.
- [UIImage.SymbolConfiguration](./symbolconfiguration-swift.class.md)
  An object that contains the specific font, size, style, and weight attributes to apply to a symbol image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/applyingsymbolconfiguration(_:))*