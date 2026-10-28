# maximumNumberOfResults

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The maximum number of reservation results to return.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var maximumNumberOfResults: NSNumber? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSNumber * maximumNumberOfResults;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSNumber * maximumNumberOfResults;
```

## Discussion

When building the list of reservation time slots, limit the number of [`INRestaurantReservationBooking`](../inrestaurantreservationbooking.md) objects you create to the number in this property.

## See Also

### Getting the Time Slot Constraints
- [var earliestBookingDateForResults: Date?](./earliestbookingdateforresults.md)
  The earliest date for which to return results.
- [var latestBookingDateForResults: Date?](./latestbookingdateforresults.md)
  The latest date for which to return results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintent/maximumnumberofresults)*