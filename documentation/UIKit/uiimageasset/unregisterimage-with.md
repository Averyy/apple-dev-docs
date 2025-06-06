# unregisterImage(with:)

**Framework**: UIKit  
**Kind**: method

Unregisters the image with the specified image configuration details from the image asset.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func unregisterImage(with configuration: UIImage.Configuration)
```

#### Discussion

This method searches for an image whose configuration details match the information in the `configuration` parameter. The configuration details must match exactly, and must be associated with an image that you registered previously.

## Parameters

- `configuration`: An object containing the image configuration details for a previously registered image. This method matches only the contents of the object, so you don’t need to specify the same object you used at registration time.

## See Also

- [func register(UIImage, with: UITraitCollection)](uiimageasset/register(_:with:)-2plm5.md)
  Registers an image with the specified trait collection.
- [func register(UIImage, with: UIImage.Configuration)](uiimageasset/register(_:with:)-89c5b.md)
  Registers an image with the specified image configuration details.
- [func unregister(imageWith: UITraitCollection)](uiimageasset/unregister(imagewith:).md)
  Unregisters the image with the specified trait collection from the image asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageasset/unregisterimage(with:))*