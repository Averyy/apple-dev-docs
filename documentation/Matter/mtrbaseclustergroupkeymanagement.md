# MTRBaseClusterGroupKeyManagement

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
class MTRBaseClusterGroupKeyManagement
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclustergroupkeymanagement/init(device:endpoint:queue:).md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclustergroupkeymanagement/init(device:endpointid:queue:).md)
### Instance Methods
- [func keySetRead(with: MTRGroupKeyManagementClusterKeySetReadParams, completion: (MTRGroupKeyManagementClusterKeySetReadResponseParams?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/keysetread(with:completion:).md)
- [func keySetRead(with: MTRGroupKeyManagementClusterKeySetReadParams, completionHandler: (MTRGroupKeyManagementClusterKeySetReadResponseParams?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/keysetread(with:completionhandler:).md)
- [func keySetReadAllIndices(completion: (MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/keysetreadallindices(completion:).md)
- [func keySetReadAllIndices(with: MTRGroupKeyManagementClusterKeySetReadAllIndicesParams?, completion: (MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/keysetreadallindices(with:completion:).md)
- [func keySetReadAllIndices(with: MTRGroupKeyManagementClusterKeySetReadAllIndicesParams?, completionHandler: (MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/keysetreadallindices(with:completionhandler:).md)
- [func keySetRemove(with: MTRGroupKeyManagementClusterKeySetRemoveParams, completion: ((any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/keysetremove(with:completion:).md)
- [func keySetRemove(with: MTRGroupKeyManagementClusterKeySetRemoveParams, completionHandler: ((any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/keysetremove(with:completionhandler:).md)
- [func keySetWrite(with: MTRGroupKeyManagementClusterKeySetWriteParams, completion: ((any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/keysetwrite(with:completion:).md)
- [func keySetWrite(with: MTRGroupKeyManagementClusterKeySetWriteParams, completionHandler: ((any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/keysetwrite(with:completionhandler:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributeattributelist(completion:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributeattributelist(completionhandler:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributeclusterrevision(completion:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributefeaturemap(completion:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributefeaturemap(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributegeneratedcommandlist(completionhandler:).md)
- [func readAttributeGroupKeyMap(with: MTRReadParams?, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributegroupkeymap(with:completion:).md)
- [func readAttributeGroupKeyMap(with: MTRReadParams?, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributegroupkeymap(with:completionhandler:).md)
- [func readAttributeGroupTable(with: MTRReadParams?, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributegrouptable(with:completion:).md)
- [func readAttributeGroupTable(with: MTRReadParams?, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributegrouptable(with:completionhandler:).md)
- [func readAttributeMaxGroupKeysPerFabric(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributemaxgroupkeysperfabric(completion:).md)
- [func readAttributeMaxGroupKeysPerFabric(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributemaxgroupkeysperfabric(completionhandler:).md)
- [func readAttributeMaxGroupsPerFabric(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributemaxgroupsperfabric(completion:).md)
- [func readAttributeMaxGroupsPerFabric(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributemaxgroupsperfabric(completionhandler:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGroupKeyMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/subscribeattributegroupkeymap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGroupKeyMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/subscribeattributegroupkeymap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGroupTable(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/subscribeattributegrouptable(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGroupTable(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/subscribeattributegrouptable(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMaxGroupKeysPerFabric(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/subscribeattributemaxgroupkeysperfabric(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMaxGroupKeysPerFabric(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/subscribeattributemaxgroupkeysperfabric(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMaxGroupsPerFabric(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/subscribeattributemaxgroupsperfabric(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMaxGroupsPerFabric(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/subscribeattributemaxgroupsperfabric(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func writeAttributeGroupKeyMap(withValue: [Any], completion: ((any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/writeattributegroupkeymap(withvalue:completion:).md)
- [func writeAttributeGroupKeyMap(withValue: [Any], completionHandler: ((any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/writeattributegroupkeymap(withvalue:completionhandler:).md)
- [func writeAttributeGroupKeyMap(withValue: [Any], params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/writeattributegroupkeymap(withvalue:params:completion:).md)
- [func writeAttributeGroupKeyMap(withValue: [Any], params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/writeattributegroupkeymap(withvalue:params:completionhandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGroupKeyMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributegroupkeymap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGroupKeyMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributegroupkeymap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGroupTable(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributegrouptable(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGroupTable(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributegrouptable(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMaxGroupKeysPerFabric(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributemaxgroupkeysperfabric(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeMaxGroupKeysPerFabric(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributemaxgroupkeysperfabric(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMaxGroupsPerFabric(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributemaxgroupsperfabric(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeMaxGroupsPerFabric(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergroupkeymanagement/readattributemaxgroupsperfabric(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustergroupkeymanagement)*