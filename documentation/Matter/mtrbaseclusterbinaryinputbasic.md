# MTRBaseClusterBinaryInputBasic

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
class MTRBaseClusterBinaryInputBasic
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclusterbinaryinputbasic/init(device:endpoint:queue:).md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterbinaryinputbasic/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeActiveText(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeactivetext(completion:).md)
- [func readAttributeActiveText(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeactivetext(completionhandler:).md)
- [func readAttributeApplicationType(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeapplicationtype(completion:).md)
- [func readAttributeApplicationType(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeapplicationtype(completionhandler:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeattributelist(completion:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeattributelist(completionhandler:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeclusterrevision(completion:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeDescription(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributedescription(completion:).md)
- [func readAttributeDescription(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributedescription(completionhandler:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributefeaturemap(completion:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributefeaturemap(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributegeneratedcommandlist(completionhandler:).md)
- [func readAttributeInactiveText(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeinactivetext(completion:).md)
- [func readAttributeInactiveText(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeinactivetext(completionhandler:).md)
- [func readAttributeOutOfService(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeoutofservice(completion:).md)
- [func readAttributeOutOfService(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeoutofservice(completionhandler:).md)
- [func readAttributePolarity(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributepolarity(completion:).md)
- [func readAttributePolarity(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributepolarity(completionhandler:).md)
- [func readAttributePresentValue(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributepresentvalue(completion:).md)
- [func readAttributePresentValue(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributepresentvalue(completionhandler:).md)
- [func readAttributeReliability(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributereliability(completion:).md)
- [func readAttributeReliability(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributereliability(completionhandler:).md)
- [func readAttributeStatusFlags(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributestatusflags(completion:).md)
- [func readAttributeStatusFlags(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributestatusflags(completionhandler:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeActiveText(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributeactivetext(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeActiveText(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributeactivetext(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeApplicationType(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributeapplicationtype(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeApplicationType(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributeapplicationtype(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeDescription(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributedescription(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeDescription(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributedescription(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeInactiveText(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributeinactivetext(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeInactiveText(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributeinactivetext(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOutOfService(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributeoutofservice(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOutOfService(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributeoutofservice(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePolarity(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributepolarity(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePolarity(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributepolarity(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePresentValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributepresentvalue(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePresentValue(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributepresentvalue(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeReliability(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributereliability(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeReliability(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributereliability(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeStatusFlags(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributestatusflags(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeStatusFlags(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/subscribeattributestatusflags(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func writeAttributeActiveText(withValue: String, completion: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributeactivetext(withvalue:completion:).md)
- [func writeAttributeActiveText(withValue: String, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributeactivetext(withvalue:completionhandler:).md)
- [func writeAttributeActiveText(withValue: String, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributeactivetext(withvalue:params:completion:).md)
- [func writeAttributeActiveText(withValue: String, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributeactivetext(withvalue:params:completionhandler:).md)
- [func writeAttributeDescription(withValue: String, completion: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributedescription(withvalue:completion:).md)
- [func writeAttributeDescription(withValue: String, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributedescription(withvalue:completionhandler:).md)
- [func writeAttributeDescription(withValue: String, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributedescription(withvalue:params:completion:).md)
- [func writeAttributeDescription(withValue: String, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributedescription(withvalue:params:completionhandler:).md)
- [func writeAttributeInactiveText(withValue: String, completion: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributeinactivetext(withvalue:completion:).md)
- [func writeAttributeInactiveText(withValue: String, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributeinactivetext(withvalue:completionhandler:).md)
- [func writeAttributeInactiveText(withValue: String, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributeinactivetext(withvalue:params:completion:).md)
- [func writeAttributeInactiveText(withValue: String, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributeinactivetext(withvalue:params:completionhandler:).md)
- [func writeAttributeOutOfService(withValue: NSNumber, completion: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributeoutofservice(withvalue:completion:).md)
- [func writeAttributeOutOfService(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributeoutofservice(withvalue:completionhandler:).md)
- [func writeAttributeOutOfService(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributeoutofservice(withvalue:params:completion:).md)
- [func writeAttributeOutOfService(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributeoutofservice(withvalue:params:completionhandler:).md)
- [func writeAttributePresentValue(withValue: NSNumber, completion: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributepresentvalue(withvalue:completion:).md)
- [func writeAttributePresentValue(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributepresentvalue(withvalue:completionhandler:).md)
- [func writeAttributePresentValue(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributepresentvalue(withvalue:params:completion:).md)
- [func writeAttributePresentValue(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributepresentvalue(withvalue:params:completionhandler:).md)
- [func writeAttributeReliability(withValue: NSNumber, completion: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributereliability(withvalue:completion:).md)
- [func writeAttributeReliability(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributereliability(withvalue:completionhandler:).md)
- [func writeAttributeReliability(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributereliability(withvalue:params:completion:).md)
- [func writeAttributeReliability(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/writeattributereliability(withvalue:params:completionhandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeActiveText(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeactivetext(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeActiveText(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeactivetext(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeApplicationType(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeapplicationtype(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeApplicationType(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeapplicationtype(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeDescription(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributedescription(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeDescription(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributedescription(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeInactiveText(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeinactivetext(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeInactiveText(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeinactivetext(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeOutOfService(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeoutofservice(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeOutOfService(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributeoutofservice(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePolarity(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributepolarity(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributePolarity(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributepolarity(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePresentValue(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributepresentvalue(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributePresentValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributepresentvalue(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeReliability(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributereliability(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeReliability(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributereliability(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeStatusFlags(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributestatusflags(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeStatusFlags(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbinaryinputbasic/readattributestatusflags(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbinaryinputbasic)*