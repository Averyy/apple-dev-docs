# init(uuid16:)

**Framework**: IOBluetooth  
**Kind**: init

Initializes a new 16-bit IOBluetoothSDPUUID with the given UUID16

**Availability**:
- macOS ?+

## Declaration

```swift
init!(uuid16: BluetoothSDPUUID16)
```

#### Return Value

Returns self.

## Parameters

- `uuid16`: A scalar representing a 16-bit UUID

## See Also

- [convenience init!(bytes: UnsafeRawPointer!, length: UInt32)](iobluetoothsdpuuid/init(bytes:length:).md)
  Creates a new IOBluetoothSDPUUID object with the given bytes of the given length.
- [convenience init!(data: Data!)](iobluetoothsdpuuid/init(data:).md)
  Creates a new IOBluetoothSDPUUID object from the given NSData.
- [init!(uuid32: BluetoothSDPUUID32)](iobluetoothsdpuuid/init(uuid32:).md)
  Creates a new 32-bit IOBluetoothSDPUUID with the given UUID32


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid/init(uuid16:))*