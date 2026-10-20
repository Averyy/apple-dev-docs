# MTRBaseClusterServiceArea

**Framework**: Matter  
**Kind**: class  
**Role**: Class

Cluster Service Area

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
class MTRBaseClusterServiceArea
```

```objc
@interface MTRBaseClusterServiceArea : MTRGenericBaseCluster
```

#### Overview

The Service Area cluster provides an interface for controlling the areas where a device should operate, and for querying the current area being serviced.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterservicearea/init%28device,endpointid,queue%29.md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributeattributelist%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributeclusterrevision%28completion%29.md)
- [func readAttributeCurrentArea(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributecurrentarea%28completion%29.md)
- [func readAttributeEstimatedEndTime(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributeestimatedendtime%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeProgress(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributeprogress%28completion%29.md)
- [func readAttributeSelectedAreas(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributeselectedareas%28completion%29.md)
- [func readAttributeSupportedAreas(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributesupportedareas%28completion%29.md)
- [func readAttributeSupportedMaps(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributesupportedmaps%28completion%29.md)
- [func selectAreas(with: MTRServiceAreaClusterSelectAreasParams, completion: (MTRServiceAreaClusterSelectAreasResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/selectareas%28with,completion%29.md)
  Command SelectAreas
- [func skip(with: MTRServiceAreaClusterSkipAreaParams, completion: (MTRServiceAreaClusterSkipAreaResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/skip%28with,completion%29.md)
  Command SkipArea
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCurrentArea(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/subscribeattributecurrentarea%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeEstimatedEndTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/subscribeattributeestimatedendtime%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeProgress(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/subscribeattributeprogress%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSelectedAreas(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/subscribeattributeselectedareas%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSupportedAreas(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/subscribeattributesupportedareas%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSupportedMaps(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/subscribeattributesupportedmaps%28with,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCurrentArea(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributecurrentarea%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeEstimatedEndTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributeestimatedendtime%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeProgress(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributeprogress%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSelectedAreas(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributeselectedareas%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSupportedAreas(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributesupportedareas%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSupportedMaps(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterservicearea/readattributesupportedmaps%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterservicearea)*