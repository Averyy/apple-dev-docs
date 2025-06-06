# startDate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

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

#### Discussion

The default value is `nil` which requests the first payment as part of the initial transaction.

## See Also

- [var endDate: Date?](pkrecurringpaymentsummaryitem/enddate.md)
  The date of the final payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkrecurringpaymentsummaryitem/startdate)*