# ALAssetOrientation

**Framework**: Assets Library  
**Kind**: enum

Constants to indicate the orientation of an asset.

## Declaration

```swift
enum ALAssetOrientation
```

## Topics

### Constants
- [ALAssetOrientation.up](alassetorientation/up.md)
  Indicates that the picture is in its default orientation.
- [ALAssetOrientation.down](alassetorientation/down.md)
  Indicates that the picture has been rotated through 180 degrees with respect to the up orientation.
- [ALAssetOrientation.left](alassetorientation/left.md)
  Indicates that the picture has been rotated through 90 degrees counter-clockwise with respect to the up orientation.
- [ALAssetOrientation.right](alassetorientation/right.md)
  Indicates that the picture has been rotated through 90 degrees clockwise with respect to the up orientation.
- [ALAssetOrientation.upMirrored](alassetorientation/upmirrored.md)
  Indicates that the picture has been flipped horizontally with respect to the up orientation.
- [ALAssetOrientation.downMirrored](alassetorientation/downmirrored.md)
  Indicates that the picture has been rotated through 180 degrees with respect to up orientation, and then flipped horizontally.
- [ALAssetOrientation.leftMirrored](alassetorientation/leftmirrored.md)
  Indicates that the picture has been rotated through 90 degrees counter-clockwise with respect to the up orientation, and then flipped vertically.
- [ALAssetOrientation.rightMirrored](alassetorientation/rightmirrored.md)
  Indicates that the picture has been rotated through 90 degrees clockwise with respect to the up orientation and then flipped vertically.
### Initializers
- [init?(rawValue: Int)](alassetorientation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [typealias ALAssetsGroupType](alassetsgrouptype.md)
  A bitfield to identify types of asset.
- [Types of Asset](types-of-asset.md)
  Constants to identify types of asset.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetorientation)*