# register(_:with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Registers an image with the specified trait collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func register(_ image: UIImage, with traitCollection: UITraitCollection)
```

```objc
- (void) registerImage:(UIImage *) image withTraitCollection:(UITraitCollection *) traitCollection;
```

#### Discussion

Each image in an image asset must have a unique set of traits. If the asset already contains a registered image with the equivalent traits, it replaces that image with the one in the `image` parameter.

> ❗ **Important**:  The trait collection must always contain an explicit value in its [`displayScale`](../uitraitcollection/displayscale.md) property. You may experience unexpected results from [`image(with:)`](./image%28with%29-3dsgf.md) if the trait collection doesn’t explicitly define the desired scale.

## Parameters

- `image`: The image you want to register with the image asset.
- `traitCollection`: The traits to associate with `image`.

## See Also

### Registering and unregistering images
- [func register(UIImage, with: UIImage.Configuration)](./register%28_,with%29-89c5b.md)
  Registers an image with the specified image configuration details.
- [func unregister(imageWith: UITraitCollection)](./unregister%28imagewith%29.md)
  Unregisters the image with the specified trait collection from the image asset.
- [func unregisterImage(with: UIImage.Configuration)](./unregisterimage%28with%29.md)
  Unregisters the image with the specified image configuration details from the image asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageasset/register(_:with:)-2plm5)*