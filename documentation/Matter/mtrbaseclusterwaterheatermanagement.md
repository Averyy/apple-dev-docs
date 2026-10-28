# MTRBaseClusterWaterHeaterManagement

**Framework**: Matter  
**Kind**: class  
**Role**: Class

Cluster Water Heater Management

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
class MTRBaseClusterWaterHeaterManagement
```

```objc
@interface MTRBaseClusterWaterHeaterManagement : MTRGenericBaseCluster
```

## Overview

This cluster is used to allow clients to control the operation of a hot water heating appliance so that it can be used with energy management.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterwaterheatermanagement/init%28device,endpointid,queue%29.md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func boost(with: MTRWaterHeaterManagementClusterBoostParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/boost%28with,completion%29.md)
  Command Boost
- [func cancelBoost(completion: ((any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/cancelboost%28completion%29.md)
- [func cancelBoost(with: MTRWaterHeaterManagementClusterCancelBoostParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/cancelboost%28with,completion%29.md)
  Command CancelBoost
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributeattributelist%28completion%29.md)
- [func readAttributeBoostState(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributebooststate%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributeclusterrevision%28completion%29.md)
- [func readAttributeEstimatedHeatRequired(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributeestimatedheatrequired%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeHeatDemand(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributeheatdemand%28completion%29.md)
- [func readAttributeHeaterTypes(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributeheatertypes%28completion%29.md)
- [func readAttributeTankPercentage(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributetankpercentage%28completion%29.md)
- [func readAttributeTankVolume(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributetankvolume%28completion%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBoostState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/subscribeattributebooststate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeEstimatedHeatRequired(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/subscribeattributeestimatedheatrequired%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeHeatDemand(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/subscribeattributeheatdemand%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeHeaterTypes(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/subscribeattributeheatertypes%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTankPercentage(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/subscribeattributetankpercentage%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTankVolume(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/subscribeattributetankvolume%28with,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeBoostState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributebooststate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeEstimatedHeatRequired(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributeestimatedheatrequired%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeHeatDemand(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributeheatdemand%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeHeaterTypes(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributeheatertypes%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeTankPercentage(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributetankpercentage%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeTankVolume(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwaterheatermanagement/readattributetankvolume%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterwaterheatermanagement)*