# ALAsset

**Framework**: Assets Library  
**Kind**: class  
**Role**: Class

An `ALAsset` object represents a photo or a video managed by the Photo application.

## Declaration

```objc
@interface ALAsset : NSObject
```

#### Overview

> ❗ **Important**:  The Assets Library framework is deprecated as of iOS 9.0. Instead, use the Photos framework instead, which in iOS 8.0 and later provides more features and better performance for working with a user’s photo library. For more information, see `Photos`.
>
> In the Photos framework, the [`PHAsset`](../Photos/phasset.md) class provides functionality for fetching and working with photo and video assets.

Assets can have multiple representations, for example a photo which was captured in RAW and JPG. Different representations of the same asset may have different dimensions.

## Topics

### Constants
- [Property Keys](./property-keys.md)
  Constants for the keys for the properties you can get from an asset.
- [Invalid Property Value](./invalid-property-value.md)
  A constant to indicate that a property accessed by `ALAsset/value(forProperty:)` is invalid.
- [Asset Types](./asset-types.md)
  Constants that specify the type of an asset.
### Instance Properties
- [editable](./alasset/editable.md)
- [originalAsset](./alasset/originalasset.md)
### Instance Methods
- [- aspectRatioThumbnail](./alasset/aspectratiothumbnail.md)
- [- defaultRepresentation](./alasset/defaultrepresentation.md)
- [- representationForUTI:](./alasset/representationforuti_.md)
- [- setImageData:metadata:completionBlock:](./alasset/setimagedata_metadata_completionblock_.md)
- [- setVideoAtPath:completionBlock:](./alasset/setvideoatpath_completionblock_.md)
- [- thumbnail](./alasset/thumbnail.md)
- [- valueForProperty:](./alasset/valueforproperty_.md)
- [- writeModifiedImageDataToSavedPhotosAlbum:metadata:completionBlock:](./alasset/writemodifiedimagedatatosavedphotosalbum_metadata_completionblock_.md)
- [- writeModifiedVideoAtPathToSavedPhotosAlbum:completionBlock:](./alasset/writemodifiedvideoatpathtosavedphotosalbum_completionblock_.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Classes
- [ALAssetRepresentation](./alassetrepresentation.md)
  An `ALAssetRepresentation` object encapsulates one of the representations of a given [`ALAsset`](./alasset.md) object.
- [ALAssetsFilter](./alassetsfilter.md)
  `ALAssetsFilter` encapsulates filtering criteria to be used when retrieving assets from a group.
- [ALAssetsGroup](./alassetsgroup.md)
  An `ALAssetsGroup` object represents an ordered set of the assets managed by the Photos application. The order of the elements is the same as the user sees in the Photos application. An asset can belong to multiple assets groups.
- [ALAssetsLibrary](./alassetslibrary.md)
  An instance of `ALAssetsLibrary` provides access to the videos and photos that are under the control of the Photos application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alasset)*