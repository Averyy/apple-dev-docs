# requestYield()

**Framework**: ImageCaptureCore  
**Kind**: method

Requests that device module in control of this device yield control.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func requestYield()
```

#### Discussion

Use this method only if the client will communicate with the device directly. The device module may not yield control of the device if it has an open session.

## See Also

- [func requestEjectOrDisconnect()](icdevice/requestejectordisconnect.md)
  Requests to eject the media if permitted by the device, or to disconnect from a remote device.
- [var moduleExecutableArchitecture: Int32](icdevice/moduleexecutablearchitecture.md)
  The executable architecture of the device module servicing the requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevice/requestyield())*