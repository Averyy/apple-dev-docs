# uuid

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A unique identifier for an external sync device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var uuid: UUID { get }
```

```objc
@property (nonatomic, readonly) NSUUID * uuid;
```

## Discussion

Use this property to select a specific external sync device.

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
- [var vendorID: UInt32](./vendorid.md)
  The USB vendor identifier associated with the external sync device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/uuid)*