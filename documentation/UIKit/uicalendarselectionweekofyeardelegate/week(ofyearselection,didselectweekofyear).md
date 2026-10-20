# week(ofYearSelection:didSelectWeekOfYear:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies the delegate after a person selects a week in the calendar view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
func week(ofYearSelection selection: UICalendarSelectionWeekOfYear, didSelectWeekOfYear weekOfYearComponents: DateComponents?)
```

```objc
- (void) weekOfYearSelection:(UICalendarSelectionWeekOfYear *) selection didSelectWeekOfYear:(NSDateComponents *) weekOfYearComponents;
```

## See Also

### Handling week-of-year selections
- [func week(ofYearSelection: UICalendarSelectionWeekOfYear, canSelectWeekOfYear: DateComponents?) -> Bool](./week%28ofyearselection,canselectweekofyear%29.md)
  Determines if a week is available for selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionweekofyeardelegate/week(ofyearselection:didselectweekofyear:))*