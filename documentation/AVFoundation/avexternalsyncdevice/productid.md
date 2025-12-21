# productID

**Framework**: AVFoundation  
**Kind**: property

The USB product identifier associated with the external sync device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var productID: UInt32 { get }
```

#### Discussion

This `UInt32` value comes from the hardware vendor, and returns 0 if not available. Use this value in conjunction with the [`vendorID`](avexternalsyncdevice/vendorid.md) to determine a specific product.

## See Also

- [var clock: CMClock?](avexternalsyncdevice/clock.md)
  A clock representing the source of time from the external sync device.
- [var signalCompensationDelay: CMTime](avexternalsyncdevice/signalcompensationdelay.md)
  Delay to wait before starting the frame capture.
- [var status: AVExternalSyncDeviceStatus](avexternalsyncdevice/status.md)
  The status of the externally connected device.
- [var uuid: UUID](avexternalsyncdevice/uuid.md)
  A unique identifier for an external sync device.
- [var vendorID: UInt32](avexternalsyncdevice/vendorid.md)
  The USB vendor identifier associated with the external sync device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/productid)*