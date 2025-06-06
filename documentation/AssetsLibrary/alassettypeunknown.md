# ALAssetTypeUnknown

**Framework**: Assets Library  
**Kind**: var

Specifies that the asset’s type cannot be determined.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
let ALAssetTypeUnknown: String
```

#### Discussion

The asset could be a sound file, a video or photo file that the system doesn’t know about or something else. This is possible only for assets imported from a camera onto the device.

## See Also

- [let ALAssetLibraryDeletedAssetGroupsKey: String](alassetlibrarydeletedassetgroupskey.md)
  Value is a set of [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) objects identifying the asset groups that were deleted.
- [let ALAssetLibraryInsertedAssetGroupsKey: String](alassetlibraryinsertedassetgroupskey.md)
  Value is a set of [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) objects identifying the assets that were inserted.
- [let ALAssetLibraryUpdatedAssetGroupsKey: String](alassetlibraryupdatedassetgroupskey.md)
  Value is a set of [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) objects identifying the asset groups that were updated.
- [let ALAssetLibraryUpdatedAssetsKey: String](alassetlibraryupdatedassetskey.md)
  Value is a set of [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) objects identifying the assets that were updated.
- [let ALAssetPropertyAssetURL: String](alassetpropertyasseturl.md)
  The key to retrieve a URL identifier for the asset.
- [let ALAssetPropertyDate: String](alassetpropertydate.md)
  The key to retrieve the creation date of the asset.
- [let ALAssetPropertyDuration: String](alassetpropertyduration.md)
  The key to retrieve the play time duration of a video asset.
- [let ALAssetPropertyLocation: String](alassetpropertylocation.md)
  The key to retrieve the location information of the asset.
- [let ALAssetPropertyOrientation: String](alassetpropertyorientation.md)
  The key to retrieve the orientation of the asset.
- [let ALAssetPropertyRepresentations: String](alassetpropertyrepresentations.md)
  The key to retrieve the representations available for a given asset (for example RAW, JPEG).
- [let ALAssetPropertyType: String](alassetpropertytype.md)
  A key to retrieve the type of the asset.
- [let ALAssetPropertyURLs: String](alassetpropertyurls.md)
  The key to retrieve a dictionary that maps asset representations UTIs to URLs that uniquely identify the asset.
- [let ALAssetTypePhoto: String](alassettypephoto.md)
  Specifies that the asset is a photo.
- [let ALAssetTypeVideo: String](alassettypevideo.md)
  Specifies that the asset is a video.
- [let ALAssetsGroupPropertyName: String](alassetsgrouppropertyname.md)
  Key to retrieve the name of the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassettypeunknown)*