# MTRBaseClusterHEPAFilterMonitoring

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
class MTRBaseClusterHEPAFilterMonitoring
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterhepafiltermonitoring/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributeattributelist(completion:).md)
- [func readAttributeChangeIndication(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributechangeindication(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributeclusterrevision(completion:).md)
- [func readAttributeCondition(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributecondition(completion:).md)
- [func readAttributeDegradationDirection(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributedegradationdirection(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeInPlaceIndicator(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributeinplaceindicator(completion:).md)
- [func readAttributeLastChangedTime(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributelastchangedtime(completion:).md)
- [func readAttributeReplacementProductList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributereplacementproductlist(completion:).md)
- [func resetCondition(completion: MTRStatusCompletion)](mtrbaseclusterhepafiltermonitoring/resetcondition(completion:).md)
- [func resetCondition(with: MTRHEPAFilterMonitoringClusterResetConditionParams?, completion: MTRStatusCompletion)](mtrbaseclusterhepafiltermonitoring/resetcondition(with:completion:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeChangeIndication(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/subscribeattributechangeindication(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCondition(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/subscribeattributecondition(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeDegradationDirection(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/subscribeattributedegradationdirection(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeInPlaceIndicator(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/subscribeattributeinplaceindicator(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLastChangedTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/subscribeattributelastchangedtime(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeReplacementProductList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/subscribeattributereplacementproductlist(with:subscriptionestablished:reporthandler:).md)
- [func writeAttributeLastChangedTime(withValue: NSNumber?, completion: MTRStatusCompletion)](mtrbaseclusterhepafiltermonitoring/writeattributelastchangedtime(withvalue:completion:).md)
- [func writeAttributeLastChangedTime(withValue: NSNumber?, params: MTRWriteParams?, completion: MTRStatusCompletion)](mtrbaseclusterhepafiltermonitoring/writeattributelastchangedtime(withvalue:params:completion:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeChangeIndication(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributechangeindication(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCondition(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributecondition(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeDegradationDirection(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributedegradationdirection(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeInPlaceIndicator(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributeinplaceindicator(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeLastChangedTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributelastchangedtime(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeReplacementProductList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterhepafiltermonitoring/readattributereplacementproductlist(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterhepafiltermonitoring)*