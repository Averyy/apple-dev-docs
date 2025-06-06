# setVisibleDateComponents(_:animated:)

**Framework**: UIKit  
**Kind**: method

Sets the date components that represent the date for the calendar view to make visible, with an option to animate the date change.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setVisibleDateComponents(_ dateComponents: DateComponents, animated: Bool)
```

#### Discussion

The date that `dateComponents` represents must be within the dates that [`availableDateRange`](uicalendarview/availabledaterange.md) represents.

If `dateComponents.calendar` is `nil` or isn’t equal to [`calendar`](uicalendarview/calendar.md), the calendar view uses [`calendar`](uicalendarview/calendar.md), which may result in an invalid date from the date components.

## Parameters

- `dateComponents`: Date components that represent the date for the calendar view to display.
- `animated`: A Boolean value that indicates whether the calendar view animates the date change.

## See Also

- [var visibleDateComponents: DateComponents](uicalendarview/visibledatecomponents.md)
  The date components that represent the visible date in the calendar view.
- [var availableDateRange: DateInterval](uicalendarview/availabledaterange.md)
  The range of dates that the calendar view displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview/setvisibledatecomponents(_:animated:))*