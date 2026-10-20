# startDate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The date of the first payment.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var startDate: Date? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSDate * startDate;
```

#### Discussion

The default value is `nil` which requests the first payment as part of the initial transaction.

## See Also

### Setting the payment period
- [var endDate: Date?](./enddate.md)
  The date of the final payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkrecurringpaymentsummaryitem/startdate)*