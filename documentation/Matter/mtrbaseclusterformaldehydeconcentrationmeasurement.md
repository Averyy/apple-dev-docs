# MTRBaseClusterFormaldehydeConcentrationMeasurement

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
class MTRBaseClusterFormaldehydeConcentrationMeasurement
```

```objc
@interface MTRBaseClusterFormaldehydeConcentrationMeasurement : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterformaldehydeconcentrationmeasurement/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributeattributelist%28completion%29.md)
- [func readAttributeAverageMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributeaveragemeasuredvalue%28completion%29.md)
- [func readAttributeAverageMeasuredValueWindow(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributeaveragemeasuredvaluewindow%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributeclusterrevision%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeLevelValue(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributelevelvalue%28completion%29.md)
- [func readAttributeMaxMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributemaxmeasuredvalue%28completion%29.md)
- [func readAttributeMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributemeasuredvalue%28completion%29.md)
- [func readAttributeMeasurementMedium(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributemeasurementmedium%28completion%29.md)
- [func readAttributeMeasurementUnit(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributemeasurementunit%28completion%29.md)
- [func readAttributeMinMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributeminmeasuredvalue%28completion%29.md)
- [func readAttributePeakMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributepeakmeasuredvalue%28completion%29.md)
- [func readAttributePeakMeasuredValueWindow(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributepeakmeasuredvaluewindow%28completion%29.md)
- [func readAttributeUncertainty(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributeuncertainty%28completion%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAverageMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/subscribeattributeaveragemeasuredvalue%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAverageMeasuredValueWindow(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/subscribeattributeaveragemeasuredvaluewindow%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeLevelValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/subscribeattributelevelvalue%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMaxMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/subscribeattributemaxmeasuredvalue%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/subscribeattributemeasuredvalue%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMeasurementMedium(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/subscribeattributemeasurementmedium%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMeasurementUnit(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/subscribeattributemeasurementunit%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMinMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/subscribeattributeminmeasuredvalue%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePeakMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/subscribeattributepeakmeasuredvalue%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePeakMeasuredValueWindow(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/subscribeattributepeakmeasuredvaluewindow%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeUncertainty(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/subscribeattributeuncertainty%28with,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAverageMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributeaveragemeasuredvalue%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAverageMeasuredValueWindow(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributeaveragemeasuredvaluewindow%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeLevelValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributelevelvalue%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMaxMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributemaxmeasuredvalue%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributemeasuredvalue%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMeasurementMedium(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributemeasurementmedium%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMeasurementUnit(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributemeasurementunit%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMinMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributeminmeasuredvalue%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePeakMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributepeakmeasuredvalue%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePeakMeasuredValueWindow(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributepeakmeasuredvaluewindow%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeUncertainty(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterformaldehydeconcentrationmeasurement/readattributeuncertainty%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterformaldehydeconcentrationmeasurement)*