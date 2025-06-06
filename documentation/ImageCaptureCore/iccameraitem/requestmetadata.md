# requestMetadata()

**Framework**: ImageCaptureCore  
**Kind**: method

Requests metadata for the item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func requestMetadata()
```

#### Discussion

If metadata for the item is not readily available, accessing this property requests metadata from the camera, then notifies the delegate by calling [`cameraDevice(_:didReceiveMetadata:for:error:)`](iccameradevicedelegate/cameradevice(_:didreceivemetadata:for:error:).md).

Execution of the delegate callback occurs on the main thread.

## See Also

- [var metadata: [AnyHashable : Any]?](iccameraitem/metadata.md)
  The item’s metadata.
- [var metadataIfAvailable: [String : Any]?](iccameraitem/metadataifavailable.md)
  The item’s metadata if it is readily available.
- [func flushMetadataCache()](iccameraitem/flushmetadatacache.md)
  Deletes the item’s cached metadata.
- [struct ICCameraItemMetadataOption](iccameraitemmetadataoption.md)
  An option for the item’s metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/requestmetadata())*