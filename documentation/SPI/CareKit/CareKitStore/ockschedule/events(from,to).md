---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockschedule/events(from:to:)"
framework: "CareKit/CareKitStore"
---

# events(from:to:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Compute a list of events that occur between two dates. The lower bound is inclusive and the upper bound is exclusive.

## Declaration

```swift
func events(from start: Date, to end: Date) -> [OCKScheduleEvent]
```

## Discussion

> **Precondition**: `start` < `end`

## Parameters

- `start`: The earliest date (inclusive) when an event can occur.
- `end`: The latest date (exclusive) when an event can occur.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockschedule/events(from:to:))*