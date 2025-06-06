# delegate

**Framework**: UIKit  
**Kind**: property

A delegate object that a calendar view asks for selectable dates and informs of changes to the selection of multiple dates.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UICalendarSelectionMultiDateDelegate)? { get }
```

## See Also

- [protocol UICalendarSelectionMultiDateDelegate](uicalendarselectionmultidatedelegate.md)
  A set of methods you implement to provide selectable dates and handle changes to the selection of multiple dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionmultidate/delegate)*