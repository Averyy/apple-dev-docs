# RemoteKeylessEntryAction

**Framework**: CarKey  
**Kind**: struct

An automatically ending action that you want to perform on a vehicle.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
struct RemoteKeylessEntryAction
```

#### Overview

Use a [`RemoteKeylessEntryAction`](remotekeylessentryaction.md) object to store details about an action that runs to completion after you start it. For example, you might use this type of action to unlock the door locks of the vehicle. The object stores information about the feature you want to control and the action to take on that feature. It also stores the identifier for the vehicle itself.

After you create a [`RemoteKeylessEntryAction`](remotekeylessentryaction.md) object, call your session’s [`perform(_:)`](carkeyremotecontrolsession/perform(_:)-8ac0c.md) method to execute the action. Use the returned [`RemoteKeylessEntryAction.ExecutionRequest`](remotekeylessentryaction/executionrequest.md) object to determine the success or failure of the request.

## Topics

### Creating the Action Request
- [init(functionID: FunctionIdentifier, actionID: ActionIdentifier, vehicleID: String)](remotekeylessentryaction/init(functionid:actionid:vehicleid:).md)
  Creates a new action object with the specified action-specific details and vehicle ID.
### Receiving the Action’s Response
- [RemoteKeylessEntryAction.ExecutionRequest](remotekeylessentryaction/executionrequest.md)
  An object that reports the results of an automatically ending action asynchronously.
### Getting the Action Details
- [let functionID: FunctionIdentifier](remotekeylessentryaction/functionid.md)
  The vehicle-specific code that identifies which feature you want to control.
- [let actionID: ActionIdentifier](remotekeylessentryaction/actionid.md)
  The vehicle-specific code that identifies what action to take on the targeted feature.
- [let recipientVehicleID: String](remotekeylessentryaction/recipientvehicleid.md)
  The vehicle to receive the action request.

## See Also

- [struct RemoteKeylessEntryEnduringAction](remotekeylessentryenduringaction.md)
  An action with an optional stopping point that you want to perform on a vehicle.
- [struct FunctionIdentifier](functionidentifier.md)
  A type that stores the designation code for one of your vehicle’s features.
- [struct ActionIdentifier](actionidentifier.md)
  A type that stores the designation code for one of the actions that a vehicle feature supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/remotekeylessentryaction)*