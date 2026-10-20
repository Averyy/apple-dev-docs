# week(ofYearSelection:canSelectWeekOfYear:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Determines if a week is available for selection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
optional func week(ofYearSelection selection: UICalendarSelectionWeekOfYear, canSelectWeekOfYear weekOfYearComponents: DateComponents?) -> Bool
```

```objc
- (BOOL) weekOfYearSelection:(UICalendarSelectionWeekOfYear *) selection canSelectWeekOfYear:(NSDateComponents *) weekOfYearComponents;
```

## See Also

### Handling week-of-year selections
- [func week(ofYearSelection: UICalendarSelectionWeekOfYear, didSelectWeekOfYear: DateComponents?)](./week%28ofyearselection,didselectweekofyear%29.md)
  Notifies the delegate after a person selects a week in the calendar view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionweekofyeardelegate/week(ofyearselection:canselectweekofyear:))*