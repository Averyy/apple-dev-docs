# centralManager(_:didFailToConnect:error:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the central manager failed to create a connection with a peripheral.

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
optional func centralManager(_ central: CBCentralManager, didFailToConnect peripheral: CBPeripheral, error: (any Error)?)
```

```objc
- (void) centralManager:(CBCentralManager *) central didFailToConnectPeripheral:(CBPeripheral *) peripheral error:(NSError *) error;
```

#### Discussion

The manager invokes this method when a connection initiated with the [`connect(_:options:)`](../cbcentralmanager/connect%28_,options%29.md) method fails to complete. Because connection attempts don’t time out, a failed connection usually indicates a transient issue, in which case you may attempt connecting to the peripheral again.

## Parameters

- `central`: The central manager that provides this information.
- `peripheral`: The peripheral that failed to connect.
- `error`: The cause of the failure, or `nil` if no error occurred.

## See Also

### Monitoring Connections with Peripherals
- [func centralManager(CBCentralManager, didConnect: CBPeripheral)](./centralmanager%28_,didconnect%29.md)
  Tells the delegate that the central manager connected to a peripheral.
- [func centralManager(CBCentralManager, didDisconnectPeripheral: CBPeripheral, error: (any Error)?)](./centralmanager%28_,diddisconnectperipheral,error%29.md)
  Tells the delegate that the central manager disconnected from a peripheral.
- [func centralManager(CBCentralManager, connectionEventDidOccur: CBConnectionEvent, for: CBPeripheral)](./centralmanager%28_,connectioneventdidoccur,for%29.md)
  Tells the delegate that a connection event occurred which matches the registered options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/centralmanager(_:didfailtoconnect:error:))*