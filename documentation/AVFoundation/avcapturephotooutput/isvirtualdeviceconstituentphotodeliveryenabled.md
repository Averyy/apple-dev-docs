# isVirtualDeviceConstituentPhotoDeliveryEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the photo output delivers photos from constituent cameras of a virtual device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isVirtualDeviceConstituentPhotoDeliveryEnabled: Bool { get set }
```

#### Discussion

You can only set this value to [`true`](https://developer.apple.com/documentation/swift/true) when [`isVirtualDeviceConstituentPhotoDeliverySupported`](avcapturephotooutput/isvirtualdeviceconstituentphotodeliverysupported.md) is [`true`](https://developer.apple.com/documentation/swift/true).

The default value is [`false`](https://developer.apple.com/documentation/swift/false).

> ❗ **Important**:  Virtual device constituent photo delivery requires a lengthy reconfiguration of the capture render pipeline, so enable this property prior to starting the capture session.

## See Also

- [var isVirtualDeviceFusionSupported: Bool](avcapturephotooutput/isvirtualdevicefusionsupported.md)
  A Boolean value that indicates whether the device supports virtual device image fusion.
- [var isVirtualDeviceConstituentPhotoDeliverySupported: Bool](avcapturephotooutput/isvirtualdeviceconstituentphotodeliverysupported.md)
  A Boolean value that indicates whether the photo output configuration supports delivery of photos from constituent cameras of a virtual device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isvirtualdeviceconstituentphotodeliveryenabled)*