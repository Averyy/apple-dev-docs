# CBPeripheralState

**Framework**: Core Bluetooth  
**Kind**: enum  
**Role**: Enumeration

Values representing the connection state of a peripheral.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum CBPeripheralState
```

```c
enum CBPeripheralState : NSInteger;
```

## Topics

### Peripheral States
- [CBPeripheralState.disconnected](./cbperipheralstate/disconnected.md)
  The peripheral isn’t connected to the central manager.
- [CBPeripheralState.connecting](./cbperipheralstate/connecting.md)
  The peripheral is in the process of connecting to the central manager.
- [CBPeripheralState.connected](./cbperipheralstate/connected.md)
  The peripheral is connected to the central manager.
- [CBPeripheralState.disconnecting](./cbperipheralstate/disconnecting.md)
  The peripheral is disconnecting from the central manager.
### Initializers
- [init?(rawValue: Int)](./cbperipheralstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Monitoring a Peripheral’s Connection State
- [var state: CBPeripheralState](./cbperipheral/state.md)
  The connection state of the peripheral.
- [var canSendWriteWithoutResponse: Bool](./cbperipheral/cansendwritewithoutresponse.md)
  A Boolean value that indicates whether the remote device can send a write without a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralstate)*