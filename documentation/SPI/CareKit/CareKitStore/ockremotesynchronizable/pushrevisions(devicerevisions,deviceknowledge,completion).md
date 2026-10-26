---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockremotesynchronizable/pushrevisions(devicerevisions:deviceknowledge:completion:)"
framework: "CareKit/CareKitStore"
---

# pushRevisions(deviceRevisions:deviceKnowledge:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Push a revision from a device up to the server.

## Declaration

```swift
func pushRevisions(deviceRevisions: [OCKRevisionRecord], deviceKnowledge: OCKRevisionRecord.KnowledgeVector, completion: @escaping @Sendable (Error?) -> Void)
```

## Parameters

- `deviceRevisions`: Revisions from the device to be pushed to the remote.
- `deviceKnowledge`: The knowledge vector at the time of pushing the revisions.
- `completion`: A closure that should be called once the push completes.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockremotesynchronizable/pushrevisions(devicerevisions:deviceknowledge:completion:))*