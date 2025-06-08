# Core Bluetooth

**Framework**: Core Bluetooth  
**Kind**: module

Communicate with Bluetooth low energy and BR/EDR (“Classic”) Devices.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

#### Overview

The Core Bluetooth framework provides the classes needed for your apps to communicate with Bluetooth-equipped low energy (LE) and Basic Rate / Enhanced Data Rate (BR/EDR) wireless technology.

Don’t subclass any of the classes of the Core Bluetooth framework. Overriding these classes isn’t supported and results in undefined behavior.

Core Bluetooth background execution modes aren’t supported in iPad apps running on macOS.

> ❗ **Important**:  Your app will crash if its `Info.plist` doesn’t include usage description keys for the types of data it needs to access. To access Core Bluetooth APIs on apps linked on or after iOS 13, include the [`NSBluetoothAlwaysUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBluetoothAlwaysUsageDescription) key. In iOS 12 and earlier, include [`NSBluetoothPeripheralUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBluetoothPeripheralUsageDescription) to access Bluetooth peripheral data.

## Topics

### Centrals
- [class CBCentral](cbcentral.md)
  A remote device connected to a local app, which is acting as a peripheral.
- [class CBCentralManager](cbcentralmanager.md)
  An object that scans for, discovers, connects to, and manages peripherals.
- [protocol CBCentralManagerDelegate](cbcentralmanagerdelegate.md)
  A protocol that provides updates for the discovery and management of peripheral devices.
### Peripherals
- [class CBPeripheral](cbperipheral.md)
  A remote peripheral device.
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
### Data Transfer
- [Transferring Data Between Bluetooth Low Energy Devices](transferring-data-between-bluetooth-low-energy-devices.md)
  Create a Bluetooth low energy central and peripheral device, and allow them to discover each other and exchange data.
### Services
- [class CBService](cbservice.md)
  A collection of data and associated behaviors that accomplish a function or feature of a device.
- [class CBMutableService](cbmutableservice.md)
  A service with writeable property values.
- [class CBCharacteristic](cbcharacteristic.md)
  A characteristic of a remote peripheral’s service.
- [class CBMutableCharacteristic](cbmutablecharacteristic.md)
  A characteristic of a local peripheral’s service.
- [class CBDescriptor](cbdescriptor.md)
  An object that provides further information about a remote peripheral’s characteristic.
- [class CBMutableDescriptor](cbmutabledescriptor.md)
  An object that provides additional information about a local peripheral’s characteristic.
### Supporting Types
- [class CBManager](cbmanager.md)
  The abstract base class that manages central and peripheral objects.
- [class CBATTRequest](cbattrequest.md)
  A request that uses the Attribute Protocol (ATT).
- [class CBPeer](cbpeer.md)
  An object that represents a remote device.
- [class CBUUID](cbuuid.md)
  A universally unique identifier, as defined by Bluetooth standards.
### Bluetooth Classic Support
- [Using Core Bluetooth Classic](using-core-bluetooth-classic.md)
  Discover and communicate with a Bluetooth Classic device by using the Core Bluetooth APIs.
### Errors
- [struct CBError](cberror-swift.struct.md)
  An error that Core Bluetooth returns during Bluetooth transactions.
- [let CBErrorDomain: String](cberrordomain.md)
  The domain for Core Bluetooth errors.
- [CBError.Code](cberror-swift.struct/code.md)
  The codes for errors that Core Bluetooth returns during Bluetooth transactions.
- [struct CBATTError](cbatterror-swift.struct.md)
  An error that Core Bluetooth returns while using Attribute Protocol (ATT).
- [let CBATTErrorDomain: String](cbatterrordomain.md)
  The domain for Core Bluetooth ATT errors.
- [CBATTError.Code](cbatterror-swift.struct/code.md)
  The possible errors returned by a GATT server (a remote peripheral) during Bluetooth low energy ATT transactions.
- [struct CBATTError](cbatterror-swift.struct.md)
  An error that Core Bluetooth returns while using Attribute Protocol (ATT).
### Deprecated
- [enum CBCentralManagerState](cbcentralmanagerstate.md)
  Values that represent the current state of a central manager object.
- [enum CBPeripheralManagerState](cbperipheralmanagerstate.md)
  Values that represent the current state of the peripheral manager.
- [Deprecated Constants](deprecated-constants.md)
  This document describes the constants found in the Core Bluetooth framework.
### Variables
- [let CBUUIDCharacteristicObservationScheduleString: String](cbuuidcharacteristicobservationschedulestring.md)

## See Also

- [Core Bluetooth Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreBluetooth)*