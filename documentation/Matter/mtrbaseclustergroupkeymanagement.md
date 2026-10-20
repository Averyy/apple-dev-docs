# MTRBaseClusterGroupKeyManagement

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
class MTRBaseClusterGroupKeyManagement
```

```objc
@interface MTRBaseClusterGroupKeyManagement : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclustergroupkeymanagement/init%28device,endpoint,queue%29.md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclustergroupkeymanagement/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func keySetRead(with: MTRGroupKeyManagementClusterKeySetReadParams, completion: (MTRGroupKeyManagementClusterKeySetReadResponseParams?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/keysetread%28with,completion%29.md)
- [func keySetRead(with: MTRGroupKeyManagementClusterKeySetReadParams, completionHandler: (MTRGroupKeyManagementClusterKeySetReadResponseParams?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/keysetread%28with,completionhandler%29.md)
- [func keySetReadAllIndices(completion: (MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/keysetreadallindices%28completion%29.md)
- [func keySetReadAllIndices(with: MTRGroupKeyManagementClusterKeySetReadAllIndicesParams?, completion: (MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/keysetreadallindices%28with,completion%29.md)
- [func keySetReadAllIndices(with: MTRGroupKeyManagementClusterKeySetReadAllIndicesParams?, completionHandler: (MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/keysetreadallindices%28with,completionhandler%29.md)
- [func keySetRemove(with: MTRGroupKeyManagementClusterKeySetRemoveParams, completion: ((any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/keysetremove%28with,completion%29.md)
- [func keySetRemove(with: MTRGroupKeyManagementClusterKeySetRemoveParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/keysetremove%28with,completionhandler%29.md)
- [func keySetWrite(with: MTRGroupKeyManagementClusterKeySetWriteParams, completion: ((any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/keysetwrite%28with,completion%29.md)
- [func keySetWrite(with: MTRGroupKeyManagementClusterKeySetWriteParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/keysetwrite%28with,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributeattributelist%28completion%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributeclusterrevision%28completion%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributefeaturemap%28completion%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func readAttributeGroupKeyMap(with: MTRReadParams?, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributegroupkeymap%28with,completion%29.md)
- [func readAttributeGroupKeyMap(with: MTRReadParams?, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributegroupkeymap%28with,completionhandler%29.md)
- [func readAttributeGroupTable(with: MTRReadParams?, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributegrouptable%28with,completion%29.md)
- [func readAttributeGroupTable(with: MTRReadParams?, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributegrouptable%28with,completionhandler%29.md)
- [func readAttributeMaxGroupKeysPerFabric(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributemaxgroupkeysperfabric%28completion%29.md)
- [func readAttributeMaxGroupKeysPerFabric(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributemaxgroupkeysperfabric%28completionhandler%29.md)
- [func readAttributeMaxGroupsPerFabric(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributemaxgroupsperfabric%28completion%29.md)
- [func readAttributeMaxGroupsPerFabric(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributemaxgroupsperfabric%28completionhandler%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGroupKeyMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/subscribeattributegroupkeymap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGroupKeyMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/subscribeattributegroupkeymap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGroupTable(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/subscribeattributegrouptable%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGroupTable(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/subscribeattributegrouptable%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMaxGroupKeysPerFabric(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/subscribeattributemaxgroupkeysperfabric%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMaxGroupKeysPerFabric(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/subscribeattributemaxgroupkeysperfabric%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMaxGroupsPerFabric(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/subscribeattributemaxgroupsperfabric%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMaxGroupsPerFabric(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/subscribeattributemaxgroupsperfabric%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeGroupKeyMap(withValue: [Any], completion: ((any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/writeattributegroupkeymap%28withvalue,completion%29.md)
- [func writeAttributeGroupKeyMap(withValue: [Any], completionHandler: ((any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/writeattributegroupkeymap%28withvalue,completionhandler%29.md)
- [func writeAttributeGroupKeyMap(withValue: [Any], params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/writeattributegroupkeymap%28withvalue,params,completion%29.md)
- [func writeAttributeGroupKeyMap(withValue: [Any], params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/writeattributegroupkeymap%28withvalue,params,completionhandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGroupKeyMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributegroupkeymap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGroupKeyMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributegroupkeymap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGroupTable(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributegrouptable%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGroupTable(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributegrouptable%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMaxGroupKeysPerFabric(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributemaxgroupkeysperfabric%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeMaxGroupKeysPerFabric(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributemaxgroupkeysperfabric%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMaxGroupsPerFabric(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributemaxgroupsperfabric%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeMaxGroupsPerFabric(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergroupkeymanagement/readattributemaxgroupsperfabric%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustergroupkeymanagement)*