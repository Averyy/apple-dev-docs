# contentType

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The type of data being provided for this asset resource. If not specified, one will be inferred from the PHAssetResourceType or file URL extension (if provided).

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var contentType: UTType? { get set }
```

```objc
@property (nonatomic, copy, nullable) UTType * contentType;
```

## See Also

### Describing a New Asset Resource
- [var originalFilename: String?](./originalfilename.md)
  The filename for the asset resource being created.
- [var uniformTypeIdentifier: String?](./uniformtypeidentifier.md)
  The uniform type identifier for the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourcecreationoptions/contenttype)*