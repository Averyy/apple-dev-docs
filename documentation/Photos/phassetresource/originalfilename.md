# originalFilename

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The original filename of the asset resource from when it was created or imported.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use filename instead

## Declaration

```swift
var originalFilename: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * originalFilename;
```

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
- [var filename: String?](./filename.md)
  The filename associated with this asset resource (if any)
- [var pixelHeight: Int](./pixelheight.md)
  The height of the resource, in pixels.
- [var pixelWidth: Int](./pixelwidth.md)
  The width of the resource, in pixels.
- [var dataSize: Int?](./datasize-5lxva.md)
  The size of the resource in bytes
- [dataSize](./datasize-6cf5k.md)
  The size of the resource in bytes


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresource/originalfilename)*