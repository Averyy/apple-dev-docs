# charging

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the electric vehicle is currently charging.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- watchOS 5.0+

## Declaration

```swift
@nonobjc
final var charging: Bool? { get set }
```

## Discussion

Typically, you assign a value to this property only after handling the intent.

## See Also

### Providing the Charge Status
- [var activeConnector: INCar.ChargingConnectorType?](./activeconnector.md)
  The type of connector that’s currently delivering charge to the electric vehicle’s battery.
- [var minutesToFull: Int?](./minutestofull-2kbt6.md)
  The number of minutes it takes to fully charge the electric vehicle’s battery.
- [var dateOfLastStateUpdate: DateComponents?](./dateoflaststateupdate.md)
  A timestamp that indicates the most recent charge status for the electric vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponse/charging-6xnqj)*