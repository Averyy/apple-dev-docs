# isVirtualDeviceConstituentPhotoDeliverySupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isVirtualDeviceConstituentPhotoDeliverySupported) BOOL virtualDeviceConstituentPhotoDeliverySupported;
```

## Discussion

The system only supports virtual device constituent photo delivery for certain capture session presets and capture device formats.

When switching cameras or formats, this property may change. When this property changes from [`true`](../../Swift/true.md) to [`false`](../../Swift/false.md), [`isVirtualDeviceConstituentPhotoDeliveryEnabled`](./isvirtualdeviceconstituentphotodeliveryenabled.md) also reverts to [`false`](../../Swift/false.md).

This property is key-value observable.

## See Also

### Configuring virtual device capture
- [var isVirtualDeviceFusionSupported: Bool](./isvirtualdevicefusionsupported.md)
  A Boolean value that indicates whether the device supports virtual device image fusion.
- [var isVirtualDeviceConstituentPhotoDeliveryEnabled: Bool](./isvirtualdeviceconstituentphotodeliveryenabled.md)
  A Boolean value that indicates whether the photo output delivers photos from constituent cameras of a virtual device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isvirtualdeviceconstituentphotodeliverysupported)*