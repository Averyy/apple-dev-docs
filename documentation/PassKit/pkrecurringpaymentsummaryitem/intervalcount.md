# intervalCount

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The number of interval units that make up the total payment interval.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var intervalCount: Int { get set }
```

#### Discussion

The default value is `1`, which requests a recurring payment every one [`intervalUnit`](pkrecurringpaymentsummaryitem/intervalunit.md).

## See Also

- [var intervalUnit: NSCalendar.Unit](pkrecurringpaymentsummaryitem/intervalunit.md)
  The amount of time – in calendar units such as day, month, or year – that represents a fraction of the total payment interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkrecurringpaymentsummaryitem/intervalcount)*