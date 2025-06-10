# MTRBaseClusterActivatedCarbonFilterMonitoring

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
class MTRBaseClusterActivatedCarbonFilterMonitoring
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusteractivatedcarbonfiltermonitoring/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributeattributelist(completion:).md)
- [func readAttributeChangeIndication(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributechangeindication(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributeclusterrevision(completion:).md)
- [func readAttributeCondition(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributecondition(completion:).md)
- [func readAttributeDegradationDirection(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributedegradationdirection(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeInPlaceIndicator(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributeinplaceindicator(completion:).md)
- [func readAttributeLastChangedTime(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributelastchangedtime(completion:).md)
- [func readAttributeReplacementProductList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributereplacementproductlist(completion:).md)
- [func resetCondition(completion: ((any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/resetcondition(completion:).md)
- [func resetCondition(with: MTRActivatedCarbonFilterMonitoringClusterResetConditionParams?, completion: ((any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/resetcondition(with:completion:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeChangeIndication(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/subscribeattributechangeindication(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCondition(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/subscribeattributecondition(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeDegradationDirection(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/subscribeattributedegradationdirection(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeInPlaceIndicator(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/subscribeattributeinplaceindicator(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLastChangedTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/subscribeattributelastchangedtime(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeReplacementProductList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/subscribeattributereplacementproductlist(with:subscriptionestablished:reporthandler:).md)
- [func writeAttributeLastChangedTime(withValue: NSNumber?, completion: ((any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/writeattributelastchangedtime(withvalue:completion:).md)
- [func writeAttributeLastChangedTime(withValue: NSNumber?, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/writeattributelastchangedtime(withvalue:params:completion:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeChangeIndication(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributechangeindication(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCondition(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributecondition(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeDegradationDirection(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributedegradationdirection(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeInPlaceIndicator(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributeinplaceindicator(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeLastChangedTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributelastchangedtime(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeReplacementProductList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteractivatedcarbonfiltermonitoring/readattributereplacementproductlist(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteractivatedcarbonfiltermonitoring)*