# contentType

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The content type of the data associated with this asset resource

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var contentType: UTType { get }
```

```objc
@property (nonatomic, copy, readonly) UTType * contentType;
```

#### Discussion

This resource’s data can be retrieved via [`PHAssetResourceManager`](../phassetresourcemanager.md)

## See Also

### Inspecting an Asset Resource
- [var type: PHAssetResourceType](./type.md)
  The relationship of an asset resource to its owning asset.
- [enum PHAssetResourceType](../phassetresourcetype.md)
  Describes the relationship of an asset resource to its owning asset.
- [var assetLocalIdentifier: String](./assetlocalidentifier.md)
  The unique identifier the system associates for a local asset object.
- [var uniformTypeIdentifier: String](./uniformtypeidentifier.md)
  The uniform type identifier for the asset resource’s image or video data.
- [var originalFilename: String](./originalfilename.md)
  The original filename of the asset resource from when it was created or imported.
- [var filename: String?](./filename.md)
  The filename associated with this asset resource (if any)
- [var pixelHeight: Int](./pixelheight.md)
  The height of the resource, in pixels.
- [var pixelWidth: Int](./pixelwidth.md)
  The width of the resource, in pixels.
- [var dataSize: Int?](./datasize-5lxva.md)
  The size of the resource in bytes


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresource/contenttype)*