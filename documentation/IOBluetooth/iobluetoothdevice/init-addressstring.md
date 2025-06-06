# init(addressString:)

**Framework**: IOBluetooth  
**Kind**: init

Returns the IOBluetoothDevice object for the given BluetoothDeviceAddress

**Availability**:
- macOS ?+

## Declaration

```swift
convenience init!(addressString address: String!)
```

#### Return Value

Returns the IOBluetoothDevice object for the given BluetoothDeviceAddress

#### Discussion

Within a single application, there will be only one instance of IOBluetoothDevice for a given remote device address.

## Parameters

- `address`: Pointer to an NSString containing the BD_ADDR for which an IOBluetoothDevice instance is desired. The string should be of the form xx:xx:xx:xx:xx:xx

## See Also

- [convenience init!(address: UnsafePointer<BluetoothDeviceAddress>!)](iobluetoothdevice/init(address:).md)
  Returns the IOBluetoothDevice object for the given BluetoothDeviceAddress


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/init(addressstring:))*