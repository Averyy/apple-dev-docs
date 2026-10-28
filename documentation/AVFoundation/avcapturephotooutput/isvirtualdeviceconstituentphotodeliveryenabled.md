# isVirtualDeviceConstituentPhotoDeliveryEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, getter=isVirtualDeviceConstituentPhotoDeliveryEnabled) BOOL virtualDeviceConstituentPhotoDeliveryEnabled;
```

## Discussion

You can only set this value to [`true`](../../Swift/true.md) when [`isVirtualDeviceConstituentPhotoDeliverySupported`](./isvirtualdeviceconstituentphotodeliverysupported.md) is [`true`](../../Swift/true.md).

The default value is [`false`](../../Swift/false.md).

> ❗ **Important**:  Virtual device constituent photo delivery requires a lengthy reconfiguration of the capture render pipeline, so enable this property prior to starting the capture session.

## See Also

### Configuring virtual device capture
- [var isVirtualDeviceFusionSupported: Bool](./isvirtualdevicefusionsupported.md)
  A Boolean value that indicates whether the device supports virtual device image fusion.
- [var isVirtualDeviceConstituentPhotoDeliverySupported: Bool](./isvirtualdeviceconstituentphotodeliverysupported.md)
  A Boolean value that indicates whether the photo output configuration supports delivery of photos from constituent cameras of a virtual device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isvirtualdeviceconstituentphotodeliveryenabled)*