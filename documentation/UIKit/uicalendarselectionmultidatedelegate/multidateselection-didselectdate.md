# multiDateSelection(_:didSelectDate:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Informs the delegate that a user selected a date represented by date components.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func multiDateSelection(_ selection: UICalendarSelectionMultiDate, didSelectDate dateComponents: DateComponents)
```

## Parameters

- `selection`: An object that tracks one or more dates that a user selects from a calendar view.
- `dateComponents`: Date components that represent a date the user selected.

## See Also

- [func multiDateSelection(UICalendarSelectionMultiDate, didDeselectDate: DateComponents)](uicalendarselectionmultidatedelegate/multidateselection(_:diddeselectdate:).md)
  Informs the delegate that a user deselected a date represented by date components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionmultidatedelegate/multidateselection(_:didselectdate:))*