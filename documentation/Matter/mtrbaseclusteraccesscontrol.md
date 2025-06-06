# MTRBaseClusterAccessControl

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
class MTRBaseClusterAccessControl
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclusteraccesscontrol/init(device:endpoint:queue:).md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusteraccesscontrol/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeACL(with: MTRReadParams?, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeacl(with:completion:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeAccessControlEntriesPerFabric(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeaccesscontrolentriesperfabric(completion:).md)
- [func readAttributeAccessControlEntriesPerFabric(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeaccesscontrolentriesperfabric(completionhandler:).md)
- [func readAttributeAcl(with: MTRReadParams?, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeacl(with:completionhandler:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeattributelist(completion:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeattributelist(completionhandler:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeclusterrevision(completion:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeExtension(with: MTRReadParams?, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeextension(with:completion:).md)
- [func readAttributeExtension(with: MTRReadParams?, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeextension(with:completionhandler:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributefeaturemap(completion:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributefeaturemap(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributegeneratedcommandlist(completionhandler:).md)
- [func readAttributeSubjectsPerAccessControlEntry(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributesubjectsperaccesscontrolentry(completion:).md)
- [func readAttributeSubjectsPerAccessControlEntry(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributesubjectsperaccesscontrolentry(completionhandler:).md)
- [func readAttributeTargetsPerAccessControlEntry(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributetargetsperaccesscontrolentry(completion:).md)
- [func readAttributeTargetsPerAccessControlEntry(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributetargetsperaccesscontrolentry(completionhandler:).md)
- [func subscribeAttributeACL(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributeacl(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAccessControlEntriesPerFabric(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributeaccesscontrolentriesperfabric(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAccessControlEntriesPerFabric(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributeaccesscontrolentriesperfabric(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcl(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributeacl(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeExtension(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributeextension(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeExtension(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributeextension(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSubjectsPerAccessControlEntry(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributesubjectsperaccesscontrolentry(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSubjectsPerAccessControlEntry(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributesubjectsperaccesscontrolentry(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTargetsPerAccessControlEntry(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributetargetsperaccesscontrolentry(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTargetsPerAccessControlEntry(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributetargetsperaccesscontrolentry(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func writeAttributeACL(withValue: [Any], completion: MTRStatusCompletion)](mtrbaseclusteraccesscontrol/writeattributeacl(withvalue:completion:).md)
- [func writeAttributeACL(withValue: [Any], params: MTRWriteParams?, completion: MTRStatusCompletion)](mtrbaseclusteraccesscontrol/writeattributeacl(withvalue:params:completion:).md)
- [func writeAttributeAcl(withValue: [Any], completionHandler: MTRStatusCompletion)](mtrbaseclusteraccesscontrol/writeattributeacl(withvalue:completionhandler:).md)
- [func writeAttributeAcl(withValue: [Any], params: MTRWriteParams?, completionHandler: MTRStatusCompletion)](mtrbaseclusteraccesscontrol/writeattributeacl(withvalue:params:completionhandler:).md)
- [func writeAttributeExtension(withValue: [Any], completion: MTRStatusCompletion)](mtrbaseclusteraccesscontrol/writeattributeextension(withvalue:completion:).md)
- [func writeAttributeExtension(withValue: [Any], completionHandler: MTRStatusCompletion)](mtrbaseclusteraccesscontrol/writeattributeextension(withvalue:completionhandler:).md)
- [func writeAttributeExtension(withValue: [Any], params: MTRWriteParams?, completion: MTRStatusCompletion)](mtrbaseclusteraccesscontrol/writeattributeextension(withvalue:params:completion:).md)
- [func writeAttributeExtension(withValue: [Any], params: MTRWriteParams?, completionHandler: MTRStatusCompletion)](mtrbaseclusteraccesscontrol/writeattributeextension(withvalue:params:completionhandler:).md)
- [func readAttributeARL(with: MTRReadParams?, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributearl(with:completion:).md)
- [func readAttributeCommissioningARL(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributecommissioningarl(completion:).md)
- [func reviewFabricRestrictions(with: MTRAccessControlClusterReviewFabricRestrictionsParams, completion: (MTRAccessControlClusterReviewFabricRestrictionsResponseParams?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/reviewfabricrestrictions(with:completion:).md)
  Command ReviewFabricRestrictions
- [func subscribeAttributeARL(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributearl(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCommissioningARL(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/subscribeattributecommissioningarl(with:subscriptionestablished:reporthandler:).md)
### Type Methods
- [class func readAttributeACL(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeacl(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAccessControlEntriesPerFabric(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeaccesscontrolentriesperfabric(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAccessControlEntriesPerFabric(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeaccesscontrolentriesperfabric(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAcl(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeacl(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeExtension(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeextension(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeExtension(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributeextension(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSubjectsPerAccessControlEntry(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributesubjectsperaccesscontrolentry(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeSubjectsPerAccessControlEntry(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributesubjectsperaccesscontrolentry(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeTargetsPerAccessControlEntry(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributetargetsperaccesscontrolentry(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeTargetsPerAccessControlEntry(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributetargetsperaccesscontrolentry(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeARL(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributearl(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCommissioningARL(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteraccesscontrol/readattributecommissioningarl(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteraccesscontrol)*