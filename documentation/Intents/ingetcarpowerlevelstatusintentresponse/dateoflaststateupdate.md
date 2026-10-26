# dateOfLastStateUpdate

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A timestamp that indicates the most recent charge status for the electric vehicle.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var dateOfLastStateUpdate: DateComponents? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSDateComponents * dateOfLastStateUpdate;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSDateComponents * dateOfLastStateUpdate;
```

#### Discussion

When creating a response object, you must set this property to the date and time when the system captured the charge status for the electric vehicle.

## See Also

### Providing the Charge Status
- [var activeConnector: INCar.ChargingConnectorType?](./activeconnector.md)
  The type of connector that’s currently delivering charge to the electric vehicle’s battery.
- [var charging: Bool?](./charging-6xnqj.md)
  A Boolean value that indicates whether the electric vehicle is currently charging.
- [var minutesToFull: Int?](./minutestofull-2kbt6.md)
  The number of minutes it takes to fully charge the electric vehicle’s battery.
- [charging](./charging-7aamu.md)
  A Boolean value that indicates whether the electric vehicle is currently charging.
- [minutesToFull](./minutestofull-25vcb.md)
  The number of minutes it will take to fully charge the electric vehicle’s battery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponse/dateoflaststateupdate)*