---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadableoutcomestore/outcomes"
framework: "CareKit/CareKitStore"
---

# Outcomes

**Framework**: CareKit/CareKitStore  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

An asynchronous sequence that produces outcomes.

## Declaration

```swift
associatedtype Outcomes : Sendable, AsyncSequence where Self.Outcomes.Element == [Self.Outcome]
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadableoutcomestore/outcomes)*