# recentAccessDate()

**Framework**: IOBluetooth  
**Kind**: method

Returns the date/time of the most recent access of the target device.

**Availability**:
- macOS ?+

## Declaration

```swift
func recentAccessDate() -> Date!
```

#### Return Value

Returns the date/time of the most recent access of the target device. If the device has not been accessed, nil is returned.

#### Discussion

This is the date that -recentDevices uses to sort its list of the most recently accessed devices.

NOTE: This method is only available in macOS 10.2.4 (Bluetooth v1.1) or later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/recentaccessdate())*