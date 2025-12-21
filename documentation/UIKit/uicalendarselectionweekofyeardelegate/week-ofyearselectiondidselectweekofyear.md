# week(ofYearSelection:didSelectWeekOfYear:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Notifies the delegate after a person selects a week in the calendar view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
func week(ofYearSelection selection: UICalendarSelectionWeekOfYear, didSelectWeekOfYear weekOfYearComponents: DateComponents?)
```

## See Also

- [func week(ofYearSelection: UICalendarSelectionWeekOfYear, canSelectWeekOfYear: DateComponents?) -> Bool](uicalendarselectionweekofyeardelegate/week(ofyearselection:canselectweekofyear:).md)
  Determines if a week is available for selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionweekofyeardelegate/week(ofyearselection:didselectweekofyear:))*