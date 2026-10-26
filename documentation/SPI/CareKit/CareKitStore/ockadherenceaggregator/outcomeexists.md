---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockadherenceaggregator/outcomeexists"
framework: "CareKit/CareKitStore"
---

# OCKAdherenceAggregator.outcomeExists

**Framework**: CareKit/CareKitStore  
**Kind**: case  
**Role**: Case

Computes a percentage by checking if the outcome for each event exists. Any event with a non-nil outcome will be counted as 100% complete, and any event without an outcome will be counted as 0% complete. The average completion across all events will be returned.

## Declaration

```swift
case outcomeExists
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockadherenceaggregator/outcomeexists)*