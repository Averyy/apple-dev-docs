# recipientVehicleID

**Framework**: CarKey  
**Kind**: property

The vehicle to receive the action request.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
let recipientVehicleID: String
```

#### Discussion

This string is the same one that appears in the [`identifier`](vehiclereport/identifier.md) property of one of the session’s vehicle reports.

## See Also

- [let functionID: FunctionIdentifier](remotekeylessentryenduringaction/functionid.md)
  The vehicle-specific code that identifies which feature you want to control.
- [let actionID: ActionIdentifier](remotekeylessentryenduringaction/actionid.md)
  The vehicle-specific code that identifies what action to take on the targeted feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/remotekeylessentryenduringaction/recipientvehicleid)*