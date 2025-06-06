# calendarView(_:decorationFor:)

**Framework**: UIKit  
**Kind**: method

Creates a calendar view decoration for the date represented by the date components you provide.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func calendarView(_ calendarView: UICalendarView, decorationFor dateComponents: DateComponents) -> UICalendarView.Decoration?
```

#### Return Value

A calendar view decoration.

## Parameters

- `calendarView`: The calendar view object requesting the decoration.
- `dateComponents`: Date components that represent the date for the calendar view to display a decoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarviewdelegate/calendarview(_:decorationfor:))*