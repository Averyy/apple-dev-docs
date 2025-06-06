# Assets Library

**Framework**: Assets Library  
**Kind**: module

Access the assets in a user’s media library.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

#### Overview

Use the Assets Library framework to access the pictures and videos managed by the Photos application.

> ❗ **Important**:  The Assets Library framework is deprecated as of iOS 9.0. Instead, use the [`PhotoKit`](https://developer.apple.com/documentation/PhotoKit) framework, which in iOS 8.0 and later provides more features and better performance for working with a user’s photo library.

 The Assets Library framework is deprecated as of iOS 9.0. Instead, use the [`PhotoKit`](https://developer.apple.com/documentation/PhotoKit) framework, which in iOS 8.0 and later provides more features and better performance for working with a user’s photo library.

## Topics

### Classes
- [class ALAsset](alasset.md)
  An `ALAsset` object represents a photo or a video managed by the Photo application.
- [class ALAssetRepresentation](alassetrepresentation.md)
  An `ALAssetRepresentation` object encapsulates one of the representations of a given [`ALAsset`](alasset.md) object.
- [class ALAssetsFilter](alassetsfilter.md)
  `ALAssetsFilter` encapsulates filtering criteria to be used when retrieving assets from a group.
- [class ALAssetsGroup](alassetsgroup.md)
  An `ALAssetsGroup` object represents an ordered set of the assets managed by the Photos application. The order of the elements is the same as the user sees in the Photos application. An asset can belong to multiple assets groups.
- [class ALAssetsLibrary](alassetslibrary.md)
  An instance of `ALAssetsLibrary` provides access to the videos and photos that are under the control of the Photos application.
### Reference
- [AssetsLibrary Enumerations](assetslibrary-enumerations.md)
- [AssetsLibrary Constants](assetslibrary-constants.md)
- [AssetsLibrary Data Types](assetslibrary-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AssetsLibrary)*