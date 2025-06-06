# centralManager(_:didConnect:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate that the central manager connected to a peripheral.

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
optional func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral)
```

#### Discussion

The manager invokes this method when a call to [`connect(_:options:)`](cbcentralmanager/connect(_:options:).md) succeeds. You typically implement this method to set the peripheral’s delegate and discover its services.

For more information, see [`Core Bluetooth Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257).

## Parameters

- `central`: The central manager that provides this information.
- `peripheral`: The now-connected peripheral.

## See Also

- [func centralManager(CBCentralManager, didDisconnectPeripheral: CBPeripheral, error: (any Error)?)](cbcentralmanagerdelegate/centralmanager(_:diddisconnectperipheral:error:).md)
  Tells the delegate that the central manager disconnected from a peripheral.
- [func centralManager(CBCentralManager, didFailToConnect: CBPeripheral, error: (any Error)?)](cbcentralmanagerdelegate/centralmanager(_:didfailtoconnect:error:).md)
  Tells the delegate the central manager failed to create a connection with a peripheral.
- [func centralManager(CBCentralManager, connectionEventDidOccur: CBConnectionEvent, for: CBPeripheral)](cbcentralmanagerdelegate/centralmanager(_:connectioneventdidoccur:for:).md)
  Tells the delegate that a connection event occurred which matches the registered options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/centralmanager(_:didconnect:))*