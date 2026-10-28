---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockevent/computeprogress(by:)"
framework: "CareKit/CareKitStore"
---

# computeProgress(by:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Compute the progress for an event.

## Declaration

```swift
func computeProgress<Progress>(by strategy: CareTaskProgressStrategy<Progress> = .checkingOutcomeExists) -> Progress where Progress : CareTaskProgress
```

## Discussion

Progress is computed according to the `strategy`. See [`CareTaskProgressStrategy`](../caretaskprogressstrategy.md) for a list of the different strategies.

Compute progress across multiple events using [`AggregatedCareTaskProgress`](../aggregatedcaretaskprogress.md).

## Parameters

- `strategy`: The strategy that computes progress for the event.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockevent/computeprogress(by:))*