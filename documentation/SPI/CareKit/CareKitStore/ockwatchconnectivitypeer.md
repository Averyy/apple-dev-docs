---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockwatchconnectivitypeer"
framework: "CareKit/CareKitStore"
---

# OCKWatchConnectivityPeer

**Framework**: CareKit/CareKitStore  
**Kind**: class  
**Role**: Class

`OCKWatchConnectivityPeer` enables synchronizing two instances of `OCKStore` where one store is part of an iPhone app and the other belongs to the watchOS companion app.

## Declaration

```swift
final class OCKWatchConnectivityPeer
```

## Overview

The watch is capable of waking its companion app to send it messages, so the watch can synchronize with the phone at any time. The phone however, cannot wake the watch, so synchronizations initiated from the phone will only succeed when the companion app is in a reachable state.

## Topics

### Initializers
- [init()](./ockwatchconnectivitypeer/init%28%29.md)
### Instance Properties
- [var automaticallySynchronizes: Bool](./ockwatchconnectivitypeer/automaticallysynchronizes.md)
- [var delegate: OCKRemoteSynchronizationDelegate?](./ockwatchconnectivitypeer/delegate.md)
### Instance Methods
- [func chooseConflictResolution(conflicts: [OCKEntity], completion: OCKResultClosure<OCKEntity>)](./ockwatchconnectivitypeer/chooseconflictresolution%28conflicts,completion%29.md)
- [func pullRevisions(since: OCKRevisionRecord.KnowledgeVector, mergeRevision: @Sendable (OCKRevisionRecord) -> Void, completion: @Sendable (Error?) -> Void)](./ockwatchconnectivitypeer/pullrevisions%28since,mergerevision,completion%29.md)
- [func pushRevisions(deviceRevisions: [OCKRevisionRecord], deviceKnowledge: OCKRevisionRecord.KnowledgeVector, completion: (Error?) -> Void)](./ockwatchconnectivitypeer/pushrevisions%28devicerevisions,deviceknowledge,completion%29.md)
- [func reply(to: [String : Any], store: OCKStore, sendReply: (_ message: [String : Any]) -> Void)](./ockwatchconnectivitypeer/reply%28to,store,sendreply%29.md)
  You should call this method anytime you receive a message from the companion app. CareKit will inspect the message to see if it contains any synchronization requests that require a response. If there are, the appropriate response will be returned. Be sure to pass the returned keys and values to the reply handler in `WCSessionDelegate`’s `session(_:didReceiveMessage:replyHandler:)` method.

## Relationships

### Conforms To
- [OCKRemoteSynchronizable](./ockremotesynchronizable.md)
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
- [enum OCKEntity](./ockentity.md)
  Holds one of several possible modified entities.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockwatchconnectivitypeer)*