# init(uuid32:)

**Framework**: IOBluetooth  
**Kind**: init  
**Role**: Initializer

Creates a new 32-bit IOBluetoothSDPUUID with the given UUID32

**Availability**:
- macOS

## Declaration

```swift
init!(uuid32: BluetoothSDPUUID32)
```

```objc
- (instancetype) initWithUUID32:(BluetoothSDPUUID32) uuid32;
```

## Return Value

Returns self.

## Parameters

- `uuid32`: A scalar representing a 32-bit UUID

## See Also

### Initializers
- [convenience init!(bytes: UnsafeRawPointer!, length: UInt32)](./init%28bytes,length%29.md)
  Creates a new IOBluetoothSDPUUID object with the given bytes of the given length.
- [convenience init!(data: Data!)](./init%28data%29.md)
  Creates a new IOBluetoothSDPUUID object from the given NSData.
- [init!(uuid16: BluetoothSDPUUID16)](./init%28uuid16%29-7j3zk.md)
  Initializes a new 16-bit IOBluetoothSDPUUID with the given UUID16


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid/init(uuid32:)-7qjwq)*