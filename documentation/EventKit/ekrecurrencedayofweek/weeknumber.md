# weekNumber

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The week number of the day of the week.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var weekNumber: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger weekNumber;
```

#### Discussion

Values range from `–53` to `53`. A negative value indicates a value from the end of the range. `0` indicates the week number is irrelevant.

## See Also

### Accessing Properties of a Day of the Week
- [var dayOfTheWeek: EKWeekday](./dayoftheweek.md)
  The day of the week.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek/weeknumber)*