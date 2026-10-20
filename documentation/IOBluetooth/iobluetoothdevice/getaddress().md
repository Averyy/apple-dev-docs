# getAddress()

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Get the Bluetooth device address for the target device.

**Availability**:
- macOS

## Declaration

```swift
func getAddress() -> UnsafePointer<BluetoothDeviceAddress>!
```

```objc
- (const BluetoothDeviceAddress *) getAddress;
```

#### Return Value

Returns a pointer to the Bluetooth device address of the target device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/getaddress())*