# register(_:with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Registers an image with the specified image configuration details.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func register(_ image: UIImage, with configuration: UIImage.Configuration)
```

```objc
- (void) registerImage:(UIImage *) image withConfiguration:(UIImageConfiguration *) configuration;
```

## Discussion

Each image in an image asset must have a unique configuration. If the asset already contains a registered image with the equivalent configuration, it replaces that image with the one in the `image` parameter.

> ❗ **Important**:  The trait collection in `configuration` must always contain an explicit value in its [`displayScale`](../uitraitcollection/displayscale.md) property. You may experience unexpected results from [`image(with:)`](./image%28with%29-8jdwv.md) if the trait collection doesn’t explicitly define the desired scale.

## Parameters

- `image`: The image you want to register with the image asset.
- `configuration`: The image configuration details to associate with `image`.

## See Also

### Registering and unregistering images
- [func register(UIImage, with: UITraitCollection)](./register%28_,with%29-2plm5.md)
  Registers an image with the specified trait collection.
- [func unregister(imageWith: UITraitCollection)](./unregister%28imagewith%29.md)
  Unregisters the image with the specified trait collection from the image asset.
- [func unregisterImage(with: UIImage.Configuration)](./unregisterimage%28with%29.md)
  Unregisters the image with the specified image configuration details from the image asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageasset/register(_:with:)-89c5b)*