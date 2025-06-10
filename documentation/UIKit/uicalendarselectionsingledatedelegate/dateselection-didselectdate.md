# dateSelection(_:didSelectDate:)

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
func dateSelection(_ selection: UICalendarSelectionSingleDate, didSelectDate dateComponents: DateComponents?)
```

## Parameters

- `selection`: An object that tracks a date that a user selects from a calendar view.
- `dateComponents`: Date components that represent a date the user selected, or   if the user deselected a date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionsingledatedelegate/dateselection(_:didselectdate:))*