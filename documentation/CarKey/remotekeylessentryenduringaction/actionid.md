# actionID

**Framework**: CarKey  
**Kind**: property  
**Role**: Instance Property

The vehicle-specific code that identifies what action to take on the targeted feature.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.3+ - Deprecated in 15.0
- watchOS 9.0+ - Deprecated in 11.0

> **Deprecated**: Use [`perform(_:continuationStrategy:)`](../carkeyremotecontrolsession/perform%28_,continuationstrategy%29.md) instead.

## Declaration

```swift
let actionID: ActionIdentifier
```

## Discussion

You define the action identifiers for your vehicles and what actions they perform on the vehicle function.

## See Also

### Getting the Action Details
- [let functionID: FunctionIdentifier](./functionid.md)
  The vehicle-specific code that identifies which feature you want to control.
- [let recipientVehicleID: String](./recipientvehicleid.md)
  The vehicle to receive the action request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/remotekeylessentryenduringaction/actionid)*