---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockrevisionrecord/knowledgevector-swift.struct/merge(with:)"
framework: "CareKit/CareKitStore"
---

# merge(with:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Merge this vector with another.

## Declaration

```swift
mutating func merge(with other: KnowledgeVector)
```

#### Discussion

This method should be called to incorporate knowledge received from another node in the network.

```
store.mergeRevision(revision)
store.vector.merge(revision.knowledgeVector)
store.vector.increment()
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockrevisionrecord/knowledgevector-swift.struct/merge(with:))*