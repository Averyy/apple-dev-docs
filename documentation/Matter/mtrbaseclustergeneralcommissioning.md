# MTRBaseClusterGeneralCommissioning

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
class MTRBaseClusterGeneralCommissioning
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclustergeneralcommissioning/init(device:endpoint:queue:).md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclustergeneralcommissioning/init(device:endpointid:queue:).md)
### Instance Methods
- [func armFailSafe(with: MTRGeneralCommissioningClusterArmFailSafeParams, completion: (MTRGeneralCommissioningClusterArmFailSafeResponseParams?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/armfailsafe(with:completion:).md)
- [func armFailSafe(with: MTRGeneralCommissioningClusterArmFailSafeParams, completionHandler: (MTRGeneralCommissioningClusterArmFailSafeResponseParams?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/armfailsafe(with:completionhandler:).md)
- [func commissioningComplete(completion: (MTRGeneralCommissioningClusterCommissioningCompleteResponseParams?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/commissioningcomplete(completion:).md)
- [func commissioningComplete(completionHandler: (MTRGeneralCommissioningClusterCommissioningCompleteResponseParams?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/commissioningcomplete(completionhandler:).md)
- [func commissioningComplete(with: MTRGeneralCommissioningClusterCommissioningCompleteParams?, completion: (MTRGeneralCommissioningClusterCommissioningCompleteResponseParams?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/commissioningcomplete(with:completion:).md)
- [func commissioningComplete(with: MTRGeneralCommissioningClusterCommissioningCompleteParams?, completionHandler: (MTRGeneralCommissioningClusterCommissioningCompleteResponseParams?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/commissioningcomplete(with:completionhandler:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributeattributelist(completion:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributeattributelist(completionhandler:).md)
- [func readAttributeBasicCommissioningInfo(completion: (MTRGeneralCommissioningClusterBasicCommissioningInfo?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributebasiccommissioninginfo(completion:).md)
- [func readAttributeBasicCommissioningInfo(completionHandler: (MTRGeneralCommissioningClusterBasicCommissioningInfo?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributebasiccommissioninginfo(completionhandler:).md)
- [func readAttributeBreadcrumb(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributebreadcrumb(completion:).md)
- [func readAttributeBreadcrumb(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributebreadcrumb(completionhandler:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributeclusterrevision(completion:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributefeaturemap(completion:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributefeaturemap(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributegeneratedcommandlist(completionhandler:).md)
- [func readAttributeLocationCapability(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributelocationcapability(completion:).md)
- [func readAttributeLocationCapability(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributelocationcapability(completionhandler:).md)
- [func readAttributeRegulatoryConfig(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributeregulatoryconfig(completion:).md)
- [func readAttributeRegulatoryConfig(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributeregulatoryconfig(completionhandler:).md)
- [func readAttributeSupportsConcurrentConnection(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributesupportsconcurrentconnection(completion:).md)
- [func readAttributeSupportsConcurrentConnection(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributesupportsconcurrentconnection(completionhandler:).md)
- [func setRegulatoryConfigWith(MTRGeneralCommissioningClusterSetRegulatoryConfigParams, completion: (MTRGeneralCommissioningClusterSetRegulatoryConfigResponseParams?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/setregulatoryconfigwith(_:completion:).md)
- [func setRegulatoryConfigWith(MTRGeneralCommissioningClusterSetRegulatoryConfigParams, completionHandler: (MTRGeneralCommissioningClusterSetRegulatoryConfigResponseParams?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/setregulatoryconfigwith(_:completionhandler:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBasicCommissioningInfo(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRGeneralCommissioningClusterBasicCommissioningInfo?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributebasiccommissioninginfo(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBasicCommissioningInfo(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRGeneralCommissioningClusterBasicCommissioningInfo?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributebasiccommissioninginfo(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBreadcrumb(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributebreadcrumb(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBreadcrumb(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributebreadcrumb(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLocationCapability(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributelocationcapability(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLocationCapability(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributelocationcapability(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeRegulatoryConfig(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributeregulatoryconfig(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeRegulatoryConfig(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributeregulatoryconfig(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSupportsConcurrentConnection(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributesupportsconcurrentconnection(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSupportsConcurrentConnection(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/subscribeattributesupportsconcurrentconnection(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func writeAttributeBreadcrumb(withValue: NSNumber, completion: ((any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/writeattributebreadcrumb(withvalue:completion:).md)
- [func writeAttributeBreadcrumb(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/writeattributebreadcrumb(withvalue:completionhandler:).md)
- [func writeAttributeBreadcrumb(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/writeattributebreadcrumb(withvalue:params:completion:).md)
- [func writeAttributeBreadcrumb(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/writeattributebreadcrumb(withvalue:params:completionhandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeBasicCommissioningInfo(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (MTRGeneralCommissioningClusterBasicCommissioningInfo?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributebasiccommissioninginfo(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeBasicCommissioningInfo(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRGeneralCommissioningClusterBasicCommissioningInfo?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributebasiccommissioninginfo(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeBreadcrumb(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributebreadcrumb(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeBreadcrumb(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributebreadcrumb(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeLocationCapability(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributelocationcapability(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeLocationCapability(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributelocationcapability(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeRegulatoryConfig(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributeregulatoryconfig(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeRegulatoryConfig(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributeregulatoryconfig(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSupportsConcurrentConnection(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributesupportsconcurrentconnection(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeSupportsConcurrentConnection(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneralcommissioning/readattributesupportsconcurrentconnection(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustergeneralcommissioning)*