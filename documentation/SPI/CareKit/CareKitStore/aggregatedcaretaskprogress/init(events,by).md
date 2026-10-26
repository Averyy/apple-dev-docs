---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/aggregatedcaretaskprogress/init(events:by:)"
framework: "CareKit/CareKitStore"
---

# init(events:by:)

**Framework**: CareKit/CareKitStore  
**Kind**: init  
**Role**: Initializer

Create user progress by computing and combining the progress for multiple tasks using a single strategy.

## Declaration

```swift
init<Progress>(events: [OCKAnyEvent], by strategy: CareTaskProgressStrategy<Progress> = .checkingOutcomeExists) where Progress : CareTaskProgress
```

## Parameters

- `events`: The events used to compute progress.
- `strategy`: The strategy used to compute progress for each event.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/aggregatedcaretaskprogress/init(events:by:))*