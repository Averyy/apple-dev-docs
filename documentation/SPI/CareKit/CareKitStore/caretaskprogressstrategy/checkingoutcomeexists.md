---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/caretaskprogressstrategy/checkingoutcomeexists"
framework: "CareKit/CareKitStore"
---

# checkingOutcomeExists

**Framework**: CareKit/CareKitStore  
**Kind**: property  
**Role**: Type Property

A strategy that computes progress for a task by checking for the existence of an outcome.

## Declaration

```swift
static var checkingOutcomeExists: CareTaskProgressStrategy<BinaryCareTaskProgress> { get }
```

## Discussion

The task is considered completed if an [`outcome`](../ockanyevent/outcome.md) exists.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/caretaskprogressstrategy/checkingoutcomeexists)*