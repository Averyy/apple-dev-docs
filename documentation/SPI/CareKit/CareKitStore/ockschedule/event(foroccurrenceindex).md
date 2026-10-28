---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockschedule/event(foroccurrenceindex:)"
framework: "CareKit/CareKitStore"
---

# event(forOccurrenceIndex:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Compute the date of the Nth event. The result will be nil if the Nth event starts after the end of the schedule.

## Declaration

```swift
func event(forOccurrenceIndex occurrence: Int) -> OCKScheduleEvent?
```

## Discussion

> **Precondition**: `occurrence >= 0`

## Parameters

- `occurrence`: The occurrence of the desired event.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockschedule/event(foroccurrenceindex:))*