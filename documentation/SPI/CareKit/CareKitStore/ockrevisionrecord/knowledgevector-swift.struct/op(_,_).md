---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockrevisionrecord/knowledgevector-swift.struct/_(_:_:)"
framework: "CareKit/CareKitStore"
---

# <(_:_:)

**Framework**: CareKit/CareKitStore  
**Kind**: op  
**Role**: Operator

A knowledge vector A is strictly less than another knowledge vector B if the clocks of all processes in A are less than or equal to those in B and at least one is strictly less than.

## Declaration

```swift
static func < (lhs: OCKRevisionRecord.KnowledgeVector, rhs: OCKRevisionRecord.KnowledgeVector) -> Bool
```

#### Discussion

If A is strictly less than B, that means B had knowledge of A, therefore changes made by B should not be considered conflicts. If A is not strictly less than B, the changes in A and B are considered concurrent, and conflicts must be resolved.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockrevisionrecord/knowledgevector-swift.struct/_(_:_:))*