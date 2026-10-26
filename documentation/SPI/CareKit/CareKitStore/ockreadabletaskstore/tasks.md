---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadabletaskstore/tasks"
framework: "CareKit/CareKitStore"
---

# Tasks

**Framework**: CareKit/CareKitStore  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

An asynchronous sequence that produces tasks.

## Declaration

```swift
associatedtype Tasks : Sendable, AsyncSequence where Self.Tasks.Element == [Self.Task]
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadabletaskstore/tasks)*