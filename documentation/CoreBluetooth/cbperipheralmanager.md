# CBPeripheralManager

**Framework**: Core Bluetooth  
**Kind**: class

An object that manages and advertises peripheral services exposed by this app.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CBPeripheralManager
```

#### Overview

Core Bluetooth uses [`CBPeripheralManager`](cbperipheralmanager.md) objects to manage published services within the local peripheral’s Generic Attribute Profile (GATT) database and to advertise these services to central devices (represented by [`CBCentral`](cbcentral.md) objects). While a service is in the database, any connected central can see and connect to it. That said, if your app hasn’t specified the `bluetooth-peripheral` background mode, the contents of its services become disabled when it’s in the background or in a suspended state. In this scenario, any remote central trying to access the service’s characteristic value or characteristic descriptors receives an error.

Before you call [`CBPeripheralManager`](cbperipheralmanager.md) methods, the peripheral manager object must be in the powered-on state, as indicated by the [`CBPeripheralManagerState.poweredOn`](cbperipheralmanagerstate/poweredon.md). This state indicates that the device (your iPhone or iPad, for instance) supports Bluetooth low energy and that its Bluetooth is on and available for use.

In watchOS, tvOS, and visionOS, you can’t advertise services using a [`CBPeripheralManager`](cbperipheralmanager.md) object because support for doing so is unavailable.

## Topics

### Initializing a Peripheral Manager
- [convenience init()](cbperipheralmanager/init.md)
  Initializes the peripheral manager without a delegate.
- [convenience init(delegate: (any CBPeripheralManagerDelegate)?, queue: dispatch_queue_t?)](cbperipheralmanager/init(delegate:queue:).md)
  Initializes the peripheral manager with a specified delegate and dispatch queue.
- [init(delegate: (any CBPeripheralManagerDelegate)?, queue: dispatch_queue_t?, options: [String : Any]?)](cbperipheralmanager/init(delegate:queue:options:).md)
  Initializes the peripheral manager with a specified delegate, dispatch queue, and initialization options.
- [var delegate: (any CBPeripheralManagerDelegate)?](cbperipheralmanager/delegate.md)
  The delegate object specified to receive peripheral events.
- [Peripheral Manager Initialization Options](peripheral-manager-initialization-options.md)
  Keys used to specify options when creating a peripheral manager.
### Monitoring the State of a Peripheral Manager
- [class func authorizationStatus() -> CBPeripheralManagerAuthorizationStatus](cbperipheralmanager/authorizationstatus.md)
  Returns the app’s authorization status for sharing data while in the background.
- [enum CBPeripheralManagerAuthorizationStatus](cbperipheralmanagerauthorizationstatus.md)
  Values representing the current authorization state of the peripheral manager.
- [enum CBPeripheralManagerState](cbperipheralmanagerstate.md)
  Values that represent the current state of the peripheral manager.
### Adding and Removing Services
- [func add(CBMutableService)](cbperipheralmanager/add(_:).md)
  Publishes a service and any of its associated characteristics and characteristic descriptors to the local GATT database.
- [func remove(CBMutableService)](cbperipheralmanager/remove(_:).md)
  Removes a specified published service from the local GATT database.
- [func removeAllServices()](cbperipheralmanager/removeallservices.md)
  Removes all published services from the local GATT database.
### Managing Advertising
- [func startAdvertising([String : Any]?)](cbperipheralmanager/startadvertising(_:).md)
  Advertises peripheral manager data.
- [Advertising Data](advertising-data.md)
- [func stopAdvertising()](cbperipheralmanager/stopadvertising.md)
  Stops advertising peripheral manager data.
- [var isAdvertising: Bool](cbperipheralmanager/isadvertising.md)
  A Boolean value that indicates whether the peripheral is advertising data.
### Sending Updates of a Characteristic’s Value
- [func updateValue(Data, for: CBMutableCharacteristic, onSubscribedCentrals: [CBCentral]?) -> Bool](cbperipheralmanager/updatevalue(_:for:onsubscribedcentrals:).md)
  Send an updated characteristic value to one or more subscribed centrals, using a notification or indication.
### Responding to Read and Write Requests
- [func respond(to: CBATTRequest, withResult: CBATTError.Code)](cbperipheralmanager/respond(to:withresult:).md)
  Responds to a read or write request from a connected central.
### Setting Connection Latency
- [func setDesiredConnectionLatency(CBPeripheralManagerConnectionLatency, for: CBCentral)](cbperipheralmanager/setdesiredconnectionlatency(_:for:).md)
  Sets the desired connection latency for an existing connection to a central device.
- [enum CBPeripheralManagerConnectionLatency](cbperipheralmanagerconnectionlatency.md)
  Values representing the connection latency of the peripheral manager.
### Using L2CAP Channels
- [func publishL2CAPChannel(withEncryption: Bool)](cbperipheralmanager/publishl2capchannel(withencryption:).md)
  Creates a listener for incoming L2CAP channel connections.
- [func unpublishL2CAPChannel(CBL2CAPPSM)](cbperipheralmanager/unpublishl2capchannel(_:).md)
  Removes a published service from the local system.

## Relationships

### Inherits From
- [CBManager](cbmanager.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CBPeripheral](cbperipheral.md)
  A remote peripheral device.
- [protocol CBPeripheralDelegate](cbperipheraldelegate.md)
  A protocol that provides updates on the use of a peripheral’s services.
- [protocol CBPeripheralManagerDelegate](cbperipheralmanagerdelegate.md)
  A protocol that provides updates for local peripheral state and interactions with remote central devices.
- [class CBAttribute](cbattribute.md)
  A representation of common aspects of services offered by a peripheral.
- [struct CBAttributePermissions](cbattributepermissions.md)
  Values that represent the read, write, and encryption permissions for a characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager)*