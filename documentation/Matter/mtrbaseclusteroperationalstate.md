# MTRBaseClusterOperationalState

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
class MTRBaseClusterOperationalState
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusteroperationalstate/init(device:endpointid:queue:).md)
### Instance Methods
- [func pause(completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/pause(completion:).md)
- [func pause(with: MTROperationalStateClusterPauseParams?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/pause(with:completion:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributeattributelist(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributeclusterrevision(completion:).md)
- [func readAttributeCountdownTime(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributecountdowntime(completion:).md)
- [func readAttributeCurrentPhase(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributecurrentphase(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeOperationalError(completion: (MTROperationalStateClusterErrorStateStruct?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributeoperationalerror(completion:).md)
- [func readAttributeOperationalState(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributeoperationalstate(completion:).md)
- [func readAttributeOperationalStateList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributeoperationalstatelist(completion:).md)
- [func readAttributePhaseList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributephaselist(completion:).md)
- [func resume(completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/resume(completion:).md)
- [func resume(with: MTROperationalStateClusterResumeParams?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/resume(with:completion:).md)
- [func start(completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/start(completion:).md)
- [func start(with: MTROperationalStateClusterStartParams?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/start(with:completion:).md)
- [func stop(completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/stop(completion:).md)
- [func stop(with: MTROperationalStateClusterStopParams?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/stop(with:completion:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCountdownTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/subscribeattributecountdowntime(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCurrentPhase(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/subscribeattributecurrentphase(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOperationalError(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTROperationalStateClusterErrorStateStruct?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/subscribeattributeoperationalerror(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOperationalState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/subscribeattributeoperationalstate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOperationalStateList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/subscribeattributeoperationalstatelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePhaseList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/subscribeattributephaselist(with:subscriptionestablished:reporthandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCountdownTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributecountdowntime(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCurrentPhase(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributecurrentphase(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeOperationalError(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTROperationalStateClusterErrorStateStruct?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributeoperationalerror(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeOperationalState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributeoperationalstate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeOperationalStateList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributeoperationalstatelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePhaseList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalstate/readattributephaselist(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteroperationalstate)*