# offset

**Framework**: Core Bluetooth  
**Kind**: property

The zero-based index of the first byte for the read or write request.

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
var offset: Int { get }
```

#### Discussion

You can use the value of this property to ensure that the ATT request is attempting to read or write within the proper bounds of the characteristic’s value. For an example of how to take a request’s offset property into account when responding to a read or write request, see [`Responding to Read and Write Requests from a Central`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/PerformingCommonPeripheralRoleTasks/PerformingCommonPeripheralRoleTasks.html#//apple_ref/doc/uid/TP40013257-CH4-SW6).

## See Also

- [var central: CBCentral](cbattrequest/central.md)
  The remote central device that originated the request.
- [var characteristic: CBCharacteristic](cbattrequest/characteristic.md)
  The characteristic to read or write the value of.
- [var value: Data?](cbattrequest/value.md)
  The data that the central reads from or writes to the peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbattrequest/offset)*