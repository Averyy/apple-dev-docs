---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockrevisionrecord/knowledgevector-swift.struct/increment(clockfor:)"
framework: "CareKit/CareKitStore"
---

# increment(clockFor:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Increment the vector entry for the current process.

## Declaration

```swift
mutating func increment(clockFor uuid: UUID)
```

#### Discussion

This method should be called each time the vector’s owner completes merging a revision.

```
store.mergeRevision(revision)
store.vector.merge(revision.knowledgeVector)
store.vector.increment()
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockrevisionrecord/knowledgevector-swift.struct/increment(clockfor:))*