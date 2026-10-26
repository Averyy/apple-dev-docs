# estimatedPickupEndDate

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The date after which the driver may stop waiting for the user.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var estimatedPickupEndDate: Date? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSDate * estimatedPickupEndDate;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSDate * estimatedPickupEndDate;
```

#### Discussion

If the user is not at the pickup location when the driver arrives, the driver usually waits for a short period of time to give the user time to arrive. This property species the time at which the driver may opt to cancel the ride altogether if the user does not show up.

## See Also

### Accessing the Pickup and Drop Off Times
- [var scheduledPickupTime: INDateComponentsRange?](./scheduledpickuptime.md)
  The scheduled pickup time for the user.
- [var estimatedPickupDate: Date?](./estimatedpickupdate.md)
  The estimated pickup time for the ride.
- [var estimatedDropOffDate: Date?](./estimateddropoffdate.md)
  The estimated drop-off time for the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridestatus/estimatedpickupenddate)*