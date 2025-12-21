# ALAssetsFilter

**Framework**: Assets Library  
**Kind**: class

`ALAssetsFilter` encapsulates filtering criteria to be used when retrieving assets from a group.

## Declaration

```swift
class ALAssetsFilter
```

#### Overview

> ❗ **Important**:  The Assets Library framework is deprecated as of iOS 9.0. Instead, use the Photos framework instead, which in iOS 8.0 and later provides more features and better performance for working with a user’s photo library. For more information, see `Photos`. In the Photos framework, the [`PHFetchOptions`](https://developer.apple.com/documentation/Photos/PHFetchOptions) class provides functionality for filtering requests for assets or collections.

You use filters with the [`setAssetsFilter(_:)`](alassetsgroup/setassetsfilter(_:).md) method in [`ALAssetsGroup`](alassetsgroup.md).

## Topics

### Creating Filters
- [class func allAssets() -> ALAssetsFilter!](alassetsfilter/allassets.md)
  Returns a filter that gets all assets in the assets group.
- [class func allPhotos() -> ALAssetsFilter!](alassetsfilter/allphotos.md)
  Returns a filter that gets all photos in the assets group.
- [class func allVideos() -> ALAssetsFilter!](alassetsfilter/allvideos.md)
  Returns a filter that gets all videos in the assets group.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ALAsset](alasset.md)
  An `ALAsset` object represents a photo or a video managed by the Photo application.
- [class ALAssetRepresentation](alassetrepresentation.md)
  An `ALAssetRepresentation` object encapsulates one of the representations of a given [`ALAsset`](alasset.md) object.
- [class ALAssetsGroup](alassetsgroup.md)
  An `ALAssetsGroup` object represents an ordered set of the assets managed by the Photos application. The order of the elements is the same as the user sees in the Photos application. An asset can belong to multiple assets groups.
- [class ALAssetsLibrary](alassetslibrary.md)
  An instance of `ALAssetsLibrary` provides access to the videos and photos that are under the control of the Photos application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetsfilter)*