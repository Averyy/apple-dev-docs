---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockremotesynchronizationdelegate"
framework: "CareKit/CareKitStore"
---

# OCKRemoteSynchronizationDelegate

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

Implement this protocol to listen for important events coming from an `OCKRemoteSynchronizable`.

## Declaration

```swift
protocol OCKRemoteSynchronizationDelegate : AnyObject, Sendable
```

## Topics

### Instance Methods
- [func didRequestSynchronization(OCKRemoteSynchronizable)](./ockremotesynchronizationdelegate/didrequestsynchronization%28_%29.md)
  This method will be called whenever a remote endpoint has changes that need to be reflected in the device’s database.
- [func remote(OCKRemoteSynchronizable, didUpdateProgress: Double)](./ockremotesynchronizationdelegate/remote%28_,didupdateprogress%29.md)
  This method will be triggered by the remote to inform the user of progress.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [OCKStore](./ockstore.md)

## See Also

### Synchronization
- [protocol OCKRemoteSynchronizable](./ockremotesynchronizable.md)
  Implement this protocol to allow CareKitStore to synchronize against an endpoint of your choosing.
- [struct OCKRevisionRecord](./ockrevisionrecord.md)
  Revision records are exchanged by the CareKit and a remote database during synchronization. Each revision record contains an array of entities as well as a knowledge vector.
- [enum OCKEntity](./ockentity.md)
  Holds one of several possible modified entities.
- [class OCKWatchConnectivityPeer](./ockwatchconnectivitypeer.md)
  `OCKWatchConnectivityPeer` enables synchronizing two instances of `OCKStore` where one store is part of an iPhone app and the other belongs to the watchOS companion app.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockremotesynchronizationdelegate)*