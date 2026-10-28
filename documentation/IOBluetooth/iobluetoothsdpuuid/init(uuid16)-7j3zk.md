# init(uuid16:)

**Framework**: IOBluetooth  
**Kind**: init  
**Role**: Initializer

Initializes a new 16-bit IOBluetoothSDPUUID with the given UUID16

**Availability**:
- macOS

## Declaration

```swift
init!(uuid16: BluetoothSDPUUID16)
```

```objc
- (instancetype) initWithUUID16:(BluetoothSDPUUID16) uuid16;
```

## Return Value

Returns self.

## Parameters

- `uuid16`: A scalar representing a 16-bit UUID

## See Also

### Initializers
- [convenience init!(bytes: UnsafeRawPointer!, length: UInt32)](./init%28bytes,length%29.md)
  Creates a new IOBluetoothSDPUUID object with the given bytes of the given length.
- [convenience init!(data: Data!)](./init%28data%29.md)
  Creates a new IOBluetoothSDPUUID object from the given NSData.
- [init!(uuid32: BluetoothSDPUUID32)](./init%28uuid32%29-7qjwq.md)
  Creates a new 32-bit IOBluetoothSDPUUID with the given UUID32


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid/init(uuid16:)-7j3zk)*