# MTRBaseClusterHEPAFilterMonitoring

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRBaseClusterHEPAFilterMonitoring : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterhepafiltermonitoring/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributeattributelist%28completion%29.md)
- [func readAttributeChangeIndication(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributechangeindication%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributeclusterrevision%28completion%29.md)
- [func readAttributeCondition(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributecondition%28completion%29.md)
- [func readAttributeDegradationDirection(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributedegradationdirection%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeInPlaceIndicator(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributeinplaceindicator%28completion%29.md)
- [func readAttributeLastChangedTime(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributelastchangedtime%28completion%29.md)
- [func readAttributeReplacementProductList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributereplacementproductlist%28completion%29.md)
- [func resetCondition(completion: ((any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/resetcondition%28completion%29.md)
- [func resetCondition(with: MTRHEPAFilterMonitoringClusterResetConditionParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/resetcondition%28with,completion%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeChangeIndication(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/subscribeattributechangeindication%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCondition(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/subscribeattributecondition%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeDegradationDirection(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/subscribeattributedegradationdirection%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeInPlaceIndicator(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/subscribeattributeinplaceindicator%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeLastChangedTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/subscribeattributelastchangedtime%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeReplacementProductList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/subscribeattributereplacementproductlist%28with,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeLastChangedTime(withValue: NSNumber?, completion: ((any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/writeattributelastchangedtime%28withvalue,completion%29.md)
- [func writeAttributeLastChangedTime(withValue: NSNumber?, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/writeattributelastchangedtime%28withvalue,params,completion%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeChangeIndication(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributechangeindication%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCondition(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributecondition%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeDegradationDirection(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributedegradationdirection%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeInPlaceIndicator(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributeinplaceindicator%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeLastChangedTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributelastchangedtime%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeReplacementProductList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterhepafiltermonitoring/readattributereplacementproductlist%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterhepafiltermonitoring)*