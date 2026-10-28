# signalCompensationDelay

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Delay to wait before starting the frame capture.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var signalCompensationDelay: CMTime { get set }
```

```objc
@property (nonatomic) CMTime signalCompensationDelay;
```

## Discussion

An external sync is generally used to configure multiple devices in the real world. A display and a camera may receive a signal at the same time, but that does not mean the refresh of the display and camera are aligned in a way that does not cause tearing in the recording. The signal compensation delay can be used to offset the readout of a camera on an intra-frame scale.

Setting this property throws an NSInvalidArgumentException if called when [`isSignalCompensationDelaySupported`](./issignalcompensationdelaysupported.md) returns NO.

> ❗ **Important**: You should always set this property to a value less than the frame duration at which the camera is operating.

## See Also

### Inspecting a device
- [var clock: CMClock?](./clock.md)
  A clock representing the source of time from the external sync device.
- [var productID: UInt32](./productid.md)
  The USB product identifier associated with the external sync device.
- [var status: AVExternalSyncDeviceStatus](./status.md)
  The status of the externally connected device.
- [var uuid: UUID](./uuid.md)
  A unique identifier for an external sync device.
- [var vendorID: UInt32](./vendorid.md)
  The USB vendor identifier associated with the external sync device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/signalcompensationdelay)*