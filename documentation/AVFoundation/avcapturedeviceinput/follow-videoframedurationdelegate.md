# follow(_:videoFrameDuration:delegate:)

**Framework**: AVFoundation  
**Kind**: method

Configures the the device input to follow an external sync device at the given frame duration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
func follow(_ externalSyncDevice: AVExternalSyncDevice, videoFrameDuration frameDuration: CMTime, delegate: (any AVExternalSyncDeviceDelegate)?)
```

#### Discussion

Call this method to direct your [`AVCaptureDeviceInput`](avcapturedeviceinput.md) to follow the external sync pulse from a sync device at the given frame duration.

Your provided `videoFrameDuration` value must match the sync pulse duration of the external sync device. If it does not, the request times out, the external sync device’s status returns to `AVExternalSyncDeviceStatusReady`, and your session stops running, posting a [`runtimeErrorNotification`](avcapturesession/runtimeerrornotification.md) with `AVErrorFollowExternalSyncDeviceTimedOut`.

The ability to follow an external sync device may change depending on the device configuration. For example, [`follow(_:videoFrameDuration:delegate:)`](avcapturedeviceinput/follow(_:videoframeduration:delegate:).md) cannot be used when [`isAutoVideoFrameRateEnabled`](avcapturedevice/isautovideoframerateenabled.md) is `true`.

To stop following an external pulse, call [`unfollowExternalSyncDevice()`](avcapturedeviceinput/unfollowexternalsyncdevice().md). External sync device following is also disabled when your device’s [`AVCaptureDevice.Format`](avcapturedevice/format.md) changes.

Your provided delegate’s [`externalSyncDeviceStatusDidChange(_:)`](avexternalsyncdevicedelegate/externalsyncdevicestatusdidchange(_:).md) method is called with a status of `AVExternalSyncDeviceStatusReady` if the external pulse signal is not close enough to the provided `videoFrameDuration` for successful calibration.

Once your [`status`](avexternalsyncdevice/status.md) changes to `AVExternalSyncDeviceStatusActiveSync`, your input’s  `AVCaptureInput/activeExternalSyncVideoFrameDuration` property reports the up-to-date frame duration. `AVCaptureInput/activeExternalSyncVideoFrameDuration` is also reflected in the [`activeVideoMinFrameDuration`](avcapturedevice/activevideominframeduration.md) and [`activeVideoMaxFrameDuration`](avcapturedevice/activevideomaxframeduration.md) of your input’s associated device.

> **Note**: Calling this method may cause a lengthy reconfiguration of the receiver, similar to setting a new active format or [`sessionPreset`](avcapturesession/sessionpreset.md).

> ❗ **Important**: Calling this method throws an `NSInvalidArgumentException` if [`isExternalSyncSupported`](avcapturedeviceinput/isexternalsyncsupported.md) returns `false`.

> ❗ **Important**: The provided external sync device’s `status` must be `AVExternalSyncDeviceStatusReady` when you call this method, otherwise an `NSInvalidArgumentException` is thrown.

## Parameters

- `externalSyncDevice`: The   hardware to follow.
- `delegate`: The delegate to notify when the connection status changes, or an error occurs.

## See Also

- [var isExternalSyncSupported: Bool](avcapturedeviceinput/isexternalsyncsupported.md)
  Indicates whether the device input supports being configured to follow an external sync device.
- [func unfollowExternalSyncDevice()](avcapturedeviceinput/unfollowexternalsyncdevice.md)
  Discontinues external sync.
- [var activeExternalSyncVideoFrameDuration: CMTime](avcapturedeviceinput/activeexternalsyncvideoframeduration.md)
  The receiver’s external sync frame duration (the reciprocal of its frame rate) when being driven by an external sync device.
- [var externalSyncDevice: AVExternalSyncDevice?](avcapturedeviceinput/externalsyncdevice.md)
  The external sync device currently being followed by this input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/follow(_:videoframeduration:delegate:))*