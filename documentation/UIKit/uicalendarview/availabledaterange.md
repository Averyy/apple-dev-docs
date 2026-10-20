# availableDateRange

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The range of dates that the calendar view displays.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var availableDateRange: DateInterval { get set }
```

```objc
@property (nonatomic, copy, nonnull) NSDateInterval * availableDateRange;
```

#### Discussion

Set `availableDateRange` to restrict the earliest or latest dates that the calendar view displays. The default date range starts with [`distantPast`](../../Foundation/date/distantpast.md) (Swift) or [`distantPast`](../../Foundation/nsdate/distantpast.md) (Objective-C), and ends with [`distantFuture`](../../Foundation/date/distantfuture.md) (Swift) or [`distantFuture`](../../Foundation/nsdate/distantfuture.md) (Objective-C).

## See Also

### Setting the visible date and range
- [var visibleDateComponents: DateComponents](./visibledatecomponents.md)
  The date components that represent the visible date in the calendar view.
- [func setVisibleDateComponents(DateComponents, animated: Bool)](./setvisibledatecomponents%28_,animated%29.md)
  Sets the date components that represent the date for the calendar view to make visible, with an option to animate the date change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview/availabledaterange)*