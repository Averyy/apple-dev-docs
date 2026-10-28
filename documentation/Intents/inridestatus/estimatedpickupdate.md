# estimatedPickupDate

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The estimated pickup time for the ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var estimatedPickupDate: Date? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSDate * estimatedPickupDate;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSDate * estimatedPickupDate;
```

## Discussion

Specify the estimated date and time that your driver will pick up the user’s party. Siri and Maps display this information to the user.

The default value of this property is `nil`.

## See Also

### Accessing the Pickup and Drop Off Times
- [var scheduledPickupTime: INDateComponentsRange?](./scheduledpickuptime.md)
  The scheduled pickup time for the user.
- [var estimatedPickupEndDate: Date?](./estimatedpickupenddate.md)
  The date after which the driver may stop waiting for the user.
- [var estimatedDropOffDate: Date?](./estimateddropoffdate.md)
  The estimated drop-off time for the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridestatus/estimatedpickupdate)*