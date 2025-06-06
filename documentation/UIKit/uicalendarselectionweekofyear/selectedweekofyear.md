# selectedWeekOfYear

**Framework**: UIKit  
**Kind**: property

The current week-of-year selection in the calendar view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
var selectedWeekOfYear: DateComponents? { get set }
```

#### Discussion

The components need to include `[.yearForWeekOfYear, .weekOfYear]`.

## See Also

- [func setSelected(DateComponents?, animated: Bool)](uicalendarselectionweekofyear/setselected(_:animated:).md)
  Updates the date component object that represents a selected week in a calendar view, with an option to animate the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionweekofyear/selectedweekofyear)*