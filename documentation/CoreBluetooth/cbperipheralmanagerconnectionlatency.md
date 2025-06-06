# CBPeripheralManagerConnectionLatency

**Framework**: Core Bluetooth  
**Kind**: enum

Values representing the connection latency of the peripheral manager.

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
enum CBPeripheralManagerConnectionLatency
```

## Topics

### Latency Values
- [CBPeripheralManagerConnectionLatency.low](cbperipheralmanagerconnectionlatency/low.md)
  A latency setting indicating that prioritizes rapid communication over battery life.
- [CBPeripheralManagerConnectionLatency.medium](cbperipheralmanagerconnectionlatency/medium.md)
  A latency setting that balances communication frequency and battery life.
- [CBPeripheralManagerConnectionLatency.high](cbperipheralmanagerconnectionlatency/high.md)
  A latency setting that prioritizes extending battery life over rapid communication.
### Initializers
- [init?(rawValue: Int)](cbperipheralmanagerconnectionlatency/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func setDesiredConnectionLatency(CBPeripheralManagerConnectionLatency, for: CBCentral)](cbperipheralmanager/setdesiredconnectionlatency(_:for:).md)
  Sets the desired connection latency for an existing connection to a central device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerconnectionlatency)*