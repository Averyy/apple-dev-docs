---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/caretaskprogressstrategy/summingoutcomevalues"
framework: "CareKit/CareKitStore"
---

# summingOutcomeValues

**Framework**: CareKit/CareKitStore  
**Kind**: property  
**Role**: Type Property

A strategy that computes progress for a task.

## Declaration

```swift
static var summingOutcomeValues: CareTaskProgressStrategy<LinearCareTaskProgress> { get }
```

## Discussion

The strategy sums the [`targetValues`](../ockscheduleelement/targetvalues.md) for the event and compares the two results. The task is considered completed if the summed value reaches the summed target.

> **Note**:  If any of the outcome [`values`](../ockanyoutcome/values.md) or [`targetValues`](../ockscheduleelement/targetvalues.md) aren’t numeric and can’t be summed properly, they’re assigned a value of one during the summation process.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/caretaskprogressstrategy/summingoutcomevalues)*