# status

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The status of the externally connected device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var status: AVExternalSyncDeviceStatus { get }
```

```objc
@property (nonatomic, readonly) AVExternalSyncDeviceStatus status;
```

#### Discussion

Use this property to query the current connection status of the external sync device. This property is key-value observable.

## See Also

### Inspecting a device
- [var clock: CMClock?](./clock.md)
  A clock representing the source of time from the external sync device.
- [var productID: UInt32](./productid.md)
  The USB product identifier associated with the external sync device.
- [var signalCompensationDelay: CMTime](./signalcompensationdelay.md)
  Delay to wait before starting the frame capture.
- [var uuid: UUID](./uuid.md)
  A unique identifier for an external sync device.
- [var vendorID: UInt32](./vendorid.md)
  The USB vendor identifier associated with the external sync device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/status)*