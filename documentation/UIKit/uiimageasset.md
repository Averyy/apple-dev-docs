# UIImageAsset

**Framework**: UIKit  
**Kind**: class

A container for a collection of images that represent multiple ways of describing a single piece of artwork.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class UIImageAsset
```

#### Overview

A common use case for [`UIImageAsset`](uiimageasset.md) is the grouping of multiple images of the same item at different display scales. Image asset objects aren’t assigned to instances of [`UIImage`](uiimage.md) rather; [`UIImage`](uiimage.md) provides an asset when multiple representations of an image are available. Images retrieved from image asset catalogs using the [`init(named:)`](uiimage/init(named:).md) or [`init(named:in:compatibleWith:)`](uiimage/init(named:in:compatiblewith:).md) methods automatically have an image asset object that allows access to other images from the catalog.

##### Register an Image

When you register an image with an image asset, you associate a [`UITraitCollection`](uitraitcollection.md) object with the image. The trait collection must contain the [`displayScale`](uitraitcollection/displayscale.md) and [`userInterfaceIdiom`](uitraitcollection/userinterfaceidiom.md) trait properties. If you don’t define these traits in the trait collection, the following defaults are assigned:

- [`displayScale`](uitraitcollection/displayscale.md) = `1.0`
- [`userInterfaceIdiom`](uitraitcollection/userinterfaceidiom.md) = [`UIUserInterfaceIdiom.unspecified`](uiuserinterfaceidiom/unspecified.md)

For example, if you create a trait collection that only contains a horizontal size class, the default display scale and idiom are added when the image is registered.

##### Retrieve an Image

When you retrieve or unregister an image from an image asset, you do so using the trait collection that was used to register the image. To ensure the correct image is retrieved, the trait collection used must contain the [`displayScale`](uitraitcollection/displayscale.md) and [`userInterfaceIdiom`](uitraitcollection/userinterfaceidiom.md) traits. If these traits aren’t defined in the trait collection, the following defaults are assigned:

- [`displayScale`](uitraitcollection/displayscale.md) = scale of the current device
- [`userInterfaceIdiom`](uitraitcollection/userinterfaceidiom.md) = the type of interface used on the current device

For example, if you create a trait collection that only contains a horizontal size class, the default display scale and idiom of the current device are added when searching the `UIImageAsset` for an image.

[`UIImageView`](uiimageview.md) automatically retrieves the correct image when [`traitCollectionDidChange(_:)`](uitraitenvironment/traitcollectiondidchange(_:).md) is called on it.

## Topics

### Initializing an image asset
- [init()](uiimageasset/init.md)
  Creates a new image asset object.
- [init?(coder: NSCoder)](uiimageasset/init(coder:).md)
  Creates an image asset from data in an unarchiver.
### Registering and unregistering images
- [func register(UIImage, with: UITraitCollection)](uiimageasset/register(_:with:)-2plm5.md)
  Registers an image with the specified trait collection.
- [func register(UIImage, with: UIImage.Configuration)](uiimageasset/register(_:with:)-89c5b.md)
  Registers an image with the specified image configuration details.
- [func unregister(imageWith: UITraitCollection)](uiimageasset/unregister(imagewith:).md)
  Unregisters the image with the specified trait collection from the image asset.
- [func unregisterImage(with: UIImage.Configuration)](uiimageasset/unregisterimage(with:).md)
  Unregisters the image with the specified image configuration details from the image asset.
### Retrieving an image from an image asset
- [func image(with: UITraitCollection) -> UIImage](uiimageasset/image(with:)-3dsgf.md)
  Retrieves the variant of the image that best matches the specified trait collection.
- [func image(with: UIImage.Configuration) -> UIImage](uiimageasset/image(with:)-8jdwv.md)
  Retrieves the variant of the image that best matches the specified image configuration details.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSDataAsset](nsdataasset.md)
  An object from a data set type stored in an asset catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageasset)*