# init(bytes:length:)

**Framework**: IOBluetooth  
**Kind**: init  
**Role**: Initializer

Creates a new IOBluetoothSDPUUID object with the given bytes of the given length.

**Availability**:
- macOS

## Declaration

```swift
convenience init!(bytes: UnsafeRawPointer!, length: UInt32)
```

```objc
+ (instancetype) uuidWithBytes:(const void *) bytes length:(unsigned int) length;
```

## Return Value

Returns the new IOBluetoothSDPUUID object or nil on failure.

## Discussion

If the length is invalid for a UUID, nil is returned.

## Parameters

- `bytes`: An array of bytes representing the UUID.
- `length`: The length of the array of bytes.

## See Also

### Initializers
- [convenience init!(data: Data!)](./init%28data%29.md)
  Creates a new IOBluetoothSDPUUID object from the given NSData.
- [init!(uuid16: BluetoothSDPUUID16)](./init%28uuid16%29-7j3zk.md)
  Initializes a new 16-bit IOBluetoothSDPUUID with the given UUID16
- [init!(uuid32: BluetoothSDPUUID32)](./init%28uuid32%29-7qjwq.md)
  Creates a new 32-bit IOBluetoothSDPUUID with the given UUID32


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid/init(bytes:length:))*