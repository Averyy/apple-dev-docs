# init(address:)

**Framework**: IOBluetooth  
**Kind**: init  
**Role**: Initializer

Returns the IOBluetoothDevice object for the given BluetoothDeviceAddress

**Availability**:
- macOS

## Declaration

```swift
convenience init!(address: UnsafePointer<BluetoothDeviceAddress>!)
```

```objc
+ (instancetype) deviceWithAddress:(const BluetoothDeviceAddress *) address;
```

#### Return Value

Returns the IOBluetoothDevice object for the given BluetoothDeviceAddress

#### Discussion

Within a single application, there will be only one instance of IOBluetoothDevice for a given remote device address.

## Parameters

- `address`: Pointer to a BluetoothDeviceAddress for which an IOBluetoothDevice instance is desired

## See Also

### Initializers
- [convenience init!(addressString: String!)](./init%28addressstring%29.md)
  Returns the IOBluetoothDevice object for the given BluetoothDeviceAddress


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/init(address:))*