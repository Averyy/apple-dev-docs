# intervalUnit

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The amount of time – in calendar units such as day, month, or year – that represents a fraction of the total payment interval.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var intervalUnit: NSCalendar.Unit { get set }
```

#### Discussion

The default value for the interval unit is [`month`](https://developer.apple.com/documentation/Foundation/NSCalendar/Unit/month).

The supported [`NSCalendar.Unit`](https://developer.apple.com/documentation/Foundation/NSCalendar/Unit) interval units are:

- [`minute`](https://developer.apple.com/documentation/CoreFoundation/CFCalendarUnit/minute)
- [`hour`](https://developer.apple.com/documentation/CoreFoundation/CFCalendarUnit/hour)
- [`day`](https://developer.apple.com/documentation/CoreFoundation/CFCalendarUnit/day)
- [`month`](https://developer.apple.com/documentation/CoreFoundation/CFCalendarUnit/month)
- [`year`](https://developer.apple.com/documentation/CoreFoundation/CFCalendarUnit/year)

To set an interval unit based on a week, set [`intervalUnit`](pkrecurringpaymentsummaryitem/intervalunit.md) to [`day`](https://developer.apple.com/documentation/CoreFoundation/CFCalendarUnit/day), and set [`intervalCount`](pkrecurringpaymentsummaryitem/intervalcount.md) to a multiple of the number of days per week. To find the number of days for a week in the current calendar, call `NSCalendar.current.maximumRange(of: .weekday)!.count)`.

For example, the code below sets a payment that occurs every two weeks.

```swift
let daysPerWeek = NSCalendar.current.maximumRange(of: .weekday)!.count)

intervalUnit = .day
intervalCount = daysPerWeek * 2
```

## See Also

- [var intervalCount: Int](pkrecurringpaymentsummaryitem/intervalcount.md)
  The number of interval units that make up the total payment interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkrecurringpaymentsummaryitem/intervalunit)*