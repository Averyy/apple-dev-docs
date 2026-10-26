# PHAssetResource

**Framework**: Photos  
**Kind**: class  
**Role**: Class

An underlying data resource associated with a photo, video, or Live Photo asset in the Photos library.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHAssetResource
```

```objc
@interface PHAssetResource : NSObject
```

## Mentions

- [Uploading asset resources in the background](../PhotoKit/uploading-asset-resources-in-the-background.md)

#### Overview

Each [`PHAsset`](./phasset.md) object references one or more resources. Use these objects to work with those resources directly, like when backing up or restoring assets.

- A photo asset can contain both JPEG and RAW files representing the same photo.
- A Live Photo asset contains both still photo and video resources.
- An edited asset contains resources representing asset content before and after the edit, as well as a resource corresponding to the [`PHAdjustmentData`](./phadjustmentdata.md) object that describes the edit.

To work with the data contained in an asset resource, fetch it using the [`PHAssetResourceManager`](./phassetresourcemanager.md) class.

## Topics

### Retrieving an Asset’s Data Resources
- [class func assetResources(for: PHAsset) -> [PHAssetResource]](./phassetresource/assetresources%28for%29-27o4l.md)
  Returns the list of data resources associated with an asset.
- [class func assetResources(for: PHLivePhoto) -> [PHAssetResource]](./phassetresource/assetresources%28for%29-2fedw.md)
  Returns the list of data resources associated with a Live Photo object.
- [class func assetResource(forUploadJob: PHAssetResourceUploadJob) -> PHAssetResource?](./phassetresource/assetresource%28foruploadjob%29.md)
  Returns the asset resource associated with the given upload job.
### Inspecting an Asset Resource
- [var type: PHAssetResourceType](./phassetresource/type.md)
  The relationship of an asset resource to its owning asset.
- [enum PHAssetResourceType](./phassetresourcetype.md)
  Describes the relationship of an asset resource to its owning asset.
- [var contentType: UTType](./phassetresource/contenttype.md)
  The content type of the data associated with this asset resource
- [var assetLocalIdentifier: String](./phassetresource/assetlocalidentifier.md)
  The unique identifier the system associates for a local asset object.
- [var uniformTypeIdentifier: String](./phassetresource/uniformtypeidentifier.md)
  The uniform type identifier for the asset resource’s image or video data.
- [var originalFilename: String](./phassetresource/originalfilename.md)
  The original filename of the asset resource from when it was created or imported.
- [var filename: String?](./phassetresource/filename.md)
  The filename associated with this asset resource (if any)
- [var pixelHeight: Int](./phassetresource/pixelheight.md)
  The height of the resource, in pixels.
- [var pixelWidth: Int](./phassetresource/pixelwidth.md)
  The width of the resource, in pixels.
- [var dataSize: Int?](./phassetresource/datasize-5lxva.md)
  The size of the resource in bytes

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Asset resource management
- [class PHAssetCreationRequest](./phassetcreationrequest.md)
  A request to create a new Photos asset from underlying data resources, for use in a photo library change block.
- [class PHAssetResourceCreationOptions](./phassetresourcecreationoptions.md)
  A set of options affecting the creation of a new Photos asset from underlying resources.
- [class PHAssetResourceManager](./phassetresourcemanager.md)
  A resource manager for the data storage underlying a Photos asset.
- [class PHAssetResourceRequestOptions](./phassetresourcerequestoptions.md)
  A set of options affecting the delivery of underlying asset data that you request from the asset-resource manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresource)*