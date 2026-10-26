---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockremotesynchronizable"
framework: "CareKit/CareKitStore"
---

# OCKRemoteSynchronizable

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

Implement this protocol to allow CareKitStore to synchronize against an endpoint of your choosing.

## Declaration

```swift
protocol OCKRemoteSynchronizable : AnyObject, Sendable
```

## Topics

### Instance Properties
- [var automaticallySynchronizes: Bool](./ockremotesynchronizable/automaticallysynchronizes.md)
  If set to `true`, then the store will attempt to synchronize every time it is modified locally.
- [var delegate: OCKRemoteSynchronizationDelegate?](./ockremotesynchronizable/delegate.md)
  If set, the delegate will be alerted to important events delivered by the remote store.
### Instance Methods
- [func chooseConflictResolution(conflicts: [OCKEntity], completion: OCKResultClosure<OCKEntity>)](./ockremotesynchronizable/chooseconflictresolution%28conflicts,completion%29.md)
  This method will be called when CareKit detects a conflict between changes made to an entity in the device’s local store and the changes made to the same entity in other device’s stores. Inspect the conflicted and determine which version of the entity to keep, then call the completion closure with the chosen version.
- [func pullRevisions(since: OCKRevisionRecord.KnowledgeVector, mergeRevision: @Sendable (OCKRevisionRecord) -> Void, completion: @Sendable (Error?) -> Void)](./ockremotesynchronizable/pullrevisions%28since,mergerevision,completion%29.md)
  Fetch a revision record from the server that documents the changes that have been made on the server since the last time synchronization was performed.
- [func pushRevisions(deviceRevisions: [OCKRevisionRecord], deviceKnowledge: OCKRevisionRecord.KnowledgeVector, completion: @Sendable (Error?) -> Void)](./ockremotesynchronizable/pushrevisions%28devicerevisions,deviceknowledge,completion%29.md)
  Push a revision from a device up to the server.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [OCKWatchConnectivityPeer](./ockwatchconnectivitypeer.md)

## See Also

### Synchronization
- [protocol OCKRemoteSynchronizationDelegate](./ockremotesynchronizationdelegate.md)
  Implement this protocol to listen for important events coming from an `OCKRemoteSynchronizable`.
- [struct OCKRevisionRecord](./ockrevisionrecord.md)
  Revision records are exchanged by the CareKit and a remote database during synchronization. Each revision record contains an array of entities as well as a knowledge vector.
- [enum OCKEntity](./ockentity.md)
  Holds one of several possible modified entities.
- [class OCKWatchConnectivityPeer](./ockwatchconnectivitypeer.md)
  `OCKWatchConnectivityPeer` enables synchronizing two instances of `OCKStore` where one store is part of an iPhone app and the other belongs to the watchOS companion app.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockremotesynchronizable)*