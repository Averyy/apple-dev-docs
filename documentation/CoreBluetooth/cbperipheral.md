# CBPeripheral

**Framework**: Core Bluetooth  
**Kind**: class

A remote peripheral device.

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
class CBPeripheral
```

#### Overview

The [`CBPeripheral`](cbperipheral.md) class represents remote peripheral devices that your app discovers with a central manager (an instance of [`CBCentralManager`](cbcentralmanager.md)). Peripherals use universally unique identifiers (UUIDs), represented by [`NSUUID`](https://developer.apple.com/documentation/Foundation/NSUUID) objects, to identify themselves. Peripherals may contain one or more services or provide useful information about their connected signal strength.

You use this class to discover, explore, and interact with the services available on a remote peripheral that supports Bluetooth low energy. A service encapsulates the way part of the device behaves. For example, one service of a heart rate monitor may be to expose heart rate data from a sensor. Services themselves contain of characteristics or included services (references to other services). Characteristics provide further details about a peripheral’s service. For example, the heart rate service may contain multiple characteristics. One characteristic could describe the intended body location of the device’s heart rate sensor, and another characteristic could transmit the heart rate measurement data. Finally, characteristics contain any number of descriptors that provide more information about the characteristic’s value, such as a human-readable description and a way to format the value.

## Topics

### Identifying a Peripheral
- [var name: String?](cbperipheral/name.md)
  The name of the peripheral.
- [var delegate: (any CBPeripheralDelegate)?](cbperipheral/delegate.md)
  The delegate object specified to receive peripheral events.
### Discovering Services
- [func discoverServices([CBUUID]?)](cbperipheral/discoverservices(_:).md)
  Discovers the specified services of the peripheral.
- [func discoverIncludedServices([CBUUID]?, for: CBService)](cbperipheral/discoverincludedservices(_:for:).md)
  Discovers the specified included services of a previously-discovered service.
- [var services: [CBService]?](cbperipheral/services.md)
  A list of a peripheral’s discovered services.
### Discovering Characteristics and Descriptors
- [func discoverCharacteristics([CBUUID]?, for: CBService)](cbperipheral/discovercharacteristics(_:for:).md)
  Discovers the specified characteristics of a service.
- [func discoverDescriptors(for: CBCharacteristic)](cbperipheral/discoverdescriptors(for:).md)
  Discovers the descriptors of a characteristic.
### Reading Characteristic and Descriptor Values
- [func readValue(for: CBCharacteristic)](cbperipheral/readvalue(for:)-6u2kr.md)
  Retrieves the value of a specified characteristic.
- [func readValue(for: CBDescriptor)](cbperipheral/readvalue(for:)-91hhp.md)
  Retrieves the value of a specified characteristic descriptor.
### Writing Characteristic and Descriptor Values
- [func writeValue(Data, for: CBCharacteristic, type: CBCharacteristicWriteType)](cbperipheral/writevalue(_:for:type:).md)
  Writes the value of a characteristic.
- [func writeValue(Data, for: CBDescriptor)](cbperipheral/writevalue(_:for:).md)
  Writes the value of a characteristic descriptor.
- [func maximumWriteValueLength(for: CBCharacteristicWriteType) -> Int](cbperipheral/maximumwritevaluelength(for:).md)
  The maximum amount of data, in bytes, you can send to a characteristic in a single write type.
- [enum CBCharacteristicWriteType](cbcharacteristicwritetype.md)
  Values representing the possible write types to a characteristic’s value.
### Setting Notifications for a Characteristic’s Value
- [func setNotifyValue(Bool, for: CBCharacteristic)](cbperipheral/setnotifyvalue(_:for:).md)
  Sets notifications or indications for the value of a specified characteristic.
### Monitoring a Peripheral’s Connection State
- [var state: CBPeripheralState](cbperipheral/state.md)
  The connection state of the peripheral.
- [enum CBPeripheralState](cbperipheralstate.md)
  Values representing the connection state of a peripheral.
- [var canSendWriteWithoutResponse: Bool](cbperipheral/cansendwritewithoutresponse.md)
  A Boolean value that indicates whether the remote device can send a write without a response.
### Accessing a Peripheral’s Signal Strength
- [func readRSSI()](cbperipheral/readrssi.md)
  Retrieves the current RSSI value for the peripheral while connected to the central manager.
- [var rssi: NSNumber?](cbperipheral/rssi.md)
  The Received Signal Strength Indicator (RSSI), in decibels, of the peripheral.
### Working with L2CAP Channels
- [func openL2CAPChannel(CBL2CAPPSM)](cbperipheral/openl2capchannel(_:).md)
  Attempts to open an L2CAP channel to the peripheral using the supplied Protocol/Service Multiplexer (PSM).
- [class CBL2CAPChannel](cbl2capchannel.md)
  A live L2CAP connection to a remote device.
- [typealias CBL2CAPPSM](cbl2cappsm.md)
  The type of PSM identifiers.
### Working with Apple Notification Center Service (ANCS)
- [var ancsAuthorized: Bool](cbperipheral/ancsauthorized.md)
  A Boolean value that indicates if the remote device has authorization to receive data over ANCS protocol.

## Relationships

### Inherits From
- [CBPeer](cbpeer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol CBPeripheralDelegate](cbperipheraldelegate.md)
  A protocol that provides updates on the use of a peripheral’s services.
- [class CBPeripheralManager](cbperipheralmanager.md)
  An object that manages and advertises peripheral services exposed by this app.
- [protocol CBPeripheralManagerDelegate](cbperipheralmanagerdelegate.md)
  A protocol that provides updates for local peripheral state and interactions with remote central devices.
- [class CBAttribute](cbattribute.md)
  A representation of common aspects of services offered by a peripheral.
- [struct CBAttributePermissions](cbattributepermissions.md)
  Values that represent the read, write, and encryption permissions for a characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral)*