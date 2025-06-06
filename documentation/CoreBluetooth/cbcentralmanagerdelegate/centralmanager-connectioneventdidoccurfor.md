# centralManager(_:connectionEventDidOccur:for:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate that a connection event occurred which matches the registered options.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func centralManager(_ central: CBCentralManager, connectionEventDidOccur event: CBConnectionEvent, for peripheral: CBPeripheral)
```

#### Discussion

The manager calls this method when it observes a connection event that matches the options provided to [`registerForConnectionEvents(options:)`](cbcentralmanager/registerforconnectionevents(options:).md).

## See Also

- [func centralManager(CBCentralManager, didConnect: CBPeripheral)](cbcentralmanagerdelegate/centralmanager(_:didconnect:).md)
  Tells the delegate that the central manager connected to a peripheral.
- [func centralManager(CBCentralManager, didDisconnectPeripheral: CBPeripheral, error: (any Error)?)](cbcentralmanagerdelegate/centralmanager(_:diddisconnectperipheral:error:).md)
  Tells the delegate that the central manager disconnected from a peripheral.
- [func centralManager(CBCentralManager, didFailToConnect: CBPeripheral, error: (any Error)?)](cbcentralmanagerdelegate/centralmanager(_:didfailtoconnect:error:).md)
  Tells the delegate the central manager failed to create a connection with a peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/centralmanager(_:connectioneventdidoccur:for:))*