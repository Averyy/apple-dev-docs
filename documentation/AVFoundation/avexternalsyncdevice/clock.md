# clock

**Framework**: AVFoundation  
**Kind**: property

A clock representing the source of time from the external sync device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var clock: CMClock? { get }
```

#### Discussion

This property returns `NULL` until the [`status`](avexternalsyncdevice/status.md) reaches `AVExternalSyncDeviceStatusActiveSync`.

## See Also

- [var productID: UInt32](avexternalsyncdevice/productid.md)
  The USB product identifier associated with the external sync device.
- [var signalCompensationDelay: CMTime](avexternalsyncdevice/signalcompensationdelay.md)
  Delay to wait before starting the frame capture.
- [var status: AVExternalSyncDeviceStatus](avexternalsyncdevice/status.md)
  The status of the externally connected device.
- [var uuid: UUID](avexternalsyncdevice/uuid.md)
  A unique identifier for an external sync device.
- [var vendorID: UInt32](avexternalsyncdevice/vendorid.md)
  The USB vendor identifier associated with the external sync device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/clock)*