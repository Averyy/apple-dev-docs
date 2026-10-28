---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/linearcaretaskprogress/goal"
framework: "CareKit/CareKitStore"
---

# goal

**Framework**: CareKit/CareKitStore  
**Kind**: property  
**Role**: Instance Property

A value that indicates whether the task is complete.

## Declaration

```swift
var goal: Double? { get set }
```

## Discussion

When there is no goal, the value is `nil`.  The task is considered completed if the progress value is greater than zero.

> **Precondition**: `value` >= 0


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/linearcaretaskprogress/goal)*