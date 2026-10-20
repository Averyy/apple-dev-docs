# functionID

**Framework**: CarKey  
**Kind**: property  
**Role**: Instance Property

The vehicle-specific code that identifies which feature you want to control.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.3+ - Deprecated in 15.0
- watchOS 9.0+ - Deprecated in 11.0

> **Deprecated**: Use [`perform(_:continuationStrategy:)`](../carkeyremotecontrolsession/perform%28_,continuationstrategy%29.md) instead.

## Declaration

```swift
let functionID: FunctionIdentifier
```

#### Discussion

You define the function identifiers for your vehicles and what features they represent.

## See Also

### Getting the Action Details
- [let actionID: ActionIdentifier](./actionid.md)
  The vehicle-specific code that identifies what action to take on the targeted feature.
- [let recipientVehicleID: String](./recipientvehicleid.md)
  The vehicle to receive the action request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/remotekeylessentryenduringaction/functionid)*