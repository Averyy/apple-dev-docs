# init(functionID:actionID:vehicleID:)

**Framework**: CarKey  
**Kind**: init

Creates a new action object with the specified action-specific details and vehicle ID.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
init(functionID: FunctionIdentifier, actionID: ActionIdentifier, vehicleID: String)
```

#### Return Value

An enduring action object with the specified information.

#### Discussion

This method creates an immutable action object that you can pass to your session’s [`perform(_:)`](carkeyremotecontrolsession/perform(_:)-7mpsy.md) method.

## Parameters

- `functionID`: The vehicle-specific code that identifies the   feature to activate. For example, the vehicle might have a   specific code to identify the roof mechanism on a convertible vehicle.
- `actionID`: The vehicle-specific code that defines what action   to take on the vehicle feature. For example, a vehicle might have   separate actions to raise or lower the top on a convertible.
- `vehicleID`: The target vehicle for the action. Choose the vehicle   from one of the session’s vehicle reports. Specify the string   in the   property of the corresponding report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/remotekeylessentryconfigurableenduringaction/init(functionid:actionid:vehicleid:))*