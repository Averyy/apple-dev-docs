# init(delegate:)

**Framework**: UIKit  
**Kind**: init

Creates an object that tracks a date a user selects from a calendar view, with an optional delegate to manage selectable dates and selection changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(delegate: (any UICalendarSelectionSingleDateDelegate)?)
```

## Parameters

- `delegate`: A delegate object that a calendar view asks about selectable dates, and informs of changes to the selection of a single date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionsingledate/init(delegate:))*