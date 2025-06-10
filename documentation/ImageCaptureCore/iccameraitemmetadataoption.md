# ICCameraItemMetadataOption

**Framework**: ImageCaptureCore  
**Kind**: struct

An option for the item’s metadata.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
struct ICCameraItemMetadataOption
```

## Topics

### Initializers
- [init(rawValue: String)](iccameraitemmetadataoption/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func requestMetadata()](iccameraitem/requestmetadata.md)
  Requests metadata for the item.
- [var metadata: [AnyHashable : Any]?](iccameraitem/metadata.md)
  The item’s metadata.
- [var metadataIfAvailable: [String : Any]?](iccameraitem/metadataifavailable.md)
  The item’s metadata if it is readily available.
- [func flushMetadataCache()](iccameraitem/flushmetadatacache.md)
  Deletes the item’s cached metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitemmetadataoption)*