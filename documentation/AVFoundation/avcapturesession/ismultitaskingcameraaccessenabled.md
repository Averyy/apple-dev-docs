# isMultitaskingCameraAccessEnabled

**Framework**: Avfoundation  
**Kind**: property

A Boolean value that indicates whether the capture session enables access to the camera while multitasking.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- tvOS 17.0+

## Declaration

```swift
var isMultitaskingCameraAccessEnabled: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false).

> ❗ **Important**:  For apps that have the [`com.apple.developer.avfoundation.multitasking-camera-access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.avfoundation.multitasking-camera-access) entitlement, this property value defaults to [`true`](https://developer.apple.com/documentation/swift/true) if [`isMultitaskingCameraAccessSupported`](avcapturesession/ismultitaskingcameraaccesssupported.md) is also [`true`](https://developer.apple.com/documentation/swift/true).

If the value of the [`isMultitaskingCameraAccessSupported`](avcapturesession/ismultitaskingcameraaccesssupported.md) property is [`true`](https://developer.apple.com/documentation/swift/true), you can enable multitasking camera access by setting this value to [`true`](https://developer.apple.com/documentation/swift/true) prior to starting the capture session.

This property is key-value observable.

> **Note**:  If you enable multitasking camera access, the system doesn’t interrupt the capture session with a reason of [`AVCaptureSession.InterruptionReason.videoDeviceNotAvailableWithMultipleForegroundApps`](avcapturesession/interruptionreason/videodevicenotavailablewithmultipleforegroundapps.md).

To learn about best practices for using the camera while multitasking, see [`Accessing the camera while multitasking on iPad`](https://developer.apple.com/documentation/AVKit/accessing-the-camera-while-multitasking-on-ipad).

## See Also

- [var isMultitaskingCameraAccessSupported: Bool](avcapturesession/ismultitaskingcameraaccesssupported.md)
  A Boolean value that indicates whether the capture session supports using the camera while multitasking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/ismultitaskingcameraaccessenabled)*