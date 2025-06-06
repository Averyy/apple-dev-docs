# withTintColor(_:)

**Framework**: UIKit  
**Kind**: method

Returns a new version of the current image with the specified tint color.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func withTintColor(_ color: UIColor) -> UIImage
```

#### Return Value

A new version of the image that incorporates the specified tint color.

#### Discussion

For bitmap images, this method draws the background tint color followed by the image contents using the [`CGBlendMode.destinationIn`](https://developer.apple.com/documentation/CoreGraphics/CGBlendMode/destinationIn) mode. For symbol images, this method returns an image that always uses the specified tint color.

The new image uses the same rendering mode as the original image.

## Parameters

- `color`: The tint color to apply to the image.

## See Also

- [func withTintColor(UIColor, renderingMode: UIImage.RenderingMode) -> UIImage](uiimage/withtintcolor(_:renderingmode:).md)
  Returns a new version of the image with a tint color that uses the specified rendering mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/withtintcolor(_:))*