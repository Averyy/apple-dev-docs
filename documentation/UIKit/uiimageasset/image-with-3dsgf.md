# image(with:)

**Framework**: UIKit  
**Kind**: method

Retrieves the variant of the image that best matches the specified trait collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func image(with traitCollection: UITraitCollection) -> UIImage
```

#### Return Value

The found image.

#### Discussion

If this method can’t locate an image that matches the specified trait collection precisely, it returns the best match available.

## Parameters

- `traitCollection`: The trait collection to use when determining which image to return.

## See Also

- [func image(with: UIImage.Configuration) -> UIImage](uiimageasset/image(with:)-8jdwv.md)
  Retrieves the variant of the image that best matches the specified image configuration details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageasset/image(with:)-3dsgf)*