---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockrevisionrecord/knowledgevector-swift.struct/processes"
framework: "CareKit/CareKitStore"
---

# processes

**Framework**: CareKit/CareKitStore  
**Kind**: property  
**Role**: Instance Property

Each store involved in synchronization is termed a process and given a unique UUID. The corresponding integer for a process is an indication of time. If two processes have the same integer value, they both have the same knowledge of the current data representation.

## Declaration

```swift
var processes: [UUID : Int]
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockrevisionrecord/knowledgevector-swift.struct/processes)*