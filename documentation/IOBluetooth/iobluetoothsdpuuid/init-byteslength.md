# init(bytes:length:)

**Framework**: IOBluetooth  
**Kind**: init

Creates a new IOBluetoothSDPUUID object with the given bytes of the given length.

**Availability**:
- macOS ?+

## Declaration

```swift
convenience init!(bytes: UnsafeRawPointer!, length: UInt32)
```

#### Return Value

Returns the new IOBluetoothSDPUUID object or nil on failure.

#### Discussion

If the length is invalid for a UUID, nil is returned.

## Parameters

- `bytes`: An array of bytes representing the UUID.
- `length`: The length of the array of bytes.

## See Also

- [convenience init!(data: Data!)](iobluetoothsdpuuid/init(data:).md)
  Creates a new IOBluetoothSDPUUID object from the given NSData.
- [init!(uuid16: BluetoothSDPUUID16)](iobluetoothsdpuuid/init(uuid16:).md)
  Initializes a new 16-bit IOBluetoothSDPUUID with the given UUID16
- [init!(uuid32: BluetoothSDPUUID32)](iobluetoothsdpuuid/init(uuid32:).md)
  Creates a new 32-bit IOBluetoothSDPUUID with the given UUID32


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid/init(bytes:length:))*