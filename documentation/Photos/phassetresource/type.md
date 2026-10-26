# type

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The relationship of an asset resource to its owning asset.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var type: PHAssetResourceType { get }
```

```objc
@property (nonatomic, assign, readonly) PHAssetResourceType type;
```

#### Discussion

An asset can contain multiple resources, and different resources contribute to the asset in different ways. For details and examples, see [`PHAssetResourceType`](../phassetresourcetype.md).

## See Also

### Inspecting an Asset Resource
- [enum PHAssetResourceType](../phassetresourcetype.md)
  Describes the relationship of an asset resource to its owning asset.
- [var contentType: UTType](./contenttype.md)
  The content type of the data associated with this asset resource
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

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresource/type)*