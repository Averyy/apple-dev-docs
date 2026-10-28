# dataSize

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The size of the resource in bytes

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * dataSize;
```

## Discussion

The size may be unknown until a resource has finished being generated or processed and some resources never report one. `nil` means the size is unknown, not that it is zero.

## See Also

### Inspecting an Asset Resource
- [var type: PHAssetResourceType](./type.md)
  The relationship of an asset resource to its owning asset.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresource/datasize-6cf5k)*