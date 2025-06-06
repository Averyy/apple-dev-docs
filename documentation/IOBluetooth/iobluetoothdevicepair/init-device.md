# init(device:)

**Framework**: IOBluetooth  
**Kind**: init

Creates an autorelease IOBluetoothDevicePair object with a device as the pairing target.

**Availability**:
- macOS ?+

## Declaration

```swift
convenience init!(device: IOBluetoothDevice!)
```

#### Return Value

Returns an IOReturn or Bluetooth error code, if the pairing could not be started.

## Parameters

- `device`: An IOBluetoothDevice to attept to pair with. The device is retained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepair/init(device:))*