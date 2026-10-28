# maximumNumberOfResults

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The maximum number of reservations to include in your response object.

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

Use the value in this property to limit the total number of reservations you include in your response to this intent. If this property is `nil`, include all of the reservations you found.

## See Also

### Getting the Result Limits
- [var earliestBookingDateForResults: Date?](./earliestbookingdateforresults.md)
  The earliest date to associate with any reservations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetusercurrentrestaurantreservationbookingsintent/maximumnumberofresults)*