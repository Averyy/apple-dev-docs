# intervalUnit

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign) NSCalendarUnit intervalUnit;
```

#### Discussion

The default value for the interval unit is [`month`](../../Foundation/nscalendar/unit/month.md).

The supported [`NSCalendar.Unit`](../../Foundation/nscalendar/unit.md) interval units are:

- [`minute`](../../CoreFoundation/cfcalendarunit/minute.md)
- [`hour`](../../CoreFoundation/cfcalendarunit/hour.md)
- [`day`](../../CoreFoundation/cfcalendarunit/day.md)
- [`month`](../../CoreFoundation/cfcalendarunit/month.md)
- [`year`](../../CoreFoundation/cfcalendarunit/year.md)

To set an interval unit based on a week, set [`intervalUnit`](./intervalunit.md) to [`day`](../../CoreFoundation/cfcalendarunit/day.md), and set [`intervalCount`](./intervalcount.md) to a multiple of the number of days per week. To find the number of days for a week in the current calendar, call `NSCalendar.current.maximumRange(of: .weekday)!.count)`.

For example, the code below sets a payment that occurs every two weeks.

```swift
let daysPerWeek = NSCalendar.current.maximumRange(of: .weekday)!.count)

intervalUnit = .day
intervalCount = daysPerWeek * 2
```

## See Also

### Setting the payment interval
- [var intervalCount: Int](./intervalcount.md)
  The number of interval units that make up the total payment interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkrecurringpaymentsummaryitem/intervalunit)*