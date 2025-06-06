# CBPeripheralManagerDelegate

**Framework**: Core Bluetooth  
**Kind**: protocol

A protocol that provides updates for local peripheral state and interactions with remote central devices.

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
protocol CBPeripheralManagerDelegate : NSObjectProtocol
```

#### Overview

The delegate of a [`CBPeripheralManager`](cbperipheralmanager.md) object must adopt the [`CBPeripheralManagerDelegate`](cbperipheralmanagerdelegate.md) protocol, which consists of numerous optional methods and one required method. The delegate uses the protocol’s optional methods to verify publishing and advertising, and to monitor read, write, and subscription requests from remote central devices.

The protocol’s required one method, [`peripheralManagerDidUpdateState(_:)`](cbperipheralmanagerdelegate/peripheralmanagerdidupdatestate(_:).md), which Core Bluetooth calls whenever the peripheral manager’s state updates to indicate whether the peripheral manager is available.

## Topics

### Monitoring Changes to the Peripheral Manager’s State
- [func peripheralManagerDidUpdateState(CBPeripheralManager)](cbperipheralmanagerdelegate/peripheralmanagerdidupdatestate(_:).md)
  Tells the delegate the peripheral manager’s state updated.
- [func peripheralManager(CBPeripheralManager, willRestoreState: [String : Any])](cbperipheralmanagerdelegate/peripheralmanager(_:willrestorestate:).md)
  Tells the delegate the system is about to restore the peripheral manager.
- [Peripheral Manager State Restoration Options](peripheral-manager-state-restoration-options.md)
  Keys used to specify options when restoring the state of a peripheral manager.
### Adding Services
- [func peripheralManager(CBPeripheralManager, didAdd: CBService, error: (any Error)?)](cbperipheralmanagerdelegate/peripheralmanager(_:didadd:error:).md)
  Tells the delegate the peripheral manager published a service to the local GATT database.
### Advertising Peripheral Data
- [func peripheralManagerDidStartAdvertising(CBPeripheralManager, error: (any Error)?)](cbperipheralmanagerdelegate/peripheralmanagerdidstartadvertising(_:error:).md)
  Tells the delegate the peripheral manager started advertising the local peripheral device’s data.
### Monitoring Subscriptions to Characteristic Values
- [func peripheralManager(CBPeripheralManager, central: CBCentral, didSubscribeTo: CBCharacteristic)](cbperipheralmanagerdelegate/peripheralmanager(_:central:didsubscribeto:).md)
  Tells the delegate that a remote central device subscribed to a characteristic’s value.
- [func peripheralManager(CBPeripheralManager, central: CBCentral, didUnsubscribeFrom: CBCharacteristic)](cbperipheralmanagerdelegate/peripheralmanager(_:central:didunsubscribefrom:).md)
  Tells the delegate that a remote central device unsubscribed from a characteristic’s value.
- [func peripheralManagerIsReady(toUpdateSubscribers: CBPeripheralManager)](cbperipheralmanagerdelegate/peripheralmanagerisready(toupdatesubscribers:).md)
  Tells the delegate that a local peripheral device is ready to send characteristic value updates.
### Receiving Read and Write Requests
- [func peripheralManager(CBPeripheralManager, didReceiveRead: CBATTRequest)](cbperipheralmanagerdelegate/peripheralmanager(_:didreceiveread:).md)
  Tells the delegate that a local peripheral received an Attribute Protocol (ATT) read request for a characteristic with a dynamic value.
- [func peripheralManager(CBPeripheralManager, didReceiveWrite: [CBATTRequest])](cbperipheralmanagerdelegate/peripheralmanager(_:didreceivewrite:).md)
  Tells the delegate that a local peripheral device received an Attribute Protocol (ATT) write request for a characteristic with a dynamic value.
### Using L2CAP Channels
- [func peripheralManager(CBPeripheralManager, didPublishL2CAPChannel: CBL2CAPPSM, error: (any Error)?)](cbperipheralmanagerdelegate/peripheralmanager(_:didpublishl2capchannel:error:).md)
  Tells the delegate that the peripheral manager created a listener for incoming L2CAP channel connections.
- [func peripheralManager(CBPeripheralManager, didUnpublishL2CAPChannel: CBL2CAPPSM, error: (any Error)?)](cbperipheralmanagerdelegate/peripheralmanager(_:didunpublishl2capchannel:error:).md)
  Tells the delegate that the peripheral manager removed a published service from the local system.
- [func peripheralManager(CBPeripheralManager, didOpen: CBL2CAPChannel?, error: (any Error)?)](cbperipheralmanagerdelegate/peripheralmanager(_:didopen:error:).md)
  Tells the delegate that the peripheral manager opened an L2CAP channel.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CBPeripheral](cbperipheral.md)
  A remote peripheral device.
- [protocol CBPeripheralDelegate](cbperipheraldelegate.md)
  A protocol that provides updates on the use of a peripheral’s services.
- [class CBPeripheralManager](cbperipheralmanager.md)
  An object that manages and advertises peripheral services exposed by this app.
- [class CBAttribute](cbattribute.md)
  A representation of common aspects of services offered by a peripheral.
- [struct CBAttributePermissions](cbattributepermissions.md)
  Values that represent the read, write, and encryption permissions for a characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate)*