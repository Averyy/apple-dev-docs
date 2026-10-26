# earliestBookingDateForResults

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The earliest date to associate with any reservations.

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

#### Discussion

After retrieving the user’s reservations, remove any reservations occurring before the date specified by this property. If the value of this property is `nil`, do not remove reservations based on their date.

## See Also

### Getting the Result Limits
- [var maximumNumberOfResults: NSNumber?](./maximumnumberofresults.md)
  The maximum number of reservations to include in your response object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetusercurrentrestaurantreservationbookingsintent/earliestbookingdateforresults)*