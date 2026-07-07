# ALAssetPropertyDuration

**Framework**: Assets Library  
**Kind**: var

The key to retrieve the play time duration of a video asset.

## Declaration

```swift
extern NSString * const ALAssetPropertyDuration;
```

#### Discussion

The corresponding value is a double wrapped in an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object. For photos, [`ALErrorInvalidProperty`](alerrorinvalidproperty.md) is returned.

## See Also

- [ALAssetLibraryDeletedAssetGroupsKey](alassetlibrarydeletedassetgroupskey.md)
  Value is a set of [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) objects identifying the asset groups that were deleted.
- [ALAssetLibraryInsertedAssetGroupsKey](alassetlibraryinsertedassetgroupskey.md)
  Value is a set of [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) objects identifying the assets that were inserted.
- [ALAssetLibraryUpdatedAssetGroupsKey](alassetlibraryupdatedassetgroupskey.md)
  Value is a set of [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) objects identifying the asset groups that were updated.
- [ALAssetLibraryUpdatedAssetsKey](alassetlibraryupdatedassetskey.md)
  Value is a set of [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) objects identifying the assets that were updated.
- [ALAssetPropertyAssetURL](alassetpropertyasseturl.md)
  The key to retrieve a URL identifier for the asset.
- [ALAssetPropertyDate](alassetpropertydate.md)
  The key to retrieve the creation date of the asset.
- [ALAssetPropertyLocation](alassetpropertylocation.md)
  The key to retrieve the location information of the asset.
- [ALAssetPropertyOrientation](alassetpropertyorientation.md)
  The key to retrieve the orientation of the asset.
- [ALAssetPropertyRepresentations](alassetpropertyrepresentations.md)
  The key to retrieve the representations available for a given asset (for example RAW, JPEG).
- [ALAssetPropertyType](alassetpropertytype.md)
  A key to retrieve the type of the asset.
- [ALAssetPropertyURLs](alassetpropertyurls.md)
  The key to retrieve a dictionary that maps asset representations UTIs to URLs that uniquely identify the asset.
- [ALAssetTypePhoto](alassettypephoto.md)
  Specifies that the asset is a photo.
- [ALAssetTypeUnknown](alassettypeunknown.md)
  Specifies that the asset’s type cannot be determined.
- [ALAssetTypeVideo](alassettypevideo.md)
  Specifies that the asset is a video.
- [ALAssetsGroupPropertyName](alassetsgrouppropertyname.md)
  Key to retrieve the name of the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetpropertyduration)*