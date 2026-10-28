# requestYield()

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Requests that device module in control of this device yield control.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: Requesting a device yield is no longer avaialble

## Declaration

```swift
func requestYield()
```

```objc
- (void) requestYield;
```

## Discussion

Use this method only if the client will communicate with the device directly. The device module may not yield control of the device if it has an open session.

## See Also

### Deprecated Symbols
- [func requestEjectOrDisconnect()](./requestejectordisconnect%28%29.md)
  Requests to eject the media if permitted by the device, or to disconnect from a remote device.
- [var moduleExecutableArchitecture: Int32](./moduleexecutablearchitecture.md)
  The executable architecture of the device module servicing the requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevice/requestyield())*