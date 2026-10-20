# flushMetadataCache()

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Deletes the item’s cached metadata.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func flushMetadataCache()
```

```objc
- (void) flushMetadataCache;
```

## See Also

### Requesting Metadata
- [func requestMetadata()](./requestmetadata%28%29.md)
  Requests metadata for the item.
- [var metadata: [AnyHashable : Any]?](./metadata.md)
  The item’s metadata.
- [var metadataIfAvailable: [String : Any]?](./metadataifavailable.md)
  The item’s metadata if it is readily available.
- [struct ICCameraItemMetadataOption](../iccameraitemmetadataoption.md)
  An option for the item’s metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/flushmetadatacache())*