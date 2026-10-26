---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockremotesynchronizable/pullrevisions(since:mergerevision:completion:)"
framework: "CareKit/CareKitStore"
---

# pullRevisions(since:mergeRevision:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Fetch a revision record from the server that documents the changes that have been made on the server since the last time synchronization was performed.

## Declaration

```swift
func pullRevisions(since knowledgeVector: OCKRevisionRecord.KnowledgeVector, mergeRevision: @escaping @Sendable (OCKRevisionRecord) -> Void, completion: @escaping @Sendable (Error?) -> Void)
```

## Parameters

- `knowledgeVector`: Revisions newer than those encoded by this vector will be pulled.
- `mergeRevision`: A closure that can be called multiple times to merge revisions.
- `completion`: A closure that should be called with the results of the pull.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockremotesynchronizable/pullrevisions(since:mergerevision:completion:))*