# delegate

**Framework**: UIKit  
**Kind**: property

A delegate object that a calendar view asks about selectable weeks and informs of changes to the week selection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UICalendarSelectionWeekOfYearDelegate)? { get }
```

## See Also

- [protocol UICalendarSelectionWeekOfYearDelegate](uicalendarselectionweekofyeardelegate.md)
  A set of methods you implement to provide selectable weeks and handle changes to the week selection in a calendar view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionweekofyear/delegate)*