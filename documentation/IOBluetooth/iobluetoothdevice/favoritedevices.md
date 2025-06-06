# favoriteDevices()

**Framework**: IOBluetooth  
**Kind**: method

Gets an array of the user’s favorite devices.

**Availability**:
- macOS ?+

## Declaration

```swift
class func favoriteDevices() -> [Any]!
```

#### Return Value

Returns an array of device objects representing the user’s favorite devices. If the user has no favorites, nil is returned.

#### Discussion

The resulting array contains IOBluetoothDevice objects.

NOTE: This method is only available in macOS 10.2.4 (Bluetooth v1.1) or later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/favoritedevices())*