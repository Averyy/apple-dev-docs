# scannerDeviceDidBecomeAvailable(_:)

**Framework**: ImageCaptureCore  
**Kind**: method

Tells the client when another client closes the current open session on the scanner.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func scannerDeviceDidBecomeAvailable(_ scanner: ICScannerDevice)
```

#### Discussion

Scanners require exclusive access. Only one client can open a session on a scanner at a time. The scanner is available if it does not have a session opened by another client. Attempting to open a session on a scanner that already has an open session for another client will result in an error.

To open a session on a scanner as soon as it is available, implement this method and call [`requestOpenSession()`](icdevice/requestopensession().md) in the method body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevicedelegate/scannerdevicedidbecomeavailable(_:))*