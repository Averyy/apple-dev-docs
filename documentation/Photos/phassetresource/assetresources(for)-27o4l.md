# assetResources(for:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Returns the list of data resources associated with an asset.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func assetResources(for asset: PHAsset) -> [PHAssetResource]
```

```objc
+ (NSArray<PHAssetResource *> *) assetResourcesForAsset:(PHAsset *) asset;
```

#### Return Value

The asset’s resources.

#### Discussion

Asset resource objects describe the data files that an asset represents. An asset can contain multiple resources—for example, an edited photo asset contains resources for both the original and edited images, as well as for the [`PHAdjustmentData`](../phadjustmentdata.md) object describing the edit. To work with one of these files, fetch the underlying data using the [`PHAssetResourceManager`](../phassetresourcemanager.md) class.

## Parameters

- `asset`: A photo or video asset in the Photos library.

## See Also

### Retrieving an Asset’s Data Resources
- [class func assetResources(for: PHLivePhoto) -> [PHAssetResource]](./assetresources%28for%29-2fedw.md)
  Returns the list of data resources associated with a Live Photo object.
- [class func assetResource(forUploadJob: PHAssetResourceUploadJob) -> PHAssetResource?](./assetresource%28foruploadjob%29.md)
  Returns the asset resource associated with the given upload job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresource/assetresources(for:)-27o4l)*