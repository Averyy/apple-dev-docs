# state

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

The connection state of the peripheral.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var state: CBPeripheralState { get }
```

```objc
@property (readonly) CBPeripheralState state;
```

## Discussion

This property represents the current connection state of the peripheral. For a list of the possible values, see [`CBPeripheralState`](../cbperipheralstate.md).

## See Also

### Monitoring a Peripheral’s Connection State
- [enum CBPeripheralState](../cbperipheralstate.md)
  Values representing the connection state of a peripheral.
- [var canSendWriteWithoutResponse: Bool](./cansendwritewithoutresponse.md)
  A Boolean value that indicates whether the remote device can send a write without a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/state)*