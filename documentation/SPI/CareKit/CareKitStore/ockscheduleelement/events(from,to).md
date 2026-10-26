---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockscheduleelement/events(from:to:)"
framework: "CareKit/CareKitStore"
---

# events(from:to:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Compute all events that occur between `start` (inclusive) and `end` (exclusive).

## Declaration

```swift
func events(from start: Date, to end: Date) -> [OCKScheduleEvent]
```

#### Discussion

> **Precondition**: `start` < `end`

## Parameters

- `start`: The inclusive earliest start time for an event.
- `end`: The exclusive latest start time for an event.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockscheduleelement/events(from:to:))*