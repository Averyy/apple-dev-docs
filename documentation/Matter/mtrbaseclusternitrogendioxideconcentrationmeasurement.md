# MTRBaseClusterNitrogenDioxideConcentrationMeasurement

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
class MTRBaseClusterNitrogenDioxideConcentrationMeasurement
```

```objc
@interface MTRBaseClusterNitrogenDioxideConcentrationMeasurement : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributeattributelist%28completion%29.md)
- [func readAttributeAverageMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributeaveragemeasuredvalue%28completion%29.md)
- [func readAttributeAverageMeasuredValueWindow(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributeaveragemeasuredvaluewindow%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributeclusterrevision%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeLevelValue(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributelevelvalue%28completion%29.md)
- [func readAttributeMaxMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributemaxmeasuredvalue%28completion%29.md)
- [func readAttributeMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributemeasuredvalue%28completion%29.md)
- [func readAttributeMeasurementMedium(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributemeasurementmedium%28completion%29.md)
- [func readAttributeMeasurementUnit(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributemeasurementunit%28completion%29.md)
- [func readAttributeMinMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributeminmeasuredvalue%28completion%29.md)
- [func readAttributePeakMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributepeakmeasuredvalue%28completion%29.md)
- [func readAttributePeakMeasuredValueWindow(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributepeakmeasuredvaluewindow%28completion%29.md)
- [func readAttributeUncertainty(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributeuncertainty%28completion%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAverageMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/subscribeattributeaveragemeasuredvalue%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAverageMeasuredValueWindow(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/subscribeattributeaveragemeasuredvaluewindow%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeLevelValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/subscribeattributelevelvalue%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMaxMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/subscribeattributemaxmeasuredvalue%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/subscribeattributemeasuredvalue%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMeasurementMedium(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/subscribeattributemeasurementmedium%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMeasurementUnit(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/subscribeattributemeasurementunit%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMinMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/subscribeattributeminmeasuredvalue%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePeakMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/subscribeattributepeakmeasuredvalue%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePeakMeasuredValueWindow(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/subscribeattributepeakmeasuredvaluewindow%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeUncertainty(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/subscribeattributeuncertainty%28with,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAverageMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributeaveragemeasuredvalue%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAverageMeasuredValueWindow(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributeaveragemeasuredvaluewindow%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeLevelValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributelevelvalue%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMaxMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributemaxmeasuredvalue%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributemeasuredvalue%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMeasurementMedium(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributemeasurementmedium%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMeasurementUnit(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributemeasurementunit%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMinMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributeminmeasuredvalue%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePeakMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributepeakmeasuredvalue%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePeakMeasuredValueWindow(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributepeakmeasuredvaluewindow%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeUncertainty(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternitrogendioxideconcentrationmeasurement/readattributeuncertainty%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusternitrogendioxideconcentrationmeasurement)*