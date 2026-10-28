---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockscheduleelement/init(start:end:interval:text:targetvalues:duration:calendar:)"
framework: "CareKit/CareKitStore"
---

# init(start:end:interval:text:targetValues:duration:calendar:)

**Framework**: CareKit/CareKitStore  
**Kind**: init  
**Role**: Initializer

Create a `ScheduleElement` by specifying the start date, end date, and interval.

## Declaration

```swift
init(start: Date, end: Date?, interval: DateComponents, text: String? = nil, targetValues: [OCKOutcomeValue] = [], duration: Duration = .hours(1), calendar: Calendar = .autoupdatingCurrent)
```

## Discussion

> **Precondition**: `start` < `end`

> **Precondition**: `interval` should move forwards in time

## Parameters

- `start`: Date specifying the exact day and time that the first occurrence of this task happens.
- `end`: Date specifying when the task ends. The end date is not inclusive.
- `interval`: DateComponents specifying the frequency at which the schedule repeats.
- `text`: A textual representation of this schedule element. Examples: “After breakfast”, “08:00”, “As needed throughout the day”.
- `targetValues`: An array of values that represents goals for this schedule element.
- `duration`: A duration in seconds specifying how long the window to complete this event is.
- `calendar`: The calendar used when computing dates for the schedule.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockscheduleelement/init(start:end:interval:text:targetvalues:duration:calendar:))*