# CarKeyRemoteControlSession

**Framework**: CarKey  
**Kind**: class  
**Role**: Class

The object that manages communication with the vehicles you manufacture.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
class CarKeyRemoteControlSession
```

#### Overview

A `CarKeyRemoteControlSession` object coordinates interactions between your app and your company’s make of vehicles. This object works with the system to transmit data securely to and from a vehicle, and to report results back to your app. Use this object to send commands or data directly to a vehicle, and to get information about the available vehicles and their current configuration.

Don’t create this object directly. Instead, call the [`start(delegate:subscriptionRange:with:)`](./carkeyremotecontrol/start%28delegate,subscriptionrange,with%29.md) method to create a new session object. When you finish interacting with the vehicle, call the session’s [`end()`](./carkeyremotecontrolsession/end%28%29.md) method to close out the session and prevent further access. You can have only one active session at a time. If you try to start a second session, [`start(delegate:subscriptionRange:with:)`](./carkeyremotecontrol/start%28delegate,subscriptionrange,with%29.md) doesn’t return until the currently active session becomes invalid.

When you configure a new session, provide a delegate object to receive data from vehicle-initiated transfers. The system also uses your delegate notify you when the configuration of a vehicle changes. For example, it lets you know when connectivity to the vehicle changes. The delegate must adopt the [`CarKeyRemoteControlSessionDelegate`](./carkeyremotecontrolsessiondelegate.md) protocol.

> **Note**: If your app has an active session, the system automatically ends that session when your app enters the background. Upon reentering the foreground, you must create a new session to communicate with your vehicle again.

## Topics

### Performing Vehicle-Related Actions
- [func perform(RemoteKeylessEntryAction) throws -> RemoteKeylessEntryAction.ExecutionRequest](./carkeyremotecontrolsession/perform%28_%29-8ac0c.md)
  Sends a request to the vehicle to perform a one-time action.
- [func perform(RemoteKeylessEntryEnduringAction) throws -> RemoteKeylessEntryEnduringAction.EnduringExecutionRequest](./carkeyremotecontrolsession/perform%28_%29-7mpsy.md)
  Sends a request to the vehicle to start an action that has a separate stopping point.
### Sending Data to the Vehicle
- [func sendPassthroughData(Data, toVehicle: String) throws](./carkeyremotecontrolsession/sendpassthroughdata%28_,tovehicle%29.md)
  Sends the specified custom data to the vehicle.
### Closing the Session
- [func end() throws](./carkeyremotecontrolsession/end%28%29.md)
  Ends the session and stops the delivery of notifications for all vehicles in the session.
### Getting Vehicle Information
- [var vehicleReports: [VehicleReport]](./carkeyremotecontrolsession/vehiclereports.md)
  The configuration details of the provisioned vehicles that match your company’s make.
- [func isPassiveEntryAvailable(forVehicle: String) throws -> Bool](./carkeyremotecontrolsession/ispassiveentryavailable%28forvehicle%29.md)
  Returns a Boolean value that indicates whether passive entry is currently available for the specified vehicle.
### Structures
- [CarKeyRemoteControlSession.Attestation](./carkeyremotecontrolsession/attestation.md)
  Object representing an attestation and related data
### Instance Methods
- [func perform(RemoteKeylessEntryConfigurableEnduringAction, continuationStrategy: CarKeyRemoteControlSession.ContinuationStrategy) throws -> RemoteKeylessEntryConfigurableEnduringAction.EnduringExecutionRequest](./carkeyremotecontrolsession/perform%28_,continuationstrategy%29.md)
  Sends a request to the vehicle to start an action that has a separate stopping point, and optionally allows your app to have control over incoming continuation requests and to exchange data during the execution of the action.
- [func sign(data: Data, forVehicle: String) throws -> CarKeyRemoteControlSession.Attestation](./carkeyremotecontrolsession/sign%28data,forvehicle%29.md)
  Sign data with the endpoint.SK identified by vehicleIdentifier as described in the section “OEM App Data Attestation” of the Car Connectivity Consortium Digital Key Release 3.0 specification.
### Enumerations
- [CarKeyRemoteControlSession.ContinuationStrategy](./carkeyremotecontrolsession/continuationstrategy.md)
  Strategy to use on reception of a continuation request.

## See Also

### Setup
- [class CarKeyRemoteControl](./carkeyremotecontrol.md)
  The object you use to start a new vehicle-related session.
- [protocol CarKeyRemoteControlSessionDelegate](./carkeyremotecontrolsessiondelegate.md)
  An interface you use to receive session- and vehicle-related information from the system.
- [struct VehicleReport](./vehiclereport.md)
  A type that contains information about a vehicle configured for remote keyless entry in the user’s Apple Wallet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/carkeyremotecontrolsession)*