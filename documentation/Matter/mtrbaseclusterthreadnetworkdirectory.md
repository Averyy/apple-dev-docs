# MTRBaseClusterThreadNetworkDirectory

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRBaseClusterThreadNetworkDirectory : MTRGenericBaseCluster
```

## Overview

Manages the names and credentials of Thread networks visible to the user.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterthreadnetworkdirectory/init%28device,endpointid,queue%29.md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func addNetwork(with: MTRThreadNetworkDirectoryClusterAddNetworkParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/addnetwork%28with,completion%29.md)
  Command AddNetwork
- [func getOperationalDataset(with: MTRThreadNetworkDirectoryClusterGetOperationalDatasetParams, completion: (MTRThreadNetworkDirectoryClusterOperationalDatasetResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/getoperationaldataset%28with,completion%29.md)
  Command GetOperationalDataset
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/readattributeattributelist%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/readattributeclusterrevision%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributePreferredExtendedPanID(completion: (Data?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/readattributepreferredextendedpanid%28completion%29.md)
- [func readAttributeThreadNetworkTableSize(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/readattributethreadnetworktablesize%28completion%29.md)
- [func readAttributeThreadNetworks(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/readattributethreadnetworks%28completion%29.md)
- [func removeNetwork(with: MTRThreadNetworkDirectoryClusterRemoveNetworkParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/removenetwork%28with,completion%29.md)
  Command RemoveNetwork
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePreferredExtendedPanID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (Data?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/subscribeattributepreferredextendedpanid%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeThreadNetworkTableSize(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/subscribeattributethreadnetworktablesize%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeThreadNetworks(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/subscribeattributethreadnetworks%28with,subscriptionestablished,reporthandler%29.md)
- [func writeAttributePreferredExtendedPanID(withValue: Data?, completion: ((any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/writeattributepreferredextendedpanid%28withvalue,completion%29.md)
- [func writeAttributePreferredExtendedPanID(withValue: Data?, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/writeattributepreferredextendedpanid%28withvalue,params,completion%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePreferredExtendedPanID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (Data?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/readattributepreferredextendedpanid%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeThreadNetworkTableSize(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/readattributethreadnetworktablesize%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeThreadNetworks(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadnetworkdirectory/readattributethreadnetworks%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterthreadnetworkdirectory)*