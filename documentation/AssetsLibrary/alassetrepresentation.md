# ALAssetRepresentation

**Framework**: Assets Library  
**Kind**: class

An `ALAssetRepresentation` object encapsulates one of the representations of a given [`ALAsset`](alasset.md) object.

## Declaration

```swift
@interface ALAssetRepresentation : NSObject
```

#### Overview

> ❗ **Important**:  The Assets Library framework is deprecated as of iOS 9.0. Instead, use the Photos framework instead, which in iOS 8.0 and later provides more features and better performance for working with a user’s photo library. For more information, see `Photos`. In the Photos framework, the [`PHAsset`](https://developer.apple.com/documentation/Photos/PHAsset) and [`PHImageManager`](https://developer.apple.com/documentation/Photos/PHImageManager) classes provide functionality for fetching an asset’s image or video data.

A given asset in the library may have more than one representation. For example, if a camera provides RAW and JPEG versions of an image, the resulting asset will have two representations—one for the RAW file and one for the JPEG file.

## Topics

### Instance Methods
- [- CGImageWithOptions:](alassetrepresentation/cgimagewithoptions:.md)
- [- UTI](alassetrepresentation/uti.md)
- [- dimensions](alassetrepresentation/dimensions.md)
- [- filename](alassetrepresentation/filename.md)
- [- fullResolutionImage](alassetrepresentation/fullresolutionimage.md)
- [- fullScreenImage](alassetrepresentation/fullscreenimage.md)
- [- getBytes:fromOffset:length:error:](alassetrepresentation/getbytes:fromoffset:length:error:.md)
- [- metadata](alassetrepresentation/metadata.md)
- [- orientation](alassetrepresentation/orientation.md)
- [- scale](alassetrepresentation/scale.md)
- [- size](alassetrepresentation/size.md)
- [- url](alassetrepresentation/url.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)

## See Also

- [ALAsset](alasset.md)
  An `ALAsset` object represents a photo or a video managed by the Photo application.
- [ALAssetsFilter](alassetsfilter.md)
  `ALAssetsFilter` encapsulates filtering criteria to be used when retrieving assets from a group.
- [ALAssetsGroup](alassetsgroup.md)
  An `ALAssetsGroup` object represents an ordered set of the assets managed by the Photos application. The order of the elements is the same as the user sees in the Photos application. An asset can belong to multiple assets groups.
- [ALAssetsLibrary](alassetslibrary.md)
  An instance of `ALAssetsLibrary` provides access to the videos and photos that are under the control of the Photos application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation)*