# dateSelection(_:canSelectDate:)

**Framework**: UIKit  
**Kind**: method

Returns whether a user can select a date represented by date components in the calendar view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func dateSelection(_ selection: UICalendarSelectionSingleDate, canSelectDate dateComponents: DateComponents?) -> Bool
```

#### Return Value

A Boolean value that indicates whether the calendar view can select the date you provide.

#### Discussion

The calendar view displays nonselectable dates as disabled.

## Parameters

- `selection`: An object that tracks a date that a user selects from a calendar view.
- `dateComponents`: Date components that represent a date to select.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionsingledatedelegate/dateselection(_:canselectdate:))*