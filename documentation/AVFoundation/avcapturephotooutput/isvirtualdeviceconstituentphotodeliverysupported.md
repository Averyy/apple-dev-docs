# isVirtualDeviceConstituentPhotoDeliverySupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the photo output configuration supports delivery of photos from constituent cameras of a virtual device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isVirtualDeviceConstituentPhotoDeliverySupported: Bool { get }
```

#### Discussion

The system only supports virtual device constituent photo delivery for certain capture session presets and capture device formats.

When switching cameras or formats, this property may change. When this property changes from [`true`](https://developer.apple.com/documentation/swift/true) to [`false`](https://developer.apple.com/documentation/swift/false), [`isVirtualDeviceConstituentPhotoDeliveryEnabled`](avcapturephotooutput/isvirtualdeviceconstituentphotodeliveryenabled.md) also reverts to [`false`](https://developer.apple.com/documentation/swift/false).

This property is key-value observable.

## See Also

- [var isVirtualDeviceFusionSupported: Bool](avcapturephotooutput/isvirtualdevicefusionsupported.md)
  A Boolean value that indicates whether the device supports virtual device image fusion.
- [var isVirtualDeviceConstituentPhotoDeliveryEnabled: Bool](avcapturephotooutput/isvirtualdeviceconstituentphotodeliveryenabled.md)
  A Boolean value that indicates whether the photo output delivers photos from constituent cameras of a virtual device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isvirtualdeviceconstituentphotodeliverysupported)*