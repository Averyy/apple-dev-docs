# metadata

**Framework**: ImageCaptureCore  
**Kind**: property

The item’s metadata.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var metadata: [AnyHashable : Any]? { get }
```

#### Discussion

The value of this property is `nil` unless a [`requestMetadata()`](iccameraitem/requestmetadata().md) message is sent to this object.

## See Also

- [func requestMetadata()](iccameraitem/requestmetadata.md)
  Requests metadata for the item.
- [var metadataIfAvailable: [String : Any]?](iccameraitem/metadataifavailable.md)
  The item’s metadata if it is readily available.
- [func flushMetadataCache()](iccameraitem/flushmetadatacache.md)
  Deletes the item’s cached metadata.
- [struct ICCameraItemMetadataOption](iccameraitemmetadataoption.md)
  An option for the item’s metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/metadata)*