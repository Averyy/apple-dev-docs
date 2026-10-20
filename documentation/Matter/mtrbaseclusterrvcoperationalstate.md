# MTRBaseClusterRVCOperationalState

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
class MTRBaseClusterRVCOperationalState
```

```objc
@interface MTRBaseClusterRVCOperationalState : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterrvcoperationalstate/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func pause(completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/pause%28completion%29.md)
- [func pause(with: MTRRVCOperationalStateClusterPauseParams?, completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/pause%28with,completion%29.md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributeattributelist%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributeclusterrevision%28completion%29.md)
- [func readAttributeCountdownTime(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributecountdowntime%28completion%29.md)
- [func readAttributeCurrentPhase(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributecurrentphase%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeOperationalError(completion: (MTRRVCOperationalStateClusterErrorStateStruct?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributeoperationalerror%28completion%29.md)
- [func readAttributeOperationalState(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributeoperationalstate%28completion%29.md)
- [func readAttributeOperationalStateList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributeoperationalstatelist%28completion%29.md)
- [func readAttributePhaseList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributephaselist%28completion%29.md)
- [func resume(completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/resume%28completion%29.md)
- [func resume(with: MTRRVCOperationalStateClusterResumeParams?, completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/resume%28with,completion%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCountdownTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/subscribeattributecountdowntime%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCurrentPhase(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/subscribeattributecurrentphase%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOperationalError(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRRVCOperationalStateClusterErrorStateStruct?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/subscribeattributeoperationalerror%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOperationalState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/subscribeattributeoperationalstate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOperationalStateList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/subscribeattributeoperationalstatelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePhaseList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/subscribeattributephaselist%28with,subscriptionestablished,reporthandler%29.md)
- [func goHome(completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/gohome%28completion%29.md)
- [func goHome(with: MTRRVCOperationalStateClusterGoHomeParams?, completion: (MTRRVCOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/gohome%28with,completion%29.md)
  Command GoHome
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCountdownTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributecountdowntime%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCurrentPhase(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributecurrentphase%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeOperationalError(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRRVCOperationalStateClusterErrorStateStruct?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributeoperationalerror%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeOperationalState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributeoperationalstate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeOperationalStateList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributeoperationalstatelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePhaseList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterrvcoperationalstate/readattributephaselist%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterrvcoperationalstate)*