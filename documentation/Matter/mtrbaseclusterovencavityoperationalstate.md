# MTRBaseClusterOvenCavityOperationalState

**Framework**: Matter  
**Kind**: class  
**Role**: Class

Cluster Oven Cavity Operational State

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
class MTRBaseClusterOvenCavityOperationalState
```

```objc
@interface MTRBaseClusterOvenCavityOperationalState : MTRGenericBaseCluster
```

## Overview

This cluster supports remotely monitoring and, where supported, changing the operational state of an Oven.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterovencavityoperationalstate/init%28device,endpointid,queue%29.md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributeattributelist%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributeclusterrevision%28completion%29.md)
- [func readAttributeCountdownTime(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributecountdowntime%28completion%29.md)
- [func readAttributeCurrentPhase(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributecurrentphase%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeOperationalError(completion: (MTROvenCavityOperationalStateClusterErrorStateStruct?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributeoperationalerror%28completion%29.md)
- [func readAttributeOperationalState(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributeoperationalstate%28completion%29.md)
- [func readAttributeOperationalStateList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributeoperationalstatelist%28completion%29.md)
- [func readAttributePhaseList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributephaselist%28completion%29.md)
- [func start(completion: (MTROvenCavityOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/start%28completion%29.md)
- [func start(with: MTROvenCavityOperationalStateClusterStartParams?, completion: (MTROvenCavityOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/start%28with,completion%29.md)
  Command Start
- [func stop(completion: (MTROvenCavityOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/stop%28completion%29.md)
- [func stop(with: MTROvenCavityOperationalStateClusterStopParams?, completion: (MTROvenCavityOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/stop%28with,completion%29.md)
  Command Stop
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCountdownTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/subscribeattributecountdowntime%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCurrentPhase(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/subscribeattributecurrentphase%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOperationalError(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTROvenCavityOperationalStateClusterErrorStateStruct?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/subscribeattributeoperationalerror%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOperationalState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/subscribeattributeoperationalstate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOperationalStateList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/subscribeattributeoperationalstatelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePhaseList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/subscribeattributephaselist%28with,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCountdownTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributecountdowntime%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCurrentPhase(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributecurrentphase%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeOperationalError(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTROvenCavityOperationalStateClusterErrorStateStruct?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributeoperationalerror%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeOperationalState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributeoperationalstate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeOperationalStateList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributeoperationalstatelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePhaseList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovencavityoperationalstate/readattributephaselist%28withclusterstatecache,endpoint,queue,completion%29.md)

## Relationships

### Inherits From
- [MTRGenericBaseCluster](./mtrgenericbasecluster.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterovencavityoperationalstate)*