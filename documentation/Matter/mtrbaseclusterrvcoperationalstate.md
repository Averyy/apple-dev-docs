# MTRBaseClusterRVCOperationalState

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
class MTRBaseClusterRVCOperationalState
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterrvcoperationalstate/init(device:endpointid:queue:).md)
### Instance Methods
- [func pause(completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/pause(completion:).md)
- [func pause(with: MTRRVCOperationalStateClusterPauseParams?, completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/pause(with:completion:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributeattributelist(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributeclusterrevision(completion:).md)
- [func readAttributeCountdownTime(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributecountdowntime(completion:).md)
- [func readAttributeCurrentPhase(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributecurrentphase(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeOperationalError(completion: (MTRRVCOperationalStateClusterErrorStateStruct?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributeoperationalerror(completion:).md)
- [func readAttributeOperationalState(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributeoperationalstate(completion:).md)
- [func readAttributeOperationalStateList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributeoperationalstatelist(completion:).md)
- [func readAttributePhaseList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributephaselist(completion:).md)
- [func resume(completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/resume(completion:).md)
- [func resume(with: MTRRVCOperationalStateClusterResumeParams?, completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/resume(with:completion:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCountdownTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/subscribeattributecountdowntime(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCurrentPhase(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/subscribeattributecurrentphase(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOperationalError(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRRVCOperationalStateClusterErrorStateStruct?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/subscribeattributeoperationalerror(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOperationalState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/subscribeattributeoperationalstate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOperationalStateList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/subscribeattributeoperationalstatelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePhaseList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/subscribeattributephaselist(with:subscriptionestablished:reporthandler:).md)
- [func goHome(completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/gohome(completion:).md)
- [func goHome(with: MTRRVCOperationalStateClusterGoHomeParams?, completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/gohome(with:completion:).md)
  Command GoHome
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCountdownTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributecountdowntime(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCurrentPhase(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributecurrentphase(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeOperationalError(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRRVCOperationalStateClusterErrorStateStruct?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributeoperationalerror(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeOperationalState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributeoperationalstate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeOperationalStateList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributeoperationalstatelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePhaseList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterrvcoperationalstate/readattributephaselist(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterrvcoperationalstate)*