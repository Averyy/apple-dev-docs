# PHAssetResourceType

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

Describes the relationship of an asset resource to its owning asset.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum PHAssetResourceType
```

```c
enum PHAssetResourceType : NSInteger;
```

## Topics

### Resource Types
- [PHAssetResourceType.photo](./phassetresourcetype/photo.md)
  Provides the original photo data for its asset.
- [PHAssetResourceType.video](./phassetresourcetype/video.md)
  Provides the original video data for its asset.
- [PHAssetResourceType.audio](./phassetresourcetype/audio.md)
  Provides the original audio data for its asset.
- [PHAssetResourceType.alternatePhoto](./phassetresourcetype/alternatephoto.md)
  Provides photo data that isn’t the primary form of its asset.
- [PHAssetResourceType.fullSizePhoto](./phassetresourcetype/fullsizephoto.md)
  Provides a modified version of the original photo asset.
- [PHAssetResourceType.fullSizeVideo](./phassetresourcetype/fullsizevideo.md)
  Provides a modified version of the original video asset.
- [PHAssetResourceType.adjustmentData](./phassetresourcetype/adjustmentdata.md)
  Provides data for use in reconstructing recent edits to its asset.
- [PHAssetResourceType.adjustmentBasePhoto](./phassetresourcetype/adjustmentbasephoto.md)
  Provides an unaltered version of its photo asset for use in for use in reconstructing recent edits.
- [PHAssetResourceType.pairedVideo](./phassetresourcetype/pairedvideo.md)
  Provides the original video data component of a Live Photo asset.
- [PHAssetResourceType.fullSizePairedVideo](./phassetresourcetype/fullsizepairedvideo.md)
  Provides the current video data component of a Live Photo asset.
- [PHAssetResourceType.adjustmentBaseVideo](./phassetresourcetype/adjustmentbasevideo.md)
  Provides an unaltered version of its video asset.
- [PHAssetResourceType.adjustmentBasePairedVideo](./phassetresourcetype/adjustmentbasepairedvideo.md)
  Provides an unaltered version of the video data for a Live Photo asset for use in reconstructing recent edits.
### Enumeration Cases
- [PHAssetResourceType.photoProxy](./phassetresourcetype/photoproxy.md)
### Initializers
- [init?(rawValue: Int)](./phassetresourcetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inspecting an Asset Resource
- [var type: PHAssetResourceType](./phassetresource/type.md)
  The relationship of an asset resource to its owning asset.
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
- [dataSize](./phassetresource/datasize-6cf5k.md)
  The size of the resource in bytes


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourcetype)*