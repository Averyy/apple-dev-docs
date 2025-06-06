# CBPeripheralDelegate

**Framework**: Core Bluetooth  
**Kind**: protocol

A protocol that provides updates on the use of a peripheral’s services.

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
protocol CBPeripheralDelegate : NSObjectProtocol
```

#### Overview

The delegate of a [`CBPeripheral`](cbperipheral.md) object must adopt the [`CBPeripheralDelegate`](cbperipheraldelegate.md) protocol. The delegate uses this protocol’s methods to monitor the discovery, exploration, and interaction of a remote peripheral’s services and properties. This protocol doesn’t have any required methods.

## Topics

### Discovering Services
- [func peripheral(CBPeripheral, didDiscoverServices: (any Error)?)](cbperipheraldelegate/peripheral(_:diddiscoverservices:).md)
  Tells the delegate that peripheral service discovery succeeded.
- [func peripheral(CBPeripheral, didDiscoverIncludedServicesFor: CBService, error: (any Error)?)](cbperipheraldelegate/peripheral(_:diddiscoverincludedservicesfor:error:).md)
  Tells the delegate that discovering included services within the indicated service completed.
### Discovering Characteristics and their Descriptors
- [func peripheral(CBPeripheral, didDiscoverCharacteristicsFor: CBService, error: (any Error)?)](cbperipheraldelegate/peripheral(_:diddiscovercharacteristicsfor:error:).md)
  Tells the delegate that the peripheral found characteristics for a service.
- [func peripheral(CBPeripheral, didDiscoverDescriptorsFor: CBCharacteristic, error: (any Error)?)](cbperipheraldelegate/peripheral(_:diddiscoverdescriptorsfor:error:).md)
  Tells the delegate that the peripheral found descriptors for a characteristic.
### Retrieving Characteristic and Descriptor Values
- [func peripheral(CBPeripheral, didUpdateValueFor: CBCharacteristic, error: (any Error)?)](cbperipheraldelegate/peripheral(_:didupdatevaluefor:error:)-1xyna.md)
  Tells the delegate that retrieving the specified characteristic’s value succeeded, or that the characteristic’s value changed.
- [func peripheral(CBPeripheral, didUpdateValueFor: CBDescriptor, error: (any Error)?)](cbperipheraldelegate/peripheral(_:didupdatevaluefor:error:)-1t3wm.md)
  Tells the delegate that retrieving a specified characteristic descriptor’s value succeeded.
### Writing Characteristic and Descriptor Values
- [func peripheral(CBPeripheral, didWriteValueFor: CBCharacteristic, error: (any Error)?)](cbperipheraldelegate/peripheral(_:didwritevaluefor:error:)-4f5ea.md)
  Tells the delegate that the peripheral successfully set a value for the characteristic.
- [func peripheral(CBPeripheral, didWriteValueFor: CBDescriptor, error: (any Error)?)](cbperipheraldelegate/peripheral(_:didwritevaluefor:error:)-1ybl3.md)
  Tells the delegate that the peripheral successfully set a value for the descriptor.
- [func peripheralIsReady(toSendWriteWithoutResponse: CBPeripheral)](cbperipheraldelegate/peripheralisready(tosendwritewithoutresponse:).md)
  Tells the delegate that a peripheral is again ready to send characteristic updates.
### Managing Notifications for a Characteristic’s Value
- [func peripheral(CBPeripheral, didUpdateNotificationStateFor: CBCharacteristic, error: (any Error)?)](cbperipheraldelegate/peripheral(_:didupdatenotificationstatefor:error:).md)
  Tells the delegate that the peripheral received a request to start or stop providing notifications for a specified characteristic’s value.
### Retrieving a Peripheral’s RSSI Data
- [func peripheral(CBPeripheral, didReadRSSI: NSNumber, error: (any Error)?)](cbperipheraldelegate/peripheral(_:didreadrssi:error:).md)
  Tells the delegate that retrieving the value of the peripheral’s current Received Signal Strength Indicator (RSSI) succeeded.
- [func peripheralDidUpdateRSSI(CBPeripheral, error: (any Error)?)](cbperipheraldelegate/peripheraldidupdaterssi(_:error:).md)
  Tells the delegate that retrieving the value of the peripheral’s current Received Signal Strength Indicator (RSSI) succeeded.
### Monitoring Changes to a Peripheral’s Name or Services
- [func peripheralDidUpdateName(CBPeripheral)](cbperipheraldelegate/peripheraldidupdatename(_:).md)
  Tells the delegate that a peripheral’s name changed.
- [func peripheral(CBPeripheral, didModifyServices: [CBService])](cbperipheraldelegate/peripheral(_:didmodifyservices:).md)
  Tells the delegate that a peripheral’s services changed.
### Monitoring L2CAP Channels
- [func peripheral(CBPeripheral, didOpen: CBL2CAPChannel?, error: (any Error)?)](cbperipheraldelegate/peripheral(_:didopen:error:).md)
  Delivers the result of an attempt to open an L2CAP channel.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CBPeripheral](cbperipheral.md)
  A remote peripheral device.
- [class CBPeripheralManager](cbperipheralmanager.md)
  An object that manages and advertises peripheral services exposed by this app.
- [protocol CBPeripheralManagerDelegate](cbperipheralmanagerdelegate.md)
  A protocol that provides updates for local peripheral state and interactions with remote central devices.
- [class CBAttribute](cbattribute.md)
  A representation of common aspects of services offered by a peripheral.
- [struct CBAttributePermissions](cbattributepermissions.md)
  Values that represent the read, write, and encryption permissions for a characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate)*