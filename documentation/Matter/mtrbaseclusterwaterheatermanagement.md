# MTRBaseClusterWaterHeaterManagement

**Framework**: Matter  
**Kind**: class

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

#### Overview

This cluster is used to allow clients to control the operation of a hot water heating appliance so that it can be used with energy management.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterwaterheatermanagement/init(device:endpointid:queue:).md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func boost(with: MTRWaterHeaterManagementClusterBoostParams, completion: ((any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/boost(with:completion:).md)
  Command Boost
- [func cancelBoost(completion: ((any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/cancelboost(completion:).md)
- [func cancelBoost(with: MTRWaterHeaterManagementClusterCancelBoostParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/cancelboost(with:completion:).md)
  Command CancelBoost
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributeattributelist(completion:).md)
- [func readAttributeBoostState(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributebooststate(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributeclusterrevision(completion:).md)
- [func readAttributeEstimatedHeatRequired(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributeestimatedheatrequired(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeHeatDemand(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributeheatdemand(completion:).md)
- [func readAttributeHeaterTypes(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributeheatertypes(completion:).md)
- [func readAttributeTankPercentage(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributetankpercentage(completion:).md)
- [func readAttributeTankVolume(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributetankvolume(completion:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBoostState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/subscribeattributebooststate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeEstimatedHeatRequired(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/subscribeattributeestimatedheatrequired(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeHeatDemand(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/subscribeattributeheatdemand(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeHeaterTypes(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/subscribeattributeheatertypes(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTankPercentage(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/subscribeattributetankpercentage(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTankVolume(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/subscribeattributetankvolume(with:subscriptionestablished:reporthandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeBoostState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributebooststate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeEstimatedHeatRequired(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributeestimatedheatrequired(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeHeatDemand(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributeheatdemand(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeHeaterTypes(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributeheatertypes(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeTankPercentage(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributetankpercentage(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeTankVolume(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterwaterheatermanagement/readattributetankvolume(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterwaterheatermanagement)*