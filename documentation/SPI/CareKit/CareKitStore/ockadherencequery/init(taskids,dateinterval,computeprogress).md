---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockadherencequery/init(taskids:dateinterval:computeprogress:)"
framework: "CareKit/CareKitStore"
---

# init(taskIDs:dateInterval:computeProgress:)

**Framework**: CareKit/CareKitStore  
**Kind**: init  
**Role**: Initializer

Initialize a new query by specifying the taskIDs, dates, and aggregator.

## Declaration

```swift
init(taskIDs: [String], dateInterval: DateInterval, computeProgress: @Sendable @escaping (OCKAnyEvent) -> CareTaskProgress = { event in
            event.computeProgress(by: .checkingOutcomeExists)
        })
```

## Parameters

- `taskIDs`: The identifiers of the tasks for which adherence should be computed.
- `dateInterval`: The date interval for which to return adherence information.
- `computeProgress`: Used to compute progress for an event.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockadherencequery/init(taskids:dateinterval:computeprogress:))*