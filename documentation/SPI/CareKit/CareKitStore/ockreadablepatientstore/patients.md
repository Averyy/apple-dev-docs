---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablepatientstore/patients"
framework: "CareKit/CareKitStore"
---

# Patients

**Framework**: CareKit/CareKitStore  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

An asynchronous sequence that produces patients.

## Declaration

```swift
associatedtype Patients : Sendable, AsyncSequence where Self.Patients.Element == [Self.Patient]
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablepatientstore/patients)*