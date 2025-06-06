# name

**Framework**: IOBluetooth  
**Kind**: property

Get the human readable name of the remote device.

**Availability**:
- macOS ?+

## Declaration

```swift
var name: String! { get }
```

#### Discussion

This only returns a value if a remote name request has been performed on the target device. If a successful remote name request has not been completed, nil is returned. To perform a remote name request, call -remoteNameRequest. If a remote name request has been successfully completed, the method -getLastNameUpdate will return the date/time of the last successful request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/name)*