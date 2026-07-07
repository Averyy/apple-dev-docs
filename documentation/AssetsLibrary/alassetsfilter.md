# ALAssetsFilter

**Framework**: Assets Library  
**Kind**: class

`ALAssetsFilter` encapsulates filtering criteria to be used when retrieving assets from a group.

## Declaration

```swift
@interface ALAssetsFilter : NSObject
```

#### Overview

> ❗ **Important**:  The Assets Library framework is deprecated as of iOS 9.0. Instead, use the Photos framework instead, which in iOS 8.0 and later provides more features and better performance for working with a user’s photo library. For more information, see `Photos`. In the Photos framework, the [`PHFetchOptions`](https://developer.apple.com/documentation/Photos/PHFetchOptions) class provides functionality for filtering requests for assets or collections.

You use filters with the `ALAssetsGroup/setAssetsFilter(_:)` method in [`ALAssetsGroup`](alassetsgroup.md).

## Topics

### Type Methods
- [+ allAssets](alassetsfilter/allassets.md)
- [+ allPhotos](alassetsfilter/allphotos.md)
- [+ allVideos](alassetsfilter/allvideos.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)

## See Also

- [ALAsset](alasset.md)
  An `ALAsset` object represents a photo or a video managed by the Photo application.
- [ALAssetRepresentation](alassetrepresentation.md)
  An `ALAssetRepresentation` object encapsulates one of the representations of a given [`ALAsset`](alasset.md) object.
- [ALAssetsGroup](alassetsgroup.md)
  An `ALAssetsGroup` object represents an ordered set of the assets managed by the Photos application. The order of the elements is the same as the user sees in the Photos application. An asset can belong to multiple assets groups.
- [ALAssetsLibrary](alassetslibrary.md)
  An instance of `ALAssetsLibrary` provides access to the videos and photos that are under the control of the Photos application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetsfilter)*