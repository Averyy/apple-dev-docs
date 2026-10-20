# CarKeyRemoteControlSessionDelegate

**Framework**: CarKey  
**Kind**: protocol  
**Role**: Protocol

An interface you use to receive session- and vehicle-related information from the system.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
protocol CarKeyRemoteControlSessionDelegate
```

#### Overview

The system uses the [`CarKeyRemoteControlSessionDelegate`](./carkeyremotecontrolsessiondelegate.md) protocol to notify your app asynchronously when something happens. Adopt this protocol in one of your objects and detect when the system invalidates the session. If your vehicle is capable of sending data to your app, you also use this protocol to receive any data the vehicle sends.

## Topics

### Receiving Data from the Vehicle
- [func remoteControlSession(CarKeyRemoteControlSession, vehicleDidUpdateReport: VehicleReport)](./carkeyremotecontrolsessiondelegate/remotecontrolsession%28_,vehicledidupdatereport%29.md)
  Notifies your delegate object that the status of the specified vehicle changed.
- [func remoteControlSession(CarKeyRemoteControlSession, didReceivePassthroughData: Data, fromVehicle: String)](./carkeyremotecontrolsessiondelegate/remotecontrolsession%28_,didreceivepassthroughdata,fromvehicle%29.md)
  Notifies the delegate object that the vehicle sent passthrough data for you to handle.
### Handling Session Invalidation
- [func remoteControlSession(CarKeyRemoteControlSession, didInvalidateWithError: CarKeyErrorCode)](./carkeyremotecontrolsessiondelegate/remotecontrolsession%28_,didinvalidatewitherror%29.md)
  Notifies your delegate object that the session become invalid for the specified reason.
### Instance Methods
- [func remoteControlSession(CarKeyRemoteControlSession, didCreateKey: String, forVehicle: String)](./carkeyremotecontrolsessiondelegate/remotecontrolsession%28_,didcreatekey,forvehicle%29.md)
  Called to notify your app when a new key has been created.

## See Also

### Setup
- [class CarKeyRemoteControl](./carkeyremotecontrol.md)
  The object you use to start a new vehicle-related session.
- [class CarKeyRemoteControlSession](./carkeyremotecontrolsession.md)
  The object that manages communication with the vehicles you manufacture.
- [struct VehicleReport](./vehiclereport.md)
  A type that contains information about a vehicle configured for remote keyless entry in the user’s Apple Wallet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/carkeyremotecontrolsessiondelegate)*