# unregisterImage(with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Unregisters the image with the specified image configuration details from the image asset.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func unregisterImage(with configuration: UIImage.Configuration)
```

```objc
- (void) unregisterImageWithConfiguration:(UIImageConfiguration *) configuration;
```

## Discussion

This method searches for an image whose configuration details match the information in the `configuration` parameter. The configuration details must match exactly, and must be associated with an image that you registered previously.

## Parameters

- `configuration`: An object containing the image configuration details for a previously registered image. This method matches only the contents of the object, so you don’t need to specify the same object you used at registration time.

## See Also

### Registering and unregistering images
- [func register(UIImage, with: UITraitCollection)](./register%28_,with%29-2plm5.md)
  Registers an image with the specified trait collection.
- [func register(UIImage, with: UIImage.Configuration)](./register%28_,with%29-89c5b.md)
  Registers an image with the specified image configuration details.
- [func unregister(imageWith: UITraitCollection)](./unregister%28imagewith%29.md)
  Unregisters the image with the specified trait collection from the image asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageasset/unregisterimage(with:))*