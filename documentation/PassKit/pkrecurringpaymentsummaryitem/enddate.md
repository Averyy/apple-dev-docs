# endDate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The date of the final payment.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var endDate: Date? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSDate * endDate;
```

## Discussion

The default value is `nil` which specifies no end date.

## See Also

### Setting the payment period
- [var startDate: Date?](./startdate.md)
  The date of the first payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkrecurringpaymentsummaryitem/enddate)*