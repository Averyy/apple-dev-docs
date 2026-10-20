# moduleExecutableArchitecture

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The executable architecture of the device module servicing the requests.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: Module executable architecture is no longer available

## Declaration

```swift
var moduleExecutableArchitecture: Int32 { get }
```

```objc
@property (readonly) int moduleExecutableArchitecture;
```

## See Also

### Deprecated Symbols
- [func requestEjectOrDisconnect()](./requestejectordisconnect%28%29.md)
  Requests to eject the media if permitted by the device, or to disconnect from a remote device.
- [func requestYield()](./requestyield%28%29.md)
  Requests that device module in control of this device yield control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevice/moduleexecutablearchitecture)*