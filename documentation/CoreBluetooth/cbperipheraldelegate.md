# CBPeripheralDelegate

**Framework**: Core Bluetooth  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol CBPeripheralDelegate <NSObject>
```

## Overview

The delegate of a [`CBPeripheral`](./cbperipheral.md) object must adopt the [`CBPeripheralDelegate`](./cbperipheraldelegate.md) protocol. The delegate uses this protocol’s methods to monitor the discovery, exploration, and interaction of a remote peripheral’s services and properties. This protocol doesn’t have any required methods.

## Topics

### Discovering Services
- [func peripheral(CBPeripheral, didDiscoverServices: (any Error)?)](./cbperipheraldelegate/peripheral%28_,diddiscoverservices%29.md)
  Tells the delegate that peripheral service discovery succeeded.
- [func peripheral(CBPeripheral, didDiscoverIncludedServicesFor: CBService, error: (any Error)?)](./cbperipheraldelegate/peripheral%28_,diddiscoverincludedservicesfor,error%29.md)
  Tells the delegate that discovering included services within the indicated service completed.
### Discovering Characteristics and their Descriptors
- [func peripheral(CBPeripheral, didDiscoverCharacteristicsFor: CBService, error: (any Error)?)](./cbperipheraldelegate/peripheral%28_,diddiscovercharacteristicsfor,error%29.md)
  Tells the delegate that the peripheral found characteristics for a service.
- [func peripheral(CBPeripheral, didDiscoverDescriptorsFor: CBCharacteristic, error: (any Error)?)](./cbperipheraldelegate/peripheral%28_,diddiscoverdescriptorsfor,error%29.md)
  Tells the delegate that the peripheral found descriptors for a characteristic.
### Retrieving Characteristic and Descriptor Values
- [func peripheral(CBPeripheral, didUpdateValueFor: CBCharacteristic, error: (any Error)?)](./cbperipheraldelegate/peripheral%28_,didupdatevaluefor,error%29-1xyna.md)
  Tells the delegate that retrieving the specified characteristic’s value succeeded, or that the characteristic’s value changed.
- [func peripheral(CBPeripheral, didUpdateValueFor: CBDescriptor, error: (any Error)?)](./cbperipheraldelegate/peripheral%28_,didupdatevaluefor,error%29-1t3wm.md)
  Tells the delegate that retrieving a specified characteristic descriptor’s value succeeded.
### Writing Characteristic and Descriptor Values
- [func peripheral(CBPeripheral, didWriteValueFor: CBCharacteristic, error: (any Error)?)](./cbperipheraldelegate/peripheral%28_,didwritevaluefor,error%29-4f5ea.md)
  Tells the delegate that the peripheral successfully set a value for the characteristic.
- [func peripheral(CBPeripheral, didWriteValueFor: CBDescriptor, error: (any Error)?)](./cbperipheraldelegate/peripheral%28_,didwritevaluefor,error%29-1ybl3.md)
  Tells the delegate that the peripheral successfully set a value for the descriptor.
- [func peripheralIsReady(toSendWriteWithoutResponse: CBPeripheral)](./cbperipheraldelegate/peripheralisready%28tosendwritewithoutresponse%29.md)
  Tells the delegate that a peripheral is again ready to send characteristic updates.
### Managing Notifications for a Characteristic’s Value
- [func peripheral(CBPeripheral, didUpdateNotificationStateFor: CBCharacteristic, error: (any Error)?)](./cbperipheraldelegate/peripheral%28_,didupdatenotificationstatefor,error%29.md)
  Tells the delegate that the peripheral received a request to start or stop providing notifications for a specified characteristic’s value.
### Retrieving a Peripheral’s RSSI Data
- [func peripheral(CBPeripheral, didReadRSSI: NSNumber, error: (any Error)?)](./cbperipheraldelegate/peripheral%28_,didreadrssi,error%29.md)
  Tells the delegate that retrieving the value of the peripheral’s current Received Signal Strength Indicator (RSSI) succeeded.
- [func peripheralDidUpdateRSSI(CBPeripheral, error: (any Error)?)](./cbperipheraldelegate/peripheraldidupdaterssi%28_,error%29.md)
  Tells the delegate that retrieving the value of the peripheral’s current Received Signal Strength Indicator (RSSI) succeeded.
### Monitoring Changes to a Peripheral’s Name or Services
- [func peripheralDidUpdateName(CBPeripheral)](./cbperipheraldelegate/peripheraldidupdatename%28_%29.md)
  Tells the delegate that a peripheral’s name changed.
- [func peripheral(CBPeripheral, didModifyServices: [CBService])](./cbperipheraldelegate/peripheral%28_,didmodifyservices%29.md)
  Tells the delegate that a peripheral’s services changed.
### Monitoring L2CAP Channels
- [func peripheral(CBPeripheral, didOpen: CBL2CAPChannel?, error: (any Error)?)](./cbperipheraldelegate/peripheral%28_,didopen,error%29.md)
  Delivers the result of an attempt to open an L2CAP channel.
### Instance Methods
- [func peripheral(CBPeripheral, didCompleteChannelSoundingSession: (any Error)?)](./cbperipheraldelegate/peripheral%28_,didcompletechannelsoundingsession%29.md)
- [func peripheral(CBPeripheral, didReceive: CBChannelSoundingProcedureResults?, error: (any Error)?)](./cbperipheraldelegate/peripheral%28_,didreceive,error%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Peripherals
- [class CBPeripheral](./cbperipheral.md)
  A remote peripheral device.
- [class CBPeripheralManager](./cbperipheralmanager.md)
  An object that manages and advertises peripheral services exposed by this app.
- [protocol CBPeripheralManagerDelegate](./cbperipheralmanagerdelegate.md)
  A protocol that provides updates for local peripheral state and interactions with remote central devices.
- [class CBAttribute](./cbattribute.md)
  A representation of common aspects of services offered by a peripheral.
- [struct CBAttributePermissions](./cbattributepermissions.md)
  Values that represent the read, write, and encryption permissions for a characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate)*