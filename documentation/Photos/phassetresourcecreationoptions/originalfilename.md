# originalFilename

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The filename for the asset resource being created.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var originalFilename: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * originalFilename;
```

#### Discussion

You can use this property to track the original name of the file from which you import an asset resource even if you use the [`addResource(with:data:options:)`](../phassetcreationrequest/addresource%28with,data,options%29.md) method to create a resource from data instead of from a file. After creating the asset, this information is available in the [`originalFilename`](../phassetresource/originalfilename.md) property of the corresponding [`PHAssetResource`](../phassetresource.md) object.

If you do not specify a value for this property and are using the [`addResource(with:fileURL:options:)`](../phassetcreationrequest/addresource%28with,fileurl,options%29.md) method to create a resource, Photos infers the filename from that method’s `fileURL` parameter. Otherwise, Photos automatically generates a filename.

## See Also

### Describing a New Asset Resource
- [var uniformTypeIdentifier: String?](./uniformtypeidentifier.md)
  The uniform type identifier for the resource.
- [var contentType: UTType?](./contenttype.md)
  The type of data being provided for this asset resource. If not specified, one will be inferred from the PHAssetResourceType or file URL extension (if provided).


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourcecreationoptions/originalfilename)*