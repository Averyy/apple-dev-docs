# earliestBookingDateForResults

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The earliest date for which to return results.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var earliestBookingDateForResults: Date? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSDate * earliestBookingDateForResults;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSDate * earliestBookingDateForResults;
```

## Discussion

When building the list of reservation time slots, do not include time slots that occur before the date specified by this property.

## See Also

### Getting the Time Slot Constraints
- [var latestBookingDateForResults: Date?](./latestbookingdateforresults.md)
  The latest date for which to return results.
- [var maximumNumberOfResults: NSNumber?](./maximumnumberofresults.md)
  The maximum number of reservation results to return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintent/earliestbookingdateforresults)*