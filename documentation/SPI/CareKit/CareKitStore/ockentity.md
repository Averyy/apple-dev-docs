---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockentity"
framework: "CareKit/CareKitStore"
---

# OCKEntity

**Framework**: CareKit/CareKitStore  
**Kind**: enum  
**Role**: Enumeration

Holds one of several possible modified entities.

## Declaration

```swift
enum OCKEntity
```

## Topics

### Enumeration Cases
- [case carePlan(OCKCarePlan)](./ockentity/careplan%28_%29.md)
  A care plan entity.
- [case contact(OCKContact)](./ockentity/contact%28_%29.md)
  A contact entity.
- [case healthKitTask(OCKHealthKitTask)](./ockentity/healthkittask%28_%29.md)
  A HealthKit linked task.
- [case outcome(OCKOutcome)](./ockentity/outcome%28_%29.md)
  An outcome entity.
- [case patient(OCKPatient)](./ockentity/patient%28_%29.md)
  A patient entity.
- [OCKEntity.task(_:)](./ockentity/task%28_%29.md)
  A task entity.
### Initializers
- [init(from: Decoder) throws](./ockentity/init%28from%29.md)
### Instance Properties
- [var entityType: EntityType](./ockentity/entitytype-swift.property.md)
  The type of the contained entity.
### Instance Methods
- [func encode(to: Encoder) throws](./ockentity/encode%28to%29.md)
### Enumerations
- [OCKEntity.EntityType](./ockentity/entitytype-swift.enum.md)
  Describes the types of entities that may be included in a revision record.
### Default Implementations
- [Equatable Implementations](./ockentity/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Synchronization
- [protocol OCKRemoteSynchronizable](./ockremotesynchronizable.md)
  Implement this protocol to allow CareKitStore to synchronize against an endpoint of your choosing.
- [protocol OCKRemoteSynchronizationDelegate](./ockremotesynchronizationdelegate.md)
  Implement this protocol to listen for important events coming from an `OCKRemoteSynchronizable`.
- [struct OCKRevisionRecord](./ockrevisionrecord.md)
  Revision records are exchanged by the CareKit and a remote database during synchronization. Each revision record contains an array of entities as well as a knowledge vector.
- [class OCKWatchConnectivityPeer](./ockwatchconnectivitypeer.md)
  `OCKWatchConnectivityPeer` enables synchronizing two instances of `OCKStore` where one store is part of an iPhone app and the other belongs to the watchOS companion app.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockentity)*