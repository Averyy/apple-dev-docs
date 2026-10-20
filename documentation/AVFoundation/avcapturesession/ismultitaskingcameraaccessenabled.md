# isMultitaskingCameraAccessEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the capture session enables access to the camera while multitasking.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 17.0+

## Declaration

```swift
var isMultitaskingCameraAccessEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isMultitaskingCameraAccessEnabled) BOOL multitaskingCameraAccessEnabled;
```

#### Discussion

The default value is [`false`](../../Swift/false.md).

> ❗ **Important**:  For apps that have the [`com.apple.developer.avfoundation.multitasking-camera-access`](../../BundleResources/entitlements/com.apple.developer.avfoundation.multitasking-camera-access.md) entitlement, this property value defaults to [`true`](../../Swift/true.md) if [`isMultitaskingCameraAccessSupported`](./ismultitaskingcameraaccesssupported.md) is also [`true`](../../Swift/true.md).

If the value of the [`isMultitaskingCameraAccessSupported`](./ismultitaskingcameraaccesssupported.md) property is [`true`](../../Swift/true.md), you can enable multitasking camera access by setting this value to [`true`](../../Swift/true.md) prior to starting the capture session.

This property is key-value observable.

> **Note**:  If you enable multitasking camera access, the system doesn’t interrupt the capture session with a reason of [`AVCaptureSession.InterruptionReason.videoDeviceNotAvailableWithMultipleForegroundApps`](./interruptionreason/videodevicenotavailablewithmultipleforegroundapps.md).

To learn about best practices for using the camera while multitasking, see [Accessing the camera while multitasking on iPad](../../AVKit/accessing-the-camera-while-multitasking-on-ipad.md).

## See Also

### Configuring multitasking
- [var isMultitaskingCameraAccessSupported: Bool](./ismultitaskingcameraaccesssupported.md)
  A Boolean value that indicates whether the capture session supports using the camera while multitasking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/ismultitaskingcameraaccessenabled)*