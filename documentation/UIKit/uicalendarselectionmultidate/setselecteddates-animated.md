# setSelectedDates(_:animated:)

**Framework**: UIKit  
**Kind**: method

Updates the array of date component objects that represent selected dates in a calendar view, with an option to animate the change.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setSelectedDates(_ selectedDates: [DateComponents], animated: Bool)
```

## Parameters

- `selectedDates`: An array of date component objects that represent dates to select in a calendar view.
- `animated`: A Boolean value that indicates whether the calendar view should animate changing the selected dates.

## See Also

- [var selectedDates: [DateComponents]](uicalendarselectionmultidate/selecteddates.md)
  An array of date component objects that represent selected dates in a calendar view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionmultidate/setselecteddates(_:animated:))*