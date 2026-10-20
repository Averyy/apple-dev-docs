# RemoteKeylessEntryEnduringAction

**Framework**: CarKey  
**Kind**: struct  
**Role**: Structure

An action with an optional stopping point that you want to perform on a vehicle.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.3+ - Deprecated in 15.0
- watchOS 9.0+ - Deprecated in 11.0

> **Deprecated**: Use [`perform(_:continuationStrategy:)`](./carkeyremotecontrolsession/perform%28_,continuationstrategy%29.md) instead.

## Declaration

```swift
struct RemoteKeylessEntryEnduringAction
```

#### Overview

Use a [`RemoteKeylessEntryEnduringAction`](./remotekeylessentryenduringaction.md) object to store details about an action that you can stop or let run to completion. For example, you might use this type of action to lower or raise the top of a convertible vehicle. The object stores information about the vehicle feature to control and the action to take on that feature. It also stores the identifier for the vehicle itself.

After you create a [`RemoteKeylessEntryEnduringAction`](./remotekeylessentryenduringaction.md) object, call your session’s [`perform(_:)`](./carkeyremotecontrolsession/perform%28_%29-7mpsy.md) method to execute the action. Use the returned [`RemoteKeylessEntryAction.ExecutionRequest`](./remotekeylessentryaction/executionrequest.md) object to determine the success or failure of the request.

## Topics

### Creating the Action Request
- [init(functionID: FunctionIdentifier, actionID: ActionIdentifier, vehicleID: String)](./remotekeylessentryenduringaction/init%28functionid,actionid,vehicleid%29.md)
  Creates a new action object with the specified action-specific details and vehicle ID.
### Receiving the Action’s Response
- [RemoteKeylessEntryEnduringAction.EnduringExecutionRequest](./remotekeylessentryenduringaction/enduringexecutionrequest.md)
  An object that reports the results of an action with an optional stopping point.
### Getting the Action Details
- [let functionID: FunctionIdentifier](./remotekeylessentryenduringaction/functionid.md)
  The vehicle-specific code that identifies which feature you want to control.
- [let actionID: ActionIdentifier](./remotekeylessentryenduringaction/actionid.md)
  The vehicle-specific code that identifies what action to take on the targeted feature.
- [let recipientVehicleID: String](./remotekeylessentryenduringaction/recipientvehicleid.md)
  The vehicle to receive the action request.

## See Also

### Vehicle Actions
- [struct RemoteKeylessEntryAction](./remotekeylessentryaction.md)
  An automatically ending action that you want to perform on a vehicle.
- [struct FunctionIdentifier](./functionidentifier.md)
  A type that stores the designation code for one of your vehicle’s features.
- [struct ActionIdentifier](./actionidentifier.md)
  A type that stores the designation code for one of the actions that a vehicle feature supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/remotekeylessentryenduringaction)*