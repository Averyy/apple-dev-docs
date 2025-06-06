# setDesiredConnectionLatency(_:for:)

**Framework**: Core Bluetooth  
**Kind**: method

Sets the desired connection latency for an existing connection to a central device.

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
func setDesiredConnectionLatency(_ latency: CBPeripheralManagerConnectionLatency, for central: CBCentral)
```

#### Discussion

The latency of a peripheral-central connection controls how frequently the peripheral and the peripheral’s connected central can exchange messages. By setting a desired connection latency, you manage the relationship between the frequency of the data exchange and the resulting battery performance of the peripheral device. When you call this method to set the connection latency, note that connection latency changes aren’t guaranteed. As a result, the latency may vary. If you don’t explicitly set a latency, the central device uses the connection latency it chose when establishing the connection. Typically, you don’t need to change the connection latency.

## Parameters

- `latency`: The desired connection latency. For a list of the possible connection latency values that you may set for the peripheral manager, see  .
- `central`: The central to which the peripheral manager is currently connected.

## See Also

- [enum CBPeripheralManagerConnectionLatency](cbperipheralmanagerconnectionlatency.md)
  Values representing the connection latency of the peripheral manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/setdesiredconnectionlatency(_:for:))*