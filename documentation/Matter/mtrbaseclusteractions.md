# MTRBaseClusterActions

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRBaseClusterActions
```

```objc
@interface MTRBaseClusterActions : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclusteractions/init%28device,endpoint,queue%29.md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusteractions/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func disableAction(with: MTRActionsClusterDisableActionParams, completion: ((any Error)?) -> Void)](./mtrbaseclusteractions/disableaction%28with,completion%29.md)
- [func disableAction(with: MTRActionsClusterDisableActionParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteractions/disableaction%28with,completionhandler%29.md)
- [func disableActionWithDuration(with: MTRActionsClusterDisableActionWithDurationParams, completion: ((any Error)?) -> Void)](./mtrbaseclusteractions/disableactionwithduration%28with,completion%29.md)
- [func disableActionWithDuration(with: MTRActionsClusterDisableActionWithDurationParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteractions/disableactionwithduration%28with,completionhandler%29.md)
- [func enableAction(with: MTRActionsClusterEnableActionParams, completion: ((any Error)?) -> Void)](./mtrbaseclusteractions/enableaction%28with,completion%29.md)
- [func enableAction(with: MTRActionsClusterEnableActionParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteractions/enableaction%28with,completionhandler%29.md)
- [func enableActionWithDuration(with: MTRActionsClusterEnableActionWithDurationParams, completion: ((any Error)?) -> Void)](./mtrbaseclusteractions/enableactionwithduration%28with,completion%29.md)
- [func enableActionWithDuration(with: MTRActionsClusterEnableActionWithDurationParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteractions/enableactionwithduration%28with,completionhandler%29.md)
- [func instantAction(with: MTRActionsClusterInstantActionParams, completion: ((any Error)?) -> Void)](./mtrbaseclusteractions/instantaction%28with,completion%29.md)
- [func instantAction(with: MTRActionsClusterInstantActionParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteractions/instantaction%28with,completionhandler%29.md)
- [func instantActionWithTransition(with: MTRActionsClusterInstantActionWithTransitionParams, completion: ((any Error)?) -> Void)](./mtrbaseclusteractions/instantactionwithtransition%28with,completion%29.md)
- [func instantActionWithTransition(with: MTRActionsClusterInstantActionWithTransitionParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteractions/instantactionwithtransition%28with,completionhandler%29.md)
- [func pauseAction(with: MTRActionsClusterPauseActionParams, completion: ((any Error)?) -> Void)](./mtrbaseclusteractions/pauseaction%28with,completion%29.md)
- [func pauseAction(with: MTRActionsClusterPauseActionParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteractions/pauseaction%28with,completionhandler%29.md)
- [func pauseActionWithDuration(with: MTRActionsClusterPauseActionWithDurationParams, completion: ((any Error)?) -> Void)](./mtrbaseclusteractions/pauseactionwithduration%28with,completion%29.md)
- [func pauseActionWithDuration(with: MTRActionsClusterPauseActionWithDurationParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteractions/pauseactionwithduration%28with,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeActionList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeactionlist%28completion%29.md)
- [func readAttributeActionList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeactionlist%28completionhandler%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeattributelist%28completion%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeclusterrevision%28completion%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeEndpointLists(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeendpointlists%28completion%29.md)
- [func readAttributeEndpointLists(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeendpointlists%28completionhandler%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributefeaturemap%28completion%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func readAttributeSetupURL(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributesetupurl%28completion%29.md)
- [func readAttributeSetupURL(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributesetupurl%28completionhandler%29.md)
- [func resumeAction(with: MTRActionsClusterResumeActionParams, completion: ((any Error)?) -> Void)](./mtrbaseclusteractions/resumeaction%28with,completion%29.md)
- [func resumeAction(with: MTRActionsClusterResumeActionParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteractions/resumeaction%28with,completionhandler%29.md)
- [func startAction(with: MTRActionsClusterStartActionParams, completion: ((any Error)?) -> Void)](./mtrbaseclusteractions/startaction%28with,completion%29.md)
- [func startAction(with: MTRActionsClusterStartActionParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteractions/startaction%28with,completionhandler%29.md)
- [func startActionWithDuration(with: MTRActionsClusterStartActionWithDurationParams, completion: ((any Error)?) -> Void)](./mtrbaseclusteractions/startactionwithduration%28with,completion%29.md)
- [func startActionWithDuration(with: MTRActionsClusterStartActionWithDurationParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteractions/startactionwithduration%28with,completionhandler%29.md)
- [func stopAction(with: MTRActionsClusterStopActionParams, completion: ((any Error)?) -> Void)](./mtrbaseclusteractions/stopaction%28with,completion%29.md)
- [func stopAction(with: MTRActionsClusterStopActionParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteractions/stopaction%28with,completionhandler%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeActionList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/subscribeattributeactionlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeActionList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/subscribeattributeactionlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteractions/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteractions/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeEndpointLists(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/subscribeattributeendpointlists%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeEndpointLists(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/subscribeattributeendpointlists%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteractions/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteractions/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSetupURL(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusteractions/subscribeattributesetupurl%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSetupURL(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusteractions/subscribeattributesetupurl%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeActionList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeactionlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeActionList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeactionlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeEndpointLists(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeendpointlists%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeEndpointLists(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributeendpointlists%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSetupURL(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributesetupurl%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeSetupURL(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusteractions/readattributesetupurl%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteractions)*