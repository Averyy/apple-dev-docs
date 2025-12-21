# ALAssetsLibrary

**Framework**: Assets Library  
**Kind**: class

An instance of `ALAssetsLibrary` provides access to the videos and photos that are under the control of the Photos application.

## Declaration

```swift
class ALAssetsLibrary
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

### Accessing Assets
- [class func authorizationStatus() -> ALAuthorizationStatus](alassetslibrary/authorizationstatus.md)
  Returns photo data authorization status for this application.
### Managing Notifications
- [class func disableSharedPhotoStreamsSupport()](alassetslibrary/disablesharedphotostreamssupport.md)
  Disables shared photo streams notifications and asset retrieval.
### Finding Assets
- [func asset(for: URL!, resultBlock: ALAssetsLibraryAssetForURLResultBlock!, failureBlock: ALAssetsLibraryAccessFailureBlock!)](alassetslibrary/asset(for:resultblock:failureblock:).md)
  Invokes a given block passing as a parameter an asset identified by a specified file URL.
### Enumerating Assets
- [func enumerateGroups(withTypes: ALAssetsGroupType, using: ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock: ALAssetsLibraryAccessFailureBlock!)](alassetslibrary/enumerategroups(withtypes:using:failureblock:).md)
  Invokes a given block passing as a parameter each of the asset groups that match the given asset group type.
### Saving Assets
- [func writeVideoAtPath(toSavedPhotosAlbum: URL!, completionBlock: ((URL?, (any Error)?) -> Void)!)](alassetslibrary/writevideoatpath(tosavedphotosalbum:completionblock:).md)
  Saves a video identified by a given URL to the Saved Photos album.
- [func videoAtPathIs(compatibleWithSavedPhotosAlbum: URL!) -> Bool](alassetslibrary/videoatpathis(compatiblewithsavedphotosalbum:).md)
  Returns a Boolean value that indicates whether a video identified by a given URL is compatible with the Saved Photos album.
- [func writeImage(toSavedPhotosAlbum: CGImage!, orientation: ALAssetOrientation, completionBlock: ((URL?, (any Error)?) -> Void)!)](alassetslibrary/writeimage(tosavedphotosalbum:orientation:completionblock:).md)
  Saves a given image to the Saved Photos album.
- [func writeImageData(toSavedPhotosAlbum: Data!, metadata: [AnyHashable : Any]!, completionBlock: ((URL?, (any Error)?) -> Void)!)](alassetslibrary/writeimagedata(tosavedphotosalbum:metadata:completionblock:).md)
  Writes given image data and metadata to the Photos Album.
- [func writeImage(toSavedPhotosAlbum: CGImage!, metadata: [AnyHashable : Any]!, completionBlock: ((URL?, (any Error)?) -> Void)!)](alassetslibrary/writeimage(tosavedphotosalbum:metadata:completionblock:).md)
  Writes a given image and metadata to the Photos Album.
### Managing Asset Groups
- [func addAssetsGroupAlbum(withName: String!, resultBlock: ALAssetsLibraryGroupResultBlock!, failureBlock: ALAssetsLibraryAccessFailureBlock!)](alassetslibrary/addassetsgroupalbum(withname:resultblock:failureblock:).md)
  Adds a new assets group to the library.
- [func group(for: URL!, resultBlock: ALAssetsLibraryGroupResultBlock!, failureBlock: ALAssetsLibraryAccessFailureBlock!)](alassetslibrary/group(for:resultblock:failureblock:).md)
  Returns an assets group in the result block for a URL previously retrieved from an `ALAssetsGroup` object.
### Constants
- [typealias ALAssetsGroupType](alassetsgrouptype.md)
  A bitfield to identify types of asset.
- [Types of Asset](types-of-asset.md)
  Constants to identify types of asset.
- [enum ALAssetOrientation](alassetorientation.md)
  Constants to indicate the orientation of an asset.
- [typealias ALAssetsLibraryGroupsEnumerationResultsBlock](alassetslibrarygroupsenumerationresultsblock.md)
  Signature for the block executed when a match is found during enumeration using [`enumerateGroups(withTypes:using:failureBlock:)`](alassetslibrary/enumerategroups(withtypes:using:failureblock:).md).
- [typealias ALAssetsLibraryAssetForURLResultBlock](alassetslibraryassetforurlresultblock.md)
  Signature for the block executed if the user has granted access to the caller to access the data managed by the framework in [`asset(for:resultBlock:failureBlock:)`](alassetslibrary/asset(for:resultblock:failureblock:).md).
- [typealias ALAssetsLibraryWriteImageCompletionBlock](alassetslibrarywriteimagecompletionblock.md)
  Signature for the block executed when [`writeImage(toSavedPhotosAlbum:orientation:completionBlock:)`](alassetslibrary/writeimage(tosavedphotosalbum:orientation:completionblock:).md) completes.
- [typealias ALAssetsLibraryWriteVideoCompletionBlock](alassetslibrarywritevideocompletionblock.md)
  Signature for the block executed when [`writeVideoAtPath(toSavedPhotosAlbum:completionBlock:)`](alassetslibrary/writevideoatpath(tosavedphotosalbum:completionblock:).md) completes.
- [typealias ALAssetsLibraryAccessFailureBlock](alassetslibraryaccessfailureblock.md)
  Signature for the block executed if the user does not grant access to the caller to access the data managed by the framework.
- [typealias ALAssetsLibraryGroupResultBlock](alassetslibrarygroupresultblock.md)
  Signature for the block executed if the user grants access to the caller to access the data managed by the framework..
- [enum ALAuthorizationStatus](alauthorizationstatus.md)
  Constants to indicate authorization status.
- [Notification Keys](notification-keys.md)
  Keys used to get values from the user information dictionary of the [`ALAssetsLibraryChangedNotification`](alassetslibrarychangednotification.md) notification.
- [Error Domain](error-domain.md)
  Constant for the AssetsLibrary domain.
- [Error Codes](error-codes.md)
  AssetsLibrary-related error codes
### Notifications
- [static let ALAssetsLibraryChanged: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/ALAssetsLibraryChanged.md)
  Sent when the contents of the assets library have changed from under the app that is using the data.

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
- [class ALAssetsFilter](alassetsfilter.md)
  `ALAssetsFilter` encapsulates filtering criteria to be used when retrieving assets from a group.
- [class ALAssetsGroup](alassetsgroup.md)
  An `ALAssetsGroup` object represents an ordered set of the assets managed by the Photos application. The order of the elements is the same as the user sees in the Photos application. An asset can belong to multiple assets groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetslibrary)*