# MTRBaseClusterOvenCavityOperationalState

**Framework**: Matter  
**Kind**: class

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

#### Overview

This cluster supports remotely monitoring and, where supported, changing the operational state of an Oven.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterovencavityoperationalstate/init(device:endpointid:queue:).md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributeattributelist(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributeclusterrevision(completion:).md)
- [func readAttributeCountdownTime(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributecountdowntime(completion:).md)
- [func readAttributeCurrentPhase(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributecurrentphase(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeOperationalError(completion: (MTROvenCavityOperationalStateClusterErrorStateStruct?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributeoperationalerror(completion:).md)
- [func readAttributeOperationalState(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributeoperationalstate(completion:).md)
- [func readAttributeOperationalStateList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributeoperationalstatelist(completion:).md)
- [func readAttributePhaseList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributephaselist(completion:).md)
- [func start(completion: (MTROvenCavityOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/start(completion:).md)
- [func start(with: MTROvenCavityOperationalStateClusterStartParams?, completion: (MTROvenCavityOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/start(with:completion:).md)
  Command Start
- [func stop(completion: (MTROvenCavityOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/stop(completion:).md)
- [func stop(with: MTROvenCavityOperationalStateClusterStopParams?, completion: (MTROvenCavityOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/stop(with:completion:).md)
  Command Stop
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCountdownTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/subscribeattributecountdowntime(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCurrentPhase(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/subscribeattributecurrentphase(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOperationalError(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTROvenCavityOperationalStateClusterErrorStateStruct?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/subscribeattributeoperationalerror(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOperationalState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/subscribeattributeoperationalstate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOperationalStateList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/subscribeattributeoperationalstatelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePhaseList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/subscribeattributephaselist(with:subscriptionestablished:reporthandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCountdownTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributecountdowntime(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCurrentPhase(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributecurrentphase(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeOperationalError(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTROvenCavityOperationalStateClusterErrorStateStruct?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributeoperationalerror(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeOperationalState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributeoperationalstate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeOperationalStateList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributeoperationalstatelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePhaseList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterovencavityoperationalstate/readattributephaselist(withclusterstatecache:endpoint:queue:completion:).md)

## Relationships

### Inherits From
- [MTRGenericBaseCluster](mtrgenericbasecluster.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterovencavityoperationalstate)*