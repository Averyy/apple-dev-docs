# MTRBaseClusterActions

**Framework**: Matter  
**Kind**: class

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

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclusteractions/init(device:endpoint:queue:).md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusteractions/init(device:endpointid:queue:).md)
### Instance Methods
- [func disableAction(with: MTRActionsClusterDisableActionParams, completion: MTRStatusCompletion)](mtrbaseclusteractions/disableaction(with:completion:).md)
- [func disableAction(with: MTRActionsClusterDisableActionParams, completionHandler: MTRStatusCompletion)](mtrbaseclusteractions/disableaction(with:completionhandler:).md)
- [func disableActionWithDuration(with: MTRActionsClusterDisableActionWithDurationParams, completion: MTRStatusCompletion)](mtrbaseclusteractions/disableactionwithduration(with:completion:).md)
- [func disableActionWithDuration(with: MTRActionsClusterDisableActionWithDurationParams, completionHandler: MTRStatusCompletion)](mtrbaseclusteractions/disableactionwithduration(with:completionhandler:).md)
- [func enableAction(with: MTRActionsClusterEnableActionParams, completion: MTRStatusCompletion)](mtrbaseclusteractions/enableaction(with:completion:).md)
- [func enableAction(with: MTRActionsClusterEnableActionParams, completionHandler: MTRStatusCompletion)](mtrbaseclusteractions/enableaction(with:completionhandler:).md)
- [func enableActionWithDuration(with: MTRActionsClusterEnableActionWithDurationParams, completion: MTRStatusCompletion)](mtrbaseclusteractions/enableactionwithduration(with:completion:).md)
- [func enableActionWithDuration(with: MTRActionsClusterEnableActionWithDurationParams, completionHandler: MTRStatusCompletion)](mtrbaseclusteractions/enableactionwithduration(with:completionhandler:).md)
- [func instantAction(with: MTRActionsClusterInstantActionParams, completion: MTRStatusCompletion)](mtrbaseclusteractions/instantaction(with:completion:).md)
- [func instantAction(with: MTRActionsClusterInstantActionParams, completionHandler: MTRStatusCompletion)](mtrbaseclusteractions/instantaction(with:completionhandler:).md)
- [func instantActionWithTransition(with: MTRActionsClusterInstantActionWithTransitionParams, completion: MTRStatusCompletion)](mtrbaseclusteractions/instantactionwithtransition(with:completion:).md)
- [func instantActionWithTransition(with: MTRActionsClusterInstantActionWithTransitionParams, completionHandler: MTRStatusCompletion)](mtrbaseclusteractions/instantactionwithtransition(with:completionhandler:).md)
- [func pauseAction(with: MTRActionsClusterPauseActionParams, completion: MTRStatusCompletion)](mtrbaseclusteractions/pauseaction(with:completion:).md)
- [func pauseAction(with: MTRActionsClusterPauseActionParams, completionHandler: MTRStatusCompletion)](mtrbaseclusteractions/pauseaction(with:completionhandler:).md)
- [func pauseActionWithDuration(with: MTRActionsClusterPauseActionWithDurationParams, completion: MTRStatusCompletion)](mtrbaseclusteractions/pauseactionwithduration(with:completion:).md)
- [func pauseActionWithDuration(with: MTRActionsClusterPauseActionWithDurationParams, completionHandler: MTRStatusCompletion)](mtrbaseclusteractions/pauseactionwithduration(with:completionhandler:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeActionList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeactionlist(completion:).md)
- [func readAttributeActionList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeactionlist(completionhandler:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeattributelist(completion:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeattributelist(completionhandler:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeclusterrevision(completion:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeEndpointLists(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeendpointlists(completion:).md)
- [func readAttributeEndpointLists(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeendpointlists(completionhandler:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributefeaturemap(completion:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributefeaturemap(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributegeneratedcommandlist(completionhandler:).md)
- [func readAttributeSetupURL(completion: (String?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributesetupurl(completion:).md)
- [func readAttributeSetupURL(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributesetupurl(completionhandler:).md)
- [func resumeAction(with: MTRActionsClusterResumeActionParams, completion: MTRStatusCompletion)](mtrbaseclusteractions/resumeaction(with:completion:).md)
- [func resumeAction(with: MTRActionsClusterResumeActionParams, completionHandler: MTRStatusCompletion)](mtrbaseclusteractions/resumeaction(with:completionhandler:).md)
- [func startAction(with: MTRActionsClusterStartActionParams, completion: MTRStatusCompletion)](mtrbaseclusteractions/startaction(with:completion:).md)
- [func startAction(with: MTRActionsClusterStartActionParams, completionHandler: MTRStatusCompletion)](mtrbaseclusteractions/startaction(with:completionhandler:).md)
- [func startActionWithDuration(with: MTRActionsClusterStartActionWithDurationParams, completion: MTRStatusCompletion)](mtrbaseclusteractions/startactionwithduration(with:completion:).md)
- [func startActionWithDuration(with: MTRActionsClusterStartActionWithDurationParams, completionHandler: MTRStatusCompletion)](mtrbaseclusteractions/startactionwithduration(with:completionhandler:).md)
- [func stopAction(with: MTRActionsClusterStopActionParams, completion: MTRStatusCompletion)](mtrbaseclusteractions/stopaction(with:completion:).md)
- [func stopAction(with: MTRActionsClusterStopActionParams, completionHandler: MTRStatusCompletion)](mtrbaseclusteractions/stopaction(with:completionhandler:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeActionList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/subscribeattributeactionlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeActionList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/subscribeattributeactionlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractions/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractions/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeEndpointLists(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/subscribeattributeendpointlists(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeEndpointLists(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/subscribeattributeendpointlists(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractions/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractions/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSetupURL(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusteractions/subscribeattributesetupurl(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSetupURL(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusteractions/subscribeattributesetupurl(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeActionList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeactionlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeActionList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeactionlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeEndpointLists(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeendpointlists(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeEndpointLists(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributeendpointlists(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSetupURL(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributesetupurl(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeSetupURL(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusteractions/readattributesetupurl(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteractions)*