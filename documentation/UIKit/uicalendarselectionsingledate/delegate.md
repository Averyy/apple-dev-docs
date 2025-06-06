# delegate

**Framework**: UIKit  
**Kind**: property

A delegate object that a calendar view asks about selectable dates and informs of changes to the selection of a single date.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UICalendarSelectionSingleDateDelegate)? { get }
```

## See Also

- [protocol UICalendarSelectionSingleDateDelegate](uicalendarselectionsingledatedelegate.md)
  A set of methods you implement to provide selectable dates and handle changes to the selection of a single date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionsingledate/delegate)*