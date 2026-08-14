# isVirtualDeviceFusionSupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the device supports virtual device image fusion.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isVirtualDeviceFusionSupported: Bool { get }
```

#### Discussion

When using a virtual capture device, the system can fuse the images from its constituent cameras to improve image quality.

If the current configuration doesn’t support virtual device fusion, your capture requests always resolve [`isVirtualDeviceFusionEnabled`](avcaptureresolvedphotosettings/isvirtualdevicefusionenabled.md) to [`false`](https://developer.apple.com/documentation/swift/false).

This property is key-value observable.

## See Also

- [var isVirtualDeviceConstituentPhotoDeliverySupported: Bool](avcapturephotooutput/isvirtualdeviceconstituentphotodeliverysupported.md)
  A Boolean value that indicates whether the photo output configuration supports delivery of photos from constituent cameras of a virtual device.
- [var isVirtualDeviceConstituentPhotoDeliveryEnabled: Bool](avcapturephotooutput/isvirtualdeviceconstituentphotodeliveryenabled.md)
  A Boolean value that indicates whether the photo output delivers photos from constituent cameras of a virtual device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isvirtualdevicefusionsupported)*