# activeConnector

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The type of connector that’s currently delivering charge to the electric vehicle’s battery.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var activeConnector: INCar.ChargingConnectorType? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INCarChargingConnectorType activeConnector;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INCarChargingConnectorType activeConnector;
```

#### Discussion

If [`charging`](./charging-6xnqj.md) is [`true`](../../Swift/true.md), set this property to the connector type that’s currently delivering charge to the vehicle. The [`supportedChargingConnectors`](../incar/supportedchargingconnectors.md) array of the corresponding [`INCar`](../incar.md) object must contain the value you use.

## See Also

### Providing the Charge Status
- [var charging: Bool?](./charging-6xnqj.md)
  A Boolean value that indicates whether the electric vehicle is currently charging.
- [var minutesToFull: Int?](./minutestofull-2kbt6.md)
  The number of minutes it takes to fully charge the electric vehicle’s battery.
- [var dateOfLastStateUpdate: DateComponents?](./dateoflaststateupdate.md)
  A timestamp that indicates the most recent charge status for the electric vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponse/activeconnector)*