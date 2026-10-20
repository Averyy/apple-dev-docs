# nextStartDate

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The date and time the next recurring leaderboard occurrence starts accepting scores.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var nextStartDate: Date? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSDate * nextStartDate;
```

## Mentions

- [Creating recurring leaderboards](../creating-recurring-leaderboards.md)

## See Also

### Accessing Recurring Leaderboard Properties
- [var startDate: Date?](./startdate.md)
  The date and time a recurring leaderboard occurrence starts accepting scores.
- [var duration: TimeInterval](./duration.md)
  The duration from the start date that a recurring leaderboard occurrence accepts scores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/nextstartdate)*