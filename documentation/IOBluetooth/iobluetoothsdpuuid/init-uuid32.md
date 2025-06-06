# init(uuid32:)

**Framework**: IOBluetooth  
**Kind**: init

Creates a new 32-bit IOBluetoothSDPUUID with the given UUID32

**Availability**:
- macOS ?+

## Declaration

```swift
init!(uuid32: BluetoothSDPUUID32)
```

#### Return Value

Returns self.

## Parameters

- `uuid32`: A scalar representing a 32-bit UUID

## See Also

- [convenience init!(bytes: UnsafeRawPointer!, length: UInt32)](iobluetoothsdpuuid/init(bytes:length:).md)
  Creates a new IOBluetoothSDPUUID object with the given bytes of the given length.
- [convenience init!(data: Data!)](iobluetoothsdpuuid/init(data:).md)
  Creates a new IOBluetoothSDPUUID object from the given NSData.
- [init!(uuid16: BluetoothSDPUUID16)](iobluetoothsdpuuid/init(uuid16:).md)
  Initializes a new 16-bit IOBluetoothSDPUUID with the given UUID16


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid/init(uuid32:))*