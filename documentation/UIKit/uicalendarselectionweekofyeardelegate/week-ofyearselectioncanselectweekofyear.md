# week(ofYearSelection:canSelectWeekOfYear:)

**Framework**: UIKit  
**Kind**: method

Notifies the delegate after a person selects a week in the calendar view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
optional func week(ofYearSelection selection: UICalendarSelectionWeekOfYear, canSelectWeekOfYear weekOfYearComponents: DateComponents?) -> Bool
```

## See Also

- [func week(ofYearSelection: UICalendarSelectionWeekOfYear, didSelectWeekOfYear: DateComponents?)](uicalendarselectionweekofyeardelegate/week(ofyearselection:didselectweekofyear:).md)
  Determines if a week is available for selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionweekofyeardelegate/week(ofyearselection:canselectweekofyear:))*