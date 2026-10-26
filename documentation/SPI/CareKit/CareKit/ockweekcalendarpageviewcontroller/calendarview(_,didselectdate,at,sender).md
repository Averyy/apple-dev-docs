---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockweekcalendarpageviewcontroller/calendarview(_:didselectdate:at:sender:)"
framework: "CareKit/CareKit"
---

# calendarView(_:didSelectDate:at:sender:)

**Framework**: CareKit/CareKit  
**Kind**: method  
**Role**: Instance Method

Called when a particular date in the calendar was selected.

## Declaration

```swift
@MainActor
func calendarView(_ calendarView: UIView & OCKCalendarDisplayable, didSelectDate date: Date, at index: Int, sender: Any?)
```

## Parameters

- `calendarView`: The view displaying the calendar.
- `date`: The date that was selected.
- `index`: The index of the date that was selected with respect to the collection of days in the current `dateInterval`.
- `sender`: The sender that initiated the selection.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockweekcalendarpageviewcontroller/calendarview(_:didselectdate:at:sender:))*