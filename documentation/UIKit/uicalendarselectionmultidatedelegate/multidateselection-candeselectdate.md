# multiDateSelection(_:canDeselectDate:)

**Framework**: UIKit  
**Kind**: method

Returns whether a user can deselect a date represented by date components in the calendar view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func multiDateSelection(_ selection: UICalendarSelectionMultiDate, canDeselectDate dateComponents: DateComponents) -> Bool
```

#### Return Value

A Boolean value that indicates whether the calendar view can deselect the date you provide.

## Parameters

- `selection`: An object that tracks one or more dates that a user selects from a calendar view.
- `dateComponents`: Date components that represent a date to deselect.

## See Also

- [func multiDateSelection(UICalendarSelectionMultiDate, canSelectDate: DateComponents) -> Bool](uicalendarselectionmultidatedelegate/multidateselection(_:canselectdate:).md)
  Returns whether a user can select a date represented by date components in the calendar view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionmultidatedelegate/multidateselection(_:candeselectdate:))*