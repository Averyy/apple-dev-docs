---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockscheduleelement/date(ofoccurrence:)"
framework: "CareKit/CareKitStore"
---

# date(ofOccurrence:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Computes the date of the Nth event. The result will be nil if the Nth event starts after the end of the schedule.

## Declaration

```swift
func date(ofOccurrence occurrence: Int) -> Date?
```

## Discussion

> **Precondition**: `occurrence >= 0`

## Parameters

- `occurrence`: The occurrence of the desired event.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockscheduleelement/date(ofoccurrence:))*