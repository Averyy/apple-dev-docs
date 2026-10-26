---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablecareplanstore/plans"
framework: "CareKit/CareKitStore"
---

# Plans

**Framework**: CareKit/CareKitStore  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

An asynchronous sequence that produces care plans.

## Declaration

```swift
associatedtype Plans : Sendable, AsyncSequence where Self.Plans.Element == [Self.Plan]
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablecareplanstore/plans)*