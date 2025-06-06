# MTRBaseClusterThreadNetworkDirectory

**Framework**: Matter  
**Kind**: class

Cluster Thread Network Directory

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
class MTRBaseClusterThreadNetworkDirectory
```

#### Overview

Manages the names and credentials of Thread networks visible to the user.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterthreadnetworkdirectory/init(device:endpointid:queue:).md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func addNetwork(with: MTRThreadNetworkDirectoryClusterAddNetworkParams, completion: MTRStatusCompletion)](mtrbaseclusterthreadnetworkdirectory/addnetwork(with:completion:).md)
  Command AddNetwork
- [func getOperationalDataset(with: MTRThreadNetworkDirectoryClusterGetOperationalDatasetParams, completion: (MTRThreadNetworkDirectoryClusterOperationalDatasetResponseParams?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/getoperationaldataset(with:completion:).md)
  Command GetOperationalDataset
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/readattributeattributelist(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/readattributeclusterrevision(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/readattributegeneratedcommandlist(completion:).md)
- [func readAttributePreferredExtendedPanID(completion: (Data?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/readattributepreferredextendedpanid(completion:).md)
- [func readAttributeThreadNetworkTableSize(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/readattributethreadnetworktablesize(completion:).md)
- [func readAttributeThreadNetworks(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/readattributethreadnetworks(completion:).md)
- [func removeNetwork(with: MTRThreadNetworkDirectoryClusterRemoveNetworkParams, completion: MTRStatusCompletion)](mtrbaseclusterthreadnetworkdirectory/removenetwork(with:completion:).md)
  Command RemoveNetwork
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePreferredExtendedPanID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (Data?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/subscribeattributepreferredextendedpanid(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeThreadNetworkTableSize(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/subscribeattributethreadnetworktablesize(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeThreadNetworks(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/subscribeattributethreadnetworks(with:subscriptionestablished:reporthandler:).md)
- [func writeAttributePreferredExtendedPanID(withValue: Data?, completion: MTRStatusCompletion)](mtrbaseclusterthreadnetworkdirectory/writeattributepreferredextendedpanid(withvalue:completion:).md)
- [func writeAttributePreferredExtendedPanID(withValue: Data?, params: MTRWriteParams?, completion: MTRStatusCompletion)](mtrbaseclusterthreadnetworkdirectory/writeattributepreferredextendedpanid(withvalue:params:completion:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePreferredExtendedPanID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (Data?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/readattributepreferredextendedpanid(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeThreadNetworkTableSize(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/readattributethreadnetworktablesize(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeThreadNetworks(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadnetworkdirectory/readattributethreadnetworks(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterthreadnetworkdirectory)*