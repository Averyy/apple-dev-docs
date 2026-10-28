# MTRBaseClusterPowerTopology

**Framework**: Matter  
**Kind**: class  
**Role**: Class

Cluster Power Topology

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
class MTRBaseClusterPowerTopology
```

```objc
@interface MTRBaseClusterPowerTopology : MTRGenericBaseCluster
```

## Overview

The Power Topology Cluster provides a mechanism for expressing how power is flowing between endpoints.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterpowertopology/init%28device,endpointid,queue%29.md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeActiveEndpoints(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/readattributeactiveendpoints%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/readattributeattributelist%28completion%29.md)
- [func readAttributeAvailableEndpoints(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/readattributeavailableendpoints%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/readattributeclusterrevision%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/readattributegeneratedcommandlist%28completion%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeActiveEndpoints(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/subscribeattributeactiveendpoints%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAvailableEndpoints(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/subscribeattributeavailableendpoints%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeActiveEndpoints(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/readattributeactiveendpoints%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAvailableEndpoints(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/readattributeavailableendpoints%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterpowertopology/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterpowertopology)*