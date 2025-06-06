# image(with:)

**Framework**: UIKit  
**Kind**: method

Retrieves the variant of the image that best matches the specified image configuration details.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func image(with configuration: UIImage.Configuration) -> UIImage
```

#### Return Value

The image object for the specified configuration.

#### Discussion

If this method can’t locate an image that matches the specified image configuration precisely, it returns the best match available.

## Parameters

- `configuration`: The configuration details to use when determining which image to return.

## See Also

- [func image(with: UITraitCollection) -> UIImage](uiimageasset/image(with:)-3dsgf.md)
  Retrieves the variant of the image that best matches the specified trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageasset/image(with:)-8jdwv)*