# availableDateRange

**Framework**: UIKit  
**Kind**: property

The range of dates that the calendar view displays.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var availableDateRange: DateInterval { get set }
```

#### Discussion

Set `availableDateRange` to restrict the earliest or latest dates that the calendar view displays. The default date range starts with [`distantPast`](https://developer.apple.com/documentation/Foundation/Date/distantPast) (Swift) or [`distantPast`](https://developer.apple.com/documentation/Foundation/NSDate/distantPast) (Objective-C), and ends with [`distantFuture`](https://developer.apple.com/documentation/Foundation/Date/distantFuture) (Swift) or [`distantFuture`](https://developer.apple.com/documentation/Foundation/NSDate/distantFuture) (Objective-C).

## See Also

- [var visibleDateComponents: DateComponents](uicalendarview/visibledatecomponents.md)
  The date components that represent the visible date in the calendar view.
- [func setVisibleDateComponents(DateComponents, animated: Bool)](uicalendarview/setvisibledatecomponents(_:animated:).md)
  Sets the date components that represent the date for the calendar view to make visible, with an option to animate the date change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview/availabledaterange)*