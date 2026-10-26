---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockrevisionrecord"
framework: "CareKit/CareKitStore"
---

# OCKRevisionRecord

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

Revision records are exchanged by the CareKit and a remote database during synchronization. Each revision record contains an array of entities as well as a knowledge vector.

## Declaration

```swift
struct OCKRevisionRecord
```

## Topics

### Structures
- [OCKRevisionRecord.KnowledgeVector](./ockrevisionrecord/knowledgevector-swift.struct.md)
  Knowledge vectors, also know as Lamport Timestamps, are used to determine the order of events in distributed systems that do not have a synchronized clock. If one knowledge vector is less than another, it means that the first event happened before the second. If one cannot be shown to be less than the other, it means the events are concurrent and require resolution.
### Initializers
- [init(entities: [OCKEntity], knowledgeVector: KnowledgeVector)](./ockrevisionrecord/init%28entities,knowledgevector%29.md)
  Create a new instance of `OCKRevisionRecord`.
- [init(from: any Decoder) throws](./ockrevisionrecord/init%28from%29.md)
### Instance Properties
- [let entities: [OCKEntity]](./ockrevisionrecord/entities.md)
  The entities that were modified, in the order the were inserted into the database. The first entity is the oldest and the last entity is the newest.
- [let knowledgeVector: KnowledgeVector](./ockrevisionrecord/knowledgevector-swift.property.md)
  A knowledge vector indicating the last known state of each other device by the device that authored this revision record.
### Default Implementations
- [Equatable Implementations](./ockrevisionrecord/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Synchronization
- [protocol OCKRemoteSynchronizable](./ockremotesynchronizable.md)
  Implement this protocol to allow CareKitStore to synchronize against an endpoint of your choosing.
- [protocol OCKRemoteSynchronizationDelegate](./ockremotesynchronizationdelegate.md)
  Implement this protocol to listen for important events coming from an `OCKRemoteSynchronizable`.
- [enum OCKEntity](./ockentity.md)
  Holds one of several possible modified entities.
- [class OCKWatchConnectivityPeer](./ockwatchconnectivitypeer.md)
  `OCKWatchConnectivityPeer` enables synchronizing two instances of `OCKStore` where one store is part of an iPhone app and the other belongs to the watchOS companion app.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockrevisionrecord)*