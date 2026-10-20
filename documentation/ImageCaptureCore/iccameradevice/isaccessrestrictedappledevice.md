# isAccessRestrictedAppleDevice

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the device is an Apple device, passcode-locked, and connected to an untrusted host.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var isAccessRestrictedAppleDevice: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isAccessRestrictedAppleDevice) BOOL accessRestrictedAppleDevice;
```

## See Also

### Detecting Apple Devices
- [var iCloudPhotosEnabled: Bool](./icloudphotosenabled.md)
  A Boolean value indicating whether the iCloud Photo Library is enabled on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/isaccessrestrictedappledevice)*