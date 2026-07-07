# ALAssetsLibrary

**Framework**: Assets Library  
**Kind**: class

An instance of `ALAssetsLibrary` provides access to the videos and photos that are under the control of the Photos application.

## Declaration

```swift
@interface ALAssetsLibrary : NSObject
```

#### Overview

> ❗ **Important**:  The Assets Library framework is deprecated as of iOS 9.0. Instead, use the Photos framework instead, which in iOS 8.0 and later provides more features and better performance for working with a user’s photo library. For more information, see `Photos`. In the Photos framework, the [`PHPhotoLibrary`](https://developer.apple.com/documentation/Photos/PHPhotoLibrary) class manages access to and changes in the photo library, and class methods on the [`PHAsset`](https://developer.apple.com/documentation/Photos/PHAsset) and [`PHCollection`](https://developer.apple.com/documentation/Photos/PHCollection) classes and related classes provide functionality for finding photo and video assets.

The library includes those that are in the Saved Photos album, those coming from iTunes, and those that were directly imported into the device. You use it to retrieve the list of all asset groups and to save images and videos into the Saved Photos album.

You create an instance of `ALAssetsLibrary` using `alloc` and `init`:

```objc
ALAssetsLibrary* library = [[ALAssetsLibrary alloc] init];
```

The lifetimes of objects you get back from a library instance are tied to the lifetime of the library instance.

Many of the methods declared by `ALAssetsLibrary` take blocks for failure and success as arguments. These methods are all asynchronous because the user may need to be asked to grant access to the data.

## Topics

### Constants
- [ALAssetsGroupType](alassetsgrouptype.md)
  A bitfield to identify types of asset.
- [Types of Asset](types-of-asset.md)
  Constants to identify types of asset.
- [ALAssetOrientation](alassetorientation.md)
  Constants to indicate the orientation of an asset.
- [ALAssetsLibraryGroupsEnumerationResultsBlock](alassetslibrarygroupsenumerationresultsblock.md)
  Signature for the block executed when a match is found during enumeration using `ALAssetsLibrary/enumerateGroups(withTypes:using:failureBlock:)`.
- [ALAssetsLibraryAssetForURLResultBlock](alassetslibraryassetforurlresultblock.md)
  Signature for the block executed if the user has granted access to the caller to access the data managed by the framework in `ALAssetsLibrary/asset(for:resultBlock:failureBlock:)`.
- [ALAssetsLibraryWriteImageCompletionBlock](alassetslibrarywriteimagecompletionblock.md)
  Signature for the block executed when `ALAssetsLibrary/writeImage(toSavedPhotosAlbum:orientation:completionBlock:)` completes.
- [ALAssetsLibraryWriteVideoCompletionBlock](alassetslibrarywritevideocompletionblock.md)
  Signature for the block executed when `ALAssetsLibrary/writeVideoAtPath(toSavedPhotosAlbum:completionBlock:)` completes.
- [ALAssetsLibraryAccessFailureBlock](alassetslibraryaccessfailureblock.md)
  Signature for the block executed if the user does not grant access to the caller to access the data managed by the framework.
- [ALAssetsLibraryGroupResultBlock](alassetslibrarygroupresultblock.md)
  Signature for the block executed if the user grants access to the caller to access the data managed by the framework..
- [ALAuthorizationStatus](alauthorizationstatus.md)
  Constants to indicate authorization status.
- [Notification Keys](notification-keys.md)
  Keys used to get values from the user information dictionary of the [`ALAssetsLibraryChangedNotification`](alassetslibrarychangednotification.md) notification.
- [Error Domain](error-domain.md)
  Constant for the AssetsLibrary domain.
- [Error Codes](error-codes.md)
  AssetsLibrary-related error codes
### Notifications
- [ALAssetsLibraryChangedNotification](alassetslibrarychangednotification.md)
  Sent when the contents of the assets library have changed from under the app that is using the data.
### Instance Methods
- [- addAssetsGroupAlbumWithName:resultBlock:failureBlock:](alassetslibrary/addassetsgroupalbumwithname:resultblock:failureblock:.md)
- [- assetForURL:resultBlock:failureBlock:](alassetslibrary/assetforurl:resultblock:failureblock:.md)
- [- enumerateGroupsWithTypes:usingBlock:failureBlock:](alassetslibrary/enumerategroupswithtypes:usingblock:failureblock:.md)
- [- groupForURL:resultBlock:failureBlock:](alassetslibrary/groupforurl:resultblock:failureblock:.md)
- [- videoAtPathIsCompatibleWithSavedPhotosAlbum:](alassetslibrary/videoatpathiscompatiblewithsavedphotosalbum:.md)
- [- writeImageDataToSavedPhotosAlbum:metadata:completionBlock:](alassetslibrary/writeimagedatatosavedphotosalbum:metadata:completionblock:.md)
- [- writeImageToSavedPhotosAlbum:metadata:completionBlock:](alassetslibrary/writeimagetosavedphotosalbum:metadata:completionblock:.md)
- [- writeImageToSavedPhotosAlbum:orientation:completionBlock:](alassetslibrary/writeimagetosavedphotosalbum:orientation:completionblock:.md)
- [- writeVideoAtPathToSavedPhotosAlbum:completionBlock:](alassetslibrary/writevideoatpathtosavedphotosalbum:completionblock:.md)
### Type Methods
- [+ authorizationStatus](alassetslibrary/authorizationstatus.md)
- [+ disableSharedPhotoStreamsSupport](alassetslibrary/disablesharedphotostreamssupport.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)

## See Also

- [ALAsset](alasset.md)
  An `ALAsset` object represents a photo or a video managed by the Photo application.
- [ALAssetRepresentation](alassetrepresentation.md)
  An `ALAssetRepresentation` object encapsulates one of the representations of a given [`ALAsset`](alasset.md) object.
- [ALAssetsFilter](alassetsfilter.md)
  `ALAssetsFilter` encapsulates filtering criteria to be used when retrieving assets from a group.
- [ALAssetsGroup](alassetsgroup.md)
  An `ALAssetsGroup` object represents an ordered set of the assets managed by the Photos application. The order of the elements is the same as the user sees in the Photos application. An asset can belong to multiple assets groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetslibrary)*