# assetResource(forUploadJob:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Returns the asset resource associated with the given upload job.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
class func assetResource(forUploadJob job: PHAssetResourceUploadJob) -> PHAssetResource?
```

```objc
+ (PHAssetResource *) assetResourceForUploadJob:(PHAssetResourceUploadJob *) job;
```

## Mentions

- [Uploading asset resources in the background](../../PhotoKit/uploading-asset-resources-in-the-background.md)

#### Return Value

The asset resource associated with the upload job, or nil if the resource cannot be found.

## Parameters

- `job`: The upload job whose associated asset resource is returned

## See Also

### Retrieving an Asset’s Data Resources
- [class func assetResources(for: PHAsset) -> [PHAssetResource]](./assetresources%28for%29-27o4l.md)
  Returns the list of data resources associated with an asset.
- [class func assetResources(for: PHLivePhoto) -> [PHAssetResource]](./assetresources%28for%29-2fedw.md)
  Returns the list of data resources associated with a Live Photo object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresource/assetresource(foruploadjob:))*