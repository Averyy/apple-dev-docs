# centralManager(_:didDisconnectPeripheral:error:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the central manager disconnected from a peripheral.

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
optional func centralManager(_ central: CBCentralManager, didDisconnectPeripheral peripheral: CBPeripheral, error: (any Error)?)
```

```objc
- (void) centralManager:(CBCentralManager *) central didDisconnectPeripheral:(CBPeripheral *) peripheral error:(NSError *) error;
```

#### Discussion

The manager invokes this method when disconnecting a peripheral previously connected with the [`connect(_:options:)`](../cbcentralmanager/connect%28_,options%29.md) method. The error parameter contains the reason for the disconnection, unless the disconnect resulted from a call to [`cancelPeripheralConnection(_:)`](../cbcentralmanager/cancelperipheralconnection%28_%29.md). After this method executes, the peripheral device’s [`CBPeripheralDelegate`](../cbperipheraldelegate.md) object receives no further method calls.

All services, characteristics, and characteristic descriptors a peripheral become invalidated after it disconnects.

## Parameters

- `central`: The central manager that provides this information.
- `peripheral`: The now-disconnected peripheral.
- `error`: The cause of the failure, or `nil` if no error occurred.

## See Also

### Monitoring Connections with Peripherals
- [func centralManager(CBCentralManager, didConnect: CBPeripheral)](./centralmanager%28_,didconnect%29.md)
  Tells the delegate that the central manager connected to a peripheral.
- [func centralManager(CBCentralManager, didFailToConnect: CBPeripheral, error: (any Error)?)](./centralmanager%28_,didfailtoconnect,error%29.md)
  Tells the delegate the central manager failed to create a connection with a peripheral.
- [func centralManager(CBCentralManager, connectionEventDidOccur: CBConnectionEvent, for: CBPeripheral)](./centralmanager%28_,connectioneventdidoccur,for%29.md)
  Tells the delegate that a connection event occurred which matches the registered options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/centralmanager(_:diddisconnectperipheral:error:))*