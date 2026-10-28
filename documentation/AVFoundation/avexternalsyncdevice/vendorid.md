# vendorID

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The USB vendor identifier associated with the external sync device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var vendorID: UInt32 { get }
```

```objc
@property (nonatomic, readonly) UInt32 vendorID;
```

## Discussion

This `UInt32` value is provided by the hardware vendor, and returns 0 if not available.

## See Also

### Inspecting a device
- [var clock: CMClock?](./clock.md)
  A clock representing the source of time from the external sync device.
- [var productID: UInt32](./productid.md)
  The USB product identifier associated with the external sync device.
- [var signalCompensationDelay: CMTime](./signalcompensationdelay.md)
  Delay to wait before starting the frame capture.
- [var status: AVExternalSyncDeviceStatus](./status.md)
  The status of the externally connected device.
- [var uuid: UUID](./uuid.md)
  A unique identifier for an external sync device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/vendorid)*