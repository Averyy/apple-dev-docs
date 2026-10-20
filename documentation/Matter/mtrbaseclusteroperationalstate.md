# MTRBaseClusterOperationalState

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRBaseClusterOperationalState : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusteroperationalstate/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func pause(completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/pause%28completion%29.md)
- [func pause(with: MTROperationalStateClusterPauseParams?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/pause%28with,completion%29.md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributeattributelist%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributeclusterrevision%28completion%29.md)
- [func readAttributeCountdownTime(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributecountdowntime%28completion%29.md)
- [func readAttributeCurrentPhase(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributecurrentphase%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeOperationalError(completion: (MTROperationalStateClusterErrorStateStruct?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributeoperationalerror%28completion%29.md)
- [func readAttributeOperationalState(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributeoperationalstate%28completion%29.md)
- [func readAttributeOperationalStateList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributeoperationalstatelist%28completion%29.md)
- [func readAttributePhaseList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributephaselist%28completion%29.md)
- [func resume(completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/resume%28completion%29.md)
- [func resume(with: MTROperationalStateClusterResumeParams?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/resume%28with,completion%29.md)
- [func start(completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/start%28completion%29.md)
- [func start(with: MTROperationalStateClusterStartParams?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/start%28with,completion%29.md)
- [func stop(completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/stop%28completion%29.md)
- [func stop(with: MTROperationalStateClusterStopParams?, completion: (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/stop%28with,completion%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCountdownTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/subscribeattributecountdowntime%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCurrentPhase(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/subscribeattributecurrentphase%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOperationalError(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTROperationalStateClusterErrorStateStruct?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/subscribeattributeoperationalerror%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOperationalState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/subscribeattributeoperationalstate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOperationalStateList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/subscribeattributeoperationalstatelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePhaseList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/subscribeattributephaselist%28with,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCountdownTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributecountdowntime%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCurrentPhase(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributecurrentphase%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeOperationalError(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTROperationalStateClusterErrorStateStruct?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributeoperationalerror%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeOperationalState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributeoperationalstate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeOperationalStateList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributeoperationalstatelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePhaseList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalstate/readattributephaselist%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteroperationalstate)*