# estimatedDropOffDate

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The estimated drop-off time for the ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var estimatedDropOffDate: Date? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSDate * estimatedDropOffDate;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSDate * estimatedDropOffDate;
```

#### Discussion

Use this property to provide an estimated time of arrival at the user’s destination.

The default value of this property is `nil`.

## See Also

### Accessing the Pickup and Drop Off Times
- [var scheduledPickupTime: INDateComponentsRange?](./scheduledpickuptime.md)
  The scheduled pickup time for the user.
- [var estimatedPickupDate: Date?](./estimatedpickupdate.md)
  The estimated pickup time for the ride.
- [var estimatedPickupEndDate: Date?](./estimatedpickupenddate.md)
  The date after which the driver may stop waiting for the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridestatus/estimateddropoffdate)*