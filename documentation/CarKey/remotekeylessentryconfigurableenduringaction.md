# RemoteKeylessEntryConfigurableEnduringAction

**Framework**: CarKey  
**Kind**: struct

An action with an optional stopping point that you want to perform on a vehicle.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
struct RemoteKeylessEntryConfigurableEnduringAction
```

#### Overview

Use a [`RemoteKeylessEntryConfigurableEnduringAction`](remotekeylessentryconfigurableenduringaction.md) object to store details about an action that you can stop or let run to completion. For example, you might use this type of action to lower or raise the top of a convertible vehicle. The object stores information about the vehicle feature to control and the action to take on that feature. It also stores the identifier for the vehicle itself.

After you create a [`RemoteKeylessEntryConfigurableEnduringAction`](remotekeylessentryconfigurableenduringaction.md) object, call your session’s [`perform(_:)`](carkeyremotecontrolsession/perform(_:)-7mpsy.md) method to execute the action. Use the returned [`RemoteKeylessEntryAction.ExecutionRequest`](remotekeylessentryaction/executionrequest.md) object to determine the success or failure of the request.

## Topics

### Classes
- [RemoteKeylessEntryConfigurableEnduringAction.EnduringExecutionRequest](remotekeylessentryconfigurableenduringaction/enduringexecutionrequest.md)
  An object that reports the results of an action with an optional stopping point.
### Initializers
- [init(functionID: FunctionIdentifier, actionID: ActionIdentifier, vehicleID: String)](remotekeylessentryconfigurableenduringaction/init(functionid:actionid:vehicleid:).md)
  Creates a new action object with the specified action-specific details and vehicle ID.
### Instance Properties
- [let actionID: ActionIdentifier](remotekeylessentryconfigurableenduringaction/actionid.md)
  The vehicle-specific code that identifies what action to take on the targeted feature.
- [let functionID: FunctionIdentifier](remotekeylessentryconfigurableenduringaction/functionid.md)
  The vehicle-specific code that identifies which feature you want to control.
- [let recipientVehicleID: String](remotekeylessentryconfigurableenduringaction/recipientvehicleid.md)
  The vehicle to receive the action request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/remotekeylessentryconfigurableenduringaction)*