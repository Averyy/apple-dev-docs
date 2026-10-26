---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyoutcome/taskoccurrenceindex"
framework: "CareKit/CareKitStore"
---

# taskOccurrenceIndex

**Framework**: CareKit/CareKitStore  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A property that specifies how many events occured before this outcome became instantiated.

## Declaration

```swift
var taskOccurrenceIndex: Int { get }
```

#### Discussion

For example, if a task is schedule to happen twice per day, then the 2nd outcome on the 2nd day has a `taskOccurrenceIndex` of 3.

> **Note**: The task occurrence references a specific version of a task. If a new version the task becomes instantiated, the task occurrence index restarts from 0.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyoutcome/taskoccurrenceindex)*