# metadataIfAvailable

**Framework**: ImageCaptureCore  
**Kind**: property

The item’s metadata if it is readily available.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var metadataIfAvailable: [String : Any]? { get }
```

#### Discussion

If metadata is not readily available, accessing this property will send a message to the device requesting metadata for the file. The delegate of the device will be notified via method [`cameraDevice(_:didReceiveMetadataFor:)`](iccameradevicedelegate/cameradevice(_:didreceivemetadatafor:).md), if this method is implemented by the delegate. Execution of the delegate callback will occur on the main thread.

## See Also

- [func requestMetadata()](iccameraitem/requestmetadata.md)
  Requests metadata for the item.
- [var metadata: [AnyHashable : Any]?](iccameraitem/metadata.md)
  The item’s metadata.
- [func flushMetadataCache()](iccameraitem/flushmetadatacache.md)
  Deletes the item’s cached metadata.
- [struct ICCameraItemMetadataOption](iccameraitemmetadataoption.md)
  An option for the item’s metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/metadataifavailable)*