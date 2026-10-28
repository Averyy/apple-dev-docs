# unregister(imageWith:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Unregisters the image with the specified trait collection from the image asset.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func unregister(imageWith traitCollection: UITraitCollection)
```

```objc
- (void) unregisterImageWithTraitCollection:(UITraitCollection *) traitCollection;
```

## Discussion

This method searches for an image whose trait collection matches the one in the `traitCollection` parameter. The traits in both collections must match exactly, and the matching trait collection must be associated with an image that you registered previously.

## Parameters

- `traitCollection`: A trait collection containing the traits for a previously registered image. This method matches only the trait values, so you don’t need to specify the same object you used at registration time.

## See Also

### Registering and unregistering images
- [func register(UIImage, with: UITraitCollection)](./register%28_,with%29-2plm5.md)
  Registers an image with the specified trait collection.
- [func register(UIImage, with: UIImage.Configuration)](./register%28_,with%29-89c5b.md)
  Registers an image with the specified image configuration details.
- [func unregisterImage(with: UIImage.Configuration)](./unregisterimage%28with%29.md)
  Unregisters the image with the specified image configuration details from the image asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageasset/unregister(imagewith:))*