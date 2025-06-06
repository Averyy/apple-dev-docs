# init(data:)

**Framework**: IOBluetooth  
**Kind**: init

Creates a new IOBluetoothSDPUUID object from the given NSData.

**Availability**:
- macOS ?+

## Declaration

```swift
convenience init!(data: Data!)
```

#### Return Value

Returns the new IOBluetoothSDPUUID object or nil on failure.

#### Discussion

If the length of the NSData is invalid for a UUID, nil is returned.

## Parameters

- `data`: The NSData containing the UUID bytes.

## See Also

- [convenience init!(bytes: UnsafeRawPointer!, length: UInt32)](iobluetoothsdpuuid/init(bytes:length:).md)
  Creates a new IOBluetoothSDPUUID object with the given bytes of the given length.
- [init!(uuid16: BluetoothSDPUUID16)](iobluetoothsdpuuid/init(uuid16:).md)
  Initializes a new 16-bit IOBluetoothSDPUUID with the given UUID16
- [init!(uuid32: BluetoothSDPUUID32)](iobluetoothsdpuuid/init(uuid32:).md)
  Creates a new 32-bit IOBluetoothSDPUUID with the given UUID32


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid/init(data:))*