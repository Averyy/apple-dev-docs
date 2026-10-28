# assetLocalIdentifier

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The unique identifier the system associates for a local asset object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var assetLocalIdentifier: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * assetLocalIdentifier;
```

## Discussion

This property’s value corresponds to the [`localIdentifier`](../phobject/localidentifier.md) property of the [`PHAsset`](../phasset.md) object that owns this asset resource. If you’ve obtained an asset resource without a reference to its owning asset, use the [`fetchAssets(withLocalIdentifiers:options:)`](../phasset/fetchassets%28withlocalidentifiers,options%29.md) method with this identifier to retrieve the correct [`PHAsset`](../phasset.md) object.

## See Also

### Inspecting an Asset Resource
- [var type: PHAssetResourceType](./type.md)
  The relationship of an asset resource to its owning asset.
- [enum PHAssetResourceType](../phassetresourcetype.md)
  Describes the relationship of an asset resource to its owning asset.
- [var contentType: UTType](./contenttype.md)
  The content type of the data associated with this asset resource
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
- [dataSize](./datasize-6cf5k.md)
  The size of the resource in bytes


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresource/assetlocalidentifier)*