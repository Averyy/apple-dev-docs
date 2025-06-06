# withTintColor(_:renderingMode:)

**Framework**: UIKit  
**Kind**: method

Returns a new version of the image with a tint color that uses the specified rendering mode.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func withTintColor(_ color: UIColor, renderingMode: UIImage.RenderingMode) -> UIImage
```

#### Return Value

A new version of the image that incorporates the specified tint color.

#### Discussion

For bitmap images, this method draws the background tint color followed by the image contents using the [`CGBlendMode.destinationIn`](https://developer.apple.com/documentation/CoreGraphics/CGBlendMode/destinationIn) mode. For symbol images, this method returns an image that always uses the specified tint color.

## Parameters

- `color`: The tint color to apply to the image.
- `renderingMode`: The rendering mode to assign to the returned image.

## See Also

- [func withTintColor(UIColor) -> UIImage](uiimage/withtintcolor(_:).md)
  Returns a new version of the current image with the specified tint color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/withtintcolor(_:renderingmode:))*