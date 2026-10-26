# scheduledPickupTime

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The scheduled pickup time for the user.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var scheduledPickupTime: INDateComponentsRange? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INDateComponentsRange * scheduledPickupTime;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INDateComponentsRange * scheduledPickupTime;
```

#### Discussion

Use this property to specify the scheduled pickup time for the user. Use this property instead of the [`estimatedPickupDate`](./estimatedpickupdate.md) and [`estimatedPickupEndDate`](./estimatedpickupenddate.md) properties when you can guarantee the pickup time.

## See Also

### Accessing the Pickup and Drop Off Times
- [var estimatedPickupDate: Date?](./estimatedpickupdate.md)
  The estimated pickup time for the ride.
- [var estimatedPickupEndDate: Date?](./estimatedpickupenddate.md)
  The date after which the driver may stop waiting for the user.
- [var estimatedDropOffDate: Date?](./estimateddropoffdate.md)
  The estimated drop-off time for the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridestatus/scheduledpickuptime)*