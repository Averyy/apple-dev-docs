---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockscheduleelement/events(betweenoccurrenceindex:and:)"
framework: "CareKit/CareKitStore"
---

# events(betweenOccurrenceIndex:and:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Compute all events that occur between `startIndex` (inclusive) and `stopIndex` (exclusive). The result might not contain the desired events if the schedule ends before a particular event starts.

## Declaration

```swift
func events(betweenOccurrenceIndex startIndex: Int, and stopIndex: Int) -> [OCKScheduleEvent]
```

## Discussion

> **Precondition**: `startIndex` < `stopIndex`

## Parameters

- `startIndex`: The inclusive lower bound for the event indices.
- `stopIndex`: The exclusive upper bound for the event indices.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockscheduleelement/events(betweenoccurrenceindex:and:))*