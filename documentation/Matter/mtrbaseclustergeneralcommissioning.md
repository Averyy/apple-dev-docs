# MTRBaseClusterGeneralCommissioning

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
class MTRBaseClusterGeneralCommissioning
```

```objc
@interface MTRBaseClusterGeneralCommissioning : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclustergeneralcommissioning/init%28device,endpoint,queue%29.md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclustergeneralcommissioning/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func armFailSafe(with: MTRGeneralCommissioningClusterArmFailSafeParams, completion: (MTRGeneralCommissioningClusterArmFailSafeResponseParams?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/armfailsafe%28with,completion%29.md)
- [func armFailSafe(with: MTRGeneralCommissioningClusterArmFailSafeParams, completionHandler: (MTRGeneralCommissioningClusterArmFailSafeResponseParams?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/armfailsafe%28with,completionhandler%29.md)
- [func commissioningComplete(completion: (MTRGeneralCommissioningClusterCommissioningCompleteResponseParams?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/commissioningcomplete%28completion%29.md)
- [func commissioningComplete(completionHandler: (MTRGeneralCommissioningClusterCommissioningCompleteResponseParams?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/commissioningcomplete%28completionhandler%29.md)
- [func commissioningComplete(with: MTRGeneralCommissioningClusterCommissioningCompleteParams?, completion: (MTRGeneralCommissioningClusterCommissioningCompleteResponseParams?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/commissioningcomplete%28with,completion%29.md)
- [func commissioningComplete(with: MTRGeneralCommissioningClusterCommissioningCompleteParams?, completionHandler: (MTRGeneralCommissioningClusterCommissioningCompleteResponseParams?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/commissioningcomplete%28with,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributeattributelist%28completion%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeBasicCommissioningInfo(completion: (MTRGeneralCommissioningClusterBasicCommissioningInfo?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributebasiccommissioninginfo%28completion%29.md)
- [func readAttributeBasicCommissioningInfo(completionHandler: (MTRGeneralCommissioningClusterBasicCommissioningInfo?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributebasiccommissioninginfo%28completionhandler%29.md)
- [func readAttributeBreadcrumb(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributebreadcrumb%28completion%29.md)
- [func readAttributeBreadcrumb(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributebreadcrumb%28completionhandler%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributeclusterrevision%28completion%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributefeaturemap%28completion%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func readAttributeLocationCapability(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributelocationcapability%28completion%29.md)
- [func readAttributeLocationCapability(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributelocationcapability%28completionhandler%29.md)
- [func readAttributeRegulatoryConfig(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributeregulatoryconfig%28completion%29.md)
- [func readAttributeRegulatoryConfig(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributeregulatoryconfig%28completionhandler%29.md)
- [func readAttributeSupportsConcurrentConnection(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributesupportsconcurrentconnection%28completion%29.md)
- [func readAttributeSupportsConcurrentConnection(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributesupportsconcurrentconnection%28completionhandler%29.md)
- [func setRegulatoryConfigWith(MTRGeneralCommissioningClusterSetRegulatoryConfigParams, completion: (MTRGeneralCommissioningClusterSetRegulatoryConfigResponseParams?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/setregulatoryconfigwith%28_,completion%29.md)
- [func setRegulatoryConfigWith(MTRGeneralCommissioningClusterSetRegulatoryConfigParams, completionHandler: (MTRGeneralCommissioningClusterSetRegulatoryConfigResponseParams?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/setregulatoryconfigwith%28_,completionhandler%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBasicCommissioningInfo(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRGeneralCommissioningClusterBasicCommissioningInfo?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributebasiccommissioninginfo%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBasicCommissioningInfo(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRGeneralCommissioningClusterBasicCommissioningInfo?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributebasiccommissioninginfo%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBreadcrumb(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributebreadcrumb%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBreadcrumb(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributebreadcrumb%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeLocationCapability(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributelocationcapability%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeLocationCapability(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributelocationcapability%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeRegulatoryConfig(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributeregulatoryconfig%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeRegulatoryConfig(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributeregulatoryconfig%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSupportsConcurrentConnection(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributesupportsconcurrentconnection%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSupportsConcurrentConnection(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/subscribeattributesupportsconcurrentconnection%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeBreadcrumb(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/writeattributebreadcrumb%28withvalue,completion%29.md)
- [func writeAttributeBreadcrumb(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/writeattributebreadcrumb%28withvalue,completionhandler%29.md)
- [func writeAttributeBreadcrumb(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/writeattributebreadcrumb%28withvalue,params,completion%29.md)
- [func writeAttributeBreadcrumb(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/writeattributebreadcrumb%28withvalue,params,completionhandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeBasicCommissioningInfo(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (MTRGeneralCommissioningClusterBasicCommissioningInfo?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributebasiccommissioninginfo%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeBasicCommissioningInfo(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRGeneralCommissioningClusterBasicCommissioningInfo?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributebasiccommissioninginfo%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeBreadcrumb(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributebreadcrumb%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeBreadcrumb(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributebreadcrumb%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeLocationCapability(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributelocationcapability%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeLocationCapability(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributelocationcapability%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeRegulatoryConfig(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributeregulatoryconfig%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeRegulatoryConfig(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributeregulatoryconfig%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSupportsConcurrentConnection(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributesupportsconcurrentconnection%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeSupportsConcurrentConnection(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneralcommissioning/readattributesupportsconcurrentconnection%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustergeneralcommissioning)*