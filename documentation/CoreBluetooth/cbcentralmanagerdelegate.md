# CBCentralManagerDelegate

**Framework**: Core Bluetooth  
**Kind**: protocol

A protocol that provides updates for the discovery and management of peripheral devices.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
protocol CBCentralManagerDelegate : NSObjectProtocol
```

#### Overview

The [`CBCentralManagerDelegate`](cbcentralmanagerdelegate.md) protocol defines the methods that a delegate of a [`CBCentralManager`](cbcentralmanager.md) object must adopt. The optional methods of the protocol allow the delegate to monitor the discovery, connectivity, and retrieval of peripheral devices. The only required method is [`centralManagerDidUpdateState(_:)`](cbcentralmanagerdelegate/centralmanagerdidupdatestate(_:).md); the central manager calls this when its state updates, thereby indicating the availability of the central manager.

## Topics

### Monitoring Connections with Peripherals
- [func centralManager(CBCentralManager, didConnect: CBPeripheral)](cbcentralmanagerdelegate/centralmanager(_:didconnect:).md)
  Tells the delegate that the central manager connected to a peripheral.
- [func centralManager(CBCentralManager, didDisconnectPeripheral: CBPeripheral, error: (any Error)?)](cbcentralmanagerdelegate/centralmanager(_:diddisconnectperipheral:error:).md)
  Tells the delegate that the central manager disconnected from a peripheral.
- [func centralManager(CBCentralManager, didFailToConnect: CBPeripheral, error: (any Error)?)](cbcentralmanagerdelegate/centralmanager(_:didfailtoconnect:error:).md)
  Tells the delegate the central manager failed to create a connection with a peripheral.
- [func centralManager(CBCentralManager, connectionEventDidOccur: CBConnectionEvent, for: CBPeripheral)](cbcentralmanagerdelegate/centralmanager(_:connectioneventdidoccur:for:).md)
  Tells the delegate that a connection event occurred which matches the registered options.
### Discovering and Retrieving Peripherals
- [func centralManager(CBCentralManager, didDiscover: CBPeripheral, advertisementData: [String : Any], rssi: NSNumber)](cbcentralmanagerdelegate/centralmanager(_:diddiscover:advertisementdata:rssi:).md)
  Tells the delegate the central manager discovered a peripheral while scanning for devices.
- [Advertisement Data Retrieval Keys](advertisement-data-retrieval-keys.md)
  Keys used to specify items in a dictionary of peripheral advertisement data.
### Monitoring the Central Manager’s State
- [func centralManagerDidUpdateState(CBCentralManager)](cbcentralmanagerdelegate/centralmanagerdidupdatestate(_:).md)
  Tells the delegate the central manager’s state updated.
- [func centralManager(CBCentralManager, willRestoreState: [String : Any])](cbcentralmanagerdelegate/centralmanager(_:willrestorestate:).md)
  Tells the delegate the system is about to restore the central manager, as part of relaunching the app into the background.
### Monitoring the Central Manager’s Authorization
- [func centralManager(CBCentralManager, didUpdateANCSAuthorizationFor: CBPeripheral)](cbcentralmanagerdelegate/centralmanager(_:didupdateancsauthorizationfor:).md)
  Tells the delegate the authorization status changed for a ANCS-requiring connected peripheral.
### Instance Methods
- [func centralManager(CBCentralManager, didDisconnectPeripheral: CBPeripheral, timestamp: CFAbsoluteTime, isReconnecting: Bool, error: (any Error)?)](cbcentralmanagerdelegate/centralmanager(_:diddisconnectperipheral:timestamp:isreconnecting:error:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CBCentral](cbcentral.md)
  A remote device connected to a local app, which is acting as a peripheral.
- [class CBCentralManager](cbcentralmanager.md)
  An object that scans for, discovers, connects to, and manages peripherals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate)*