# visibleDateComponents

**Framework**: UIKit  
**Kind**: property

The date components that represent the visible date in the calendar view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var visibleDateComponents: DateComponents { get set }
```

#### Discussion

If `visibleDateComponents.calendar` is `nil` or isn’t equal to [`calendar`](uicalendarview/calendar.md), the calendar view uses [`calendar`](uicalendarview/calendar.md), which may result in an invalid date from the date components.

## See Also

- [func setVisibleDateComponents(DateComponents, animated: Bool)](uicalendarview/setvisibledatecomponents(_:animated:).md)
  Sets the date components that represent the date for the calendar view to make visible, with an option to animate the date change.
- [var availableDateRange: DateInterval](uicalendarview/availabledaterange.md)
  The range of dates that the calendar view displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview/visibledatecomponents)*