# ICCameraItemMetadataOption

**Framework**: ImageCaptureCore  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * ICCameraItemMetadataOption;
```

## Topics

### Initializers
- [init(rawValue: String)](./iccameraitemmetadataoption/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Requesting Metadata
- [func requestMetadata()](./iccameraitem/requestmetadata%28%29.md)
  Requests metadata for the item.
- [var metadata: [AnyHashable : Any]?](./iccameraitem/metadata.md)
  The item’s metadata.
- [var metadataIfAvailable: [String : Any]?](./iccameraitem/metadataifavailable.md)
  The item’s metadata if it is readily available.
- [func flushMetadataCache()](./iccameraitem/flushmetadatacache%28%29.md)
  Deletes the item’s cached metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitemmetadataoption)*