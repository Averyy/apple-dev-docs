---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockcalendarviewdelegate/calendarview(_:didselectdate:at:sender:)"
framework: "CareKit/CareKitUI"
---

# calendarView(_:didSelectDate:at:sender:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate when a person selects a particular date in the calendar.

## Declaration

```swift
func calendarView(_ calendarView: UIView & OCKCalendarDisplayable, didSelectDate date: Date, at index: Int, sender: Any?)
```

## Parameters

- `calendarView`: The view displaying the calendar.
- `date`: The date that was selected.
- `index`: The index of the date that was selected with respect to the collection of days in the current `dateInterval`.
- `sender`: The sender that initiated the selection.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockcalendarviewdelegate/calendarview(_:didselectdate:at:sender:))*