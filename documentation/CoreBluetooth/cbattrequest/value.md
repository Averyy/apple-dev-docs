# value

**Framework**: Core Bluetooth  
**Kind**: property

The data that the central reads from or writes to the peripheral.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var value: Data? { get set }
```

#### Discussion

The value of this property depends on whether the request type is read or write. For read requests, the property is `nil,` and you should set it before responding to the remote central through the [`respond(to:withResult:)`](cbperipheralmanager/respond(to:withresult:).md) method. For write requests, the value is the data to write to the characteristic’s value.

## See Also

- [var central: CBCentral](cbattrequest/central.md)
  The remote central device that originated the request.
- [var characteristic: CBCharacteristic](cbattrequest/characteristic.md)
  The characteristic to read or write the value of.
- [var offset: Int](cbattrequest/offset.md)
  The zero-based index of the first byte for the read or write request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbattrequest/value)*