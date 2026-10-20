# MTRBaseClusterAccessControl

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
class MTRBaseClusterAccessControl
```

```objc
@interface MTRBaseClusterAccessControl : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclusteraccesscontrol/init%28device,endpoint,queue%29.md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusteraccesscontrol/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeACL(with: MTRReadParams?, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeacl%28with,completion%29.md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeAccessControlEntriesPerFabric(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeaccesscontrolentriesperfabric%28completion%29.md)
- [func readAttributeAccessControlEntriesPerFabric(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeaccesscontrolentriesperfabric%28completionhandler%29.md)
- [func readAttributeAcl(with: MTRReadParams?, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeacl%28with,completionhandler%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeattributelist%28completion%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeclusterrevision%28completion%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeExtension(with: MTRReadParams?, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeextension%28with,completion%29.md)
- [func readAttributeExtension(with: MTRReadParams?, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeextension%28with,completionhandler%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributefeaturemap%28completion%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func readAttributeSubjectsPerAccessControlEntry(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributesubjectsperaccesscontrolentry%28completion%29.md)
- [func readAttributeSubjectsPerAccessControlEntry(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributesubjectsperaccesscontrolentry%28completionhandler%29.md)
- [func readAttributeTargetsPerAccessControlEntry(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributetargetsperaccesscontrolentry%28completion%29.md)
- [func readAttributeTargetsPerAccessControlEntry(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributetargetsperaccesscontrolentry%28completionhandler%29.md)
- [func subscribeAttributeACL(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributeacl%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAccessControlEntriesPerFabric(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributeaccesscontrolentriesperfabric%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAccessControlEntriesPerFabric(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributeaccesscontrolentriesperfabric%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcl(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributeacl%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeExtension(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributeextension%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeExtension(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributeextension%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSubjectsPerAccessControlEntry(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributesubjectsperaccesscontrolentry%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSubjectsPerAccessControlEntry(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributesubjectsperaccesscontrolentry%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTargetsPerAccessControlEntry(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributetargetsperaccesscontrolentry%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTargetsPerAccessControlEntry(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributetargetsperaccesscontrolentry%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeACL(withValue: [Any], completion: ((any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/writeattributeacl%28withvalue,completion%29.md)
- [func writeAttributeACL(withValue: [Any], params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/writeattributeacl%28withvalue,params,completion%29.md)
- [func writeAttributeAcl(withValue: [Any], completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/writeattributeacl%28withvalue,completionhandler%29.md)
- [func writeAttributeAcl(withValue: [Any], params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/writeattributeacl%28withvalue,params,completionhandler%29.md)
- [func writeAttributeExtension(withValue: [Any], completion: ((any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/writeattributeextension%28withvalue,completion%29.md)
- [func writeAttributeExtension(withValue: [Any], completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/writeattributeextension%28withvalue,completionhandler%29.md)
- [func writeAttributeExtension(withValue: [Any], params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/writeattributeextension%28withvalue,params,completion%29.md)
- [func writeAttributeExtension(withValue: [Any], params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/writeattributeextension%28withvalue,params,completionhandler%29.md)
- [func readAttributeARL(with: MTRReadParams?, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributearl%28with,completion%29.md)
- [func readAttributeCommissioningARL(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributecommissioningarl%28completion%29.md)
- [func reviewFabricRestrictions(with: MTRAccessControlClusterReviewFabricRestrictionsParams, completion: (MTRAccessControlClusterReviewFabricRestrictionsResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/reviewfabricrestrictions%28with,completion%29.md)
  Command ReviewFabricRestrictions
- [func subscribeAttributeARL(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributearl%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCommissioningARL(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/subscribeattributecommissioningarl%28with,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeACL(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeacl%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAccessControlEntriesPerFabric(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeaccesscontrolentriesperfabric%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAccessControlEntriesPerFabric(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeaccesscontrolentriesperfabric%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAcl(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeacl%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeExtension(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeextension%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeExtension(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributeextension%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSubjectsPerAccessControlEntry(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributesubjectsperaccesscontrolentry%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeSubjectsPerAccessControlEntry(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributesubjectsperaccesscontrolentry%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeTargetsPerAccessControlEntry(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributetargetsperaccesscontrolentry%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeTargetsPerAccessControlEntry(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributetargetsperaccesscontrolentry%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeARL(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributearl%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCommissioningARL(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteraccesscontrol/readattributecommissioningarl%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteraccesscontrol)*