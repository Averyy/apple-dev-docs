# CBCentralManager

**Framework**: Core Bluetooth  
**Kind**: class

An object that scans for, discovers, connects to, and manages peripherals.

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
class CBCentralManager
```

#### Overview

[`CBCentralManager`](cbcentralmanager.md) objects manage discovered or connected remote peripheral devices (represented by [`CBPeripheral`](cbperipheral.md) objects), including scanning for, discovering, and connecting to advertising peripherals.

Before calling the [`CBCentralManager`](cbcentralmanager.md) methods, set the state of the central manager object to powered on, as indicated by the [`CBCentralManagerState.poweredOn`](cbcentralmanagerstate/poweredon.md) constant. This state indicates that the central device (your iPhone or iPad, for instance) supports Bluetooth low energy and that Bluetooth is on and available for use.

## Topics

### Initializing a Central Manager
- [convenience init()](cbcentralmanager/init.md)
  Initializes the central manager without a delegate.
- [convenience init(delegate: (any CBCentralManagerDelegate)?, queue: dispatch_queue_t?)](cbcentralmanager/init(delegate:queue:).md)
  Initializes the central manager with a specified delegate and dispatch queue.
- [init(delegate: (any CBCentralManagerDelegate)?, queue: dispatch_queue_t?, options: [String : Any]?)](cbcentralmanager/init(delegate:queue:options:).md)
  Initializes the central manager with specified delegate, dispatch queue, and initialization options.
- [Central Manager Initialization Options](central-manager-initialization-options.md)
  Keys used to pass options when initializing a central manager.
- [Central Manager State Restoration Options](central-manager-state-restoration-options.md)
  Keys used to pass state restoration options to the central manager initializer.
### Establishing or Canceling Connections with Peripherals
- [func connect(CBPeripheral, options: [String : Any]?)](cbcentralmanager/connect(_:options:).md)
  Establishes a local connection to a peripheral.
- [Peripheral Connection Options](peripheral-connection-options.md)
  Keys used to pass options when connecting to a peripheral.
- [func cancelPeripheralConnection(CBPeripheral)](cbcentralmanager/cancelperipheralconnection(_:).md)
  Cancels an active or pending local connection to a peripheral.
### Retrieving Lists of Peripherals
- [func retrieveConnectedPeripherals(withServices: [CBUUID]) -> [CBPeripheral]](cbcentralmanager/retrieveconnectedperipherals(withservices:).md)
  Returns a list of the peripherals connected to the system whose services match a given set of criteria.
- [func retrievePeripherals(withIdentifiers: [UUID]) -> [CBPeripheral]](cbcentralmanager/retrieveperipherals(withidentifiers:).md)
  Returns a list of known peripherals by their identifiers.
### Scanning or Stopping Scans of Peripherals
- [func scanForPeripherals(withServices: [CBUUID]?, options: [String : Any]?)](cbcentralmanager/scanforperipherals(withservices:options:).md)
  Scans for peripherals that are advertising services.
- [Peripheral Scanning Options](peripheral-scanning-options.md)
  Keys used to pass options when scanning for peripherals.
- [func stopScan()](cbcentralmanager/stopscan.md)
  Asks the central manager to stop scanning for peripherals.
- [var isScanning: Bool](cbcentralmanager/isscanning.md)
  A Boolean value that indicates whether the central is currently scanning.
### Inspecting Feature Support
- [class func supports(CBCentralManager.Feature) -> Bool](cbcentralmanager/supports(_:).md)
  Returns a Boolean that indicates whether the device supports a specific set of features.
- [CBCentralManager.Feature](cbcentralmanager/feature.md)
  An option set of device-specific features.
### Monitoring Properties
- [var delegate: (any CBCentralManagerDelegate)?](cbcentralmanager/delegate.md)
  The delegate object that you want to receive central manager events.
### Receiving Connection Events
- [func registerForConnectionEvents(options: [CBConnectionEventMatchingOption : Any]?)](cbcentralmanager/registerforconnectionevents(options:).md)
  Register for an event notification when the central manager makes a connection matching the given options.
- [Peripheral Connection Options](peripheral-connection-options.md)
  Keys used to pass options when connecting to a peripheral.
- [enum CBConnectionEvent](cbconnectionevent.md)
  A change to the connection state of a peer.
- [struct CBConnectionEventMatchingOption](cbconnectioneventmatchingoption.md)
  A set of options to use when registering for connection events.
### Deprecated
- [enum CBCentralManagerState](cbcentralmanagerstate.md)
  Values that represent the current state of a central manager object.

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

- [class CBCentral](cbcentral.md)
  A remote device connected to a local app, which is acting as a peripheral.
- [protocol CBCentralManagerDelegate](cbcentralmanagerdelegate.md)
  A protocol that provides updates for the discovery and management of peripheral devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager)*