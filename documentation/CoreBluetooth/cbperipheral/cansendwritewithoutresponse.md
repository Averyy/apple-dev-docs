# canSendWriteWithoutResponse

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the remote device can send a write without a response.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var canSendWriteWithoutResponse: Bool { get }
```

```objc
@property (readonly) BOOL canSendWriteWithoutResponse;
```

## Discussion

If this value is [`false`](../../Swift/false.md), flushing all current writes sets the value to [`true`](../../Swift/true.md). This also results in a call to the delegate’s [`peripheralIsReady(toSendWriteWithoutResponse:)`](../cbperipheraldelegate/peripheralisready%28tosendwritewithoutresponse%29.md).

## See Also

### Monitoring a Peripheral’s Connection State
- [var state: CBPeripheralState](./state.md)
  The connection state of the peripheral.
- [enum CBPeripheralState](../cbperipheralstate.md)
  Values representing the connection state of a peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/cansendwritewithoutresponse)*