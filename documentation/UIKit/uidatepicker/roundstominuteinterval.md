# roundsToMinuteInterval

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the date rounds to a specific minute interval.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var roundsToMinuteInterval: Bool { get set }
```

```objc
@property (nonatomic) BOOL roundsToMinuteInterval;
```

#### Discussion

If this property is [`true`](../../Swift/true.md), [`date`](./date.md) always rounds to the [`minuteInterval`](./minuteinterval.md) and only produces dates that align with the minute interval. If this property is [`false`](../../Swift/false.md), changes to [`date`](./date.md) ignore the [`minuteInterval`](./minuteinterval.md) property.

The default value is [`true`](../../Swift/true.md).

## See Also

### Configuring temporal attributes
- [var maximumDate: Date?](./maximumdate.md)
  The maximum date that a date picker can show.
- [var minimumDate: Date?](./minimumdate.md)
  The minimum date that a date picker can show.
- [var minuteInterval: Int](./minuteinterval.md)
  The interval at which the date picker should display minutes.
- [var countDownDuration: TimeInterval](./countdownduration.md)
  The value displayed by the date picker when the mode property is set to show a countdown time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker/roundstominuteinterval)*