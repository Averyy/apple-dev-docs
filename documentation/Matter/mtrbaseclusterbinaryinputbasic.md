# MTRBaseClusterBinaryInputBasic

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+ - Deprecated in 18.2
- iPadOS 16.1+ - Deprecated in 18.2
- Mac Catalyst 16.1+ - Deprecated in 18.2
- macOS 13.0+ - Deprecated in 15.2
- tvOS 16.1+ - Deprecated in 18.2
- visionOS 1.0+ - Deprecated in 2.2
- watchOS 9.1+ - Deprecated in 11.2

> **Deprecated**: BinaryInputBasic is deprecated and will be removed

## Declaration

```swift
class MTRBaseClusterBinaryInputBasic
```

```objc
@interface MTRBaseClusterBinaryInputBasic : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclusterbinaryinputbasic/init%28device,endpoint,queue%29.md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterbinaryinputbasic/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeActiveText(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeactivetext%28completion%29.md)
- [func readAttributeActiveText(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeactivetext%28completionhandler%29.md)
- [func readAttributeApplicationType(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeapplicationtype%28completion%29.md)
- [func readAttributeApplicationType(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeapplicationtype%28completionhandler%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeattributelist%28completion%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeclusterrevision%28completion%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeDescription(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributedescription%28completion%29.md)
- [func readAttributeDescription(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributedescription%28completionhandler%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributefeaturemap%28completion%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func readAttributeInactiveText(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeinactivetext%28completion%29.md)
- [func readAttributeInactiveText(completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeinactivetext%28completionhandler%29.md)
- [func readAttributeOutOfService(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeoutofservice%28completion%29.md)
- [func readAttributeOutOfService(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeoutofservice%28completionhandler%29.md)
- [func readAttributePolarity(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributepolarity%28completion%29.md)
- [func readAttributePolarity(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributepolarity%28completionhandler%29.md)
- [func readAttributePresentValue(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributepresentvalue%28completion%29.md)
- [func readAttributePresentValue(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributepresentvalue%28completionhandler%29.md)
- [func readAttributeReliability(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributereliability%28completion%29.md)
- [func readAttributeReliability(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributereliability%28completionhandler%29.md)
- [func readAttributeStatusFlags(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributestatusflags%28completion%29.md)
- [func readAttributeStatusFlags(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributestatusflags%28completionhandler%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeActiveText(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributeactivetext%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeActiveText(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributeactivetext%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeApplicationType(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributeapplicationtype%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeApplicationType(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributeapplicationtype%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeDescription(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributedescription%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeDescription(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributedescription%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeInactiveText(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributeinactivetext%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeInactiveText(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributeinactivetext%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOutOfService(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributeoutofservice%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOutOfService(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributeoutofservice%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePolarity(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributepolarity%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePolarity(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributepolarity%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePresentValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributepresentvalue%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePresentValue(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributepresentvalue%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeReliability(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributereliability%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeReliability(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributereliability%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeStatusFlags(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributestatusflags%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeStatusFlags(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/subscribeattributestatusflags%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeActiveText(withValue: String, completion: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributeactivetext%28withvalue,completion%29.md)
- [func writeAttributeActiveText(withValue: String, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributeactivetext%28withvalue,completionhandler%29.md)
- [func writeAttributeActiveText(withValue: String, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributeactivetext%28withvalue,params,completion%29.md)
- [func writeAttributeActiveText(withValue: String, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributeactivetext%28withvalue,params,completionhandler%29.md)
- [func writeAttributeDescription(withValue: String, completion: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributedescription%28withvalue,completion%29.md)
- [func writeAttributeDescription(withValue: String, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributedescription%28withvalue,completionhandler%29.md)
- [func writeAttributeDescription(withValue: String, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributedescription%28withvalue,params,completion%29.md)
- [func writeAttributeDescription(withValue: String, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributedescription%28withvalue,params,completionhandler%29.md)
- [func writeAttributeInactiveText(withValue: String, completion: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributeinactivetext%28withvalue,completion%29.md)
- [func writeAttributeInactiveText(withValue: String, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributeinactivetext%28withvalue,completionhandler%29.md)
- [func writeAttributeInactiveText(withValue: String, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributeinactivetext%28withvalue,params,completion%29.md)
- [func writeAttributeInactiveText(withValue: String, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributeinactivetext%28withvalue,params,completionhandler%29.md)
- [func writeAttributeOutOfService(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributeoutofservice%28withvalue,completion%29.md)
- [func writeAttributeOutOfService(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributeoutofservice%28withvalue,completionhandler%29.md)
- [func writeAttributeOutOfService(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributeoutofservice%28withvalue,params,completion%29.md)
- [func writeAttributeOutOfService(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributeoutofservice%28withvalue,params,completionhandler%29.md)
- [func writeAttributePresentValue(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributepresentvalue%28withvalue,completion%29.md)
- [func writeAttributePresentValue(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributepresentvalue%28withvalue,completionhandler%29.md)
- [func writeAttributePresentValue(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributepresentvalue%28withvalue,params,completion%29.md)
- [func writeAttributePresentValue(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributepresentvalue%28withvalue,params,completionhandler%29.md)
- [func writeAttributeReliability(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributereliability%28withvalue,completion%29.md)
- [func writeAttributeReliability(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributereliability%28withvalue,completionhandler%29.md)
- [func writeAttributeReliability(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributereliability%28withvalue,params,completion%29.md)
- [func writeAttributeReliability(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/writeattributereliability%28withvalue,params,completionhandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeActiveText(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeactivetext%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeActiveText(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeactivetext%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeApplicationType(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeapplicationtype%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeApplicationType(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeapplicationtype%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeDescription(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributedescription%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeDescription(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributedescription%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeInactiveText(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeinactivetext%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeInactiveText(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeinactivetext%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeOutOfService(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeoutofservice%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeOutOfService(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributeoutofservice%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePolarity(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributepolarity%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributePolarity(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributepolarity%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePresentValue(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributepresentvalue%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributePresentValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributepresentvalue%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeReliability(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributereliability%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeReliability(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributereliability%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeStatusFlags(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributestatusflags%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeStatusFlags(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbinaryinputbasic/readattributestatusflags%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbinaryinputbasic)*