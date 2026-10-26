# charging

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the electric vehicle is currently charging.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSNumber * charging;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSNumber * charging;
```

#### Discussion

Typically, you assign a value to this property only after handling the intent.

## See Also

### Providing the Charge Status
- [var activeConnector: INCar.ChargingConnectorType?](./activeconnector.md)
  The type of connector that’s currently delivering charge to the electric vehicle’s battery.
- [minutesToFull](./minutestofull-25vcb.md)
  The number of minutes it will take to fully charge the electric vehicle’s battery.
- [var dateOfLastStateUpdate: DateComponents?](./dateoflaststateupdate.md)
  A timestamp that indicates the most recent charge status for the electric vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponse/charging-7aamu)*