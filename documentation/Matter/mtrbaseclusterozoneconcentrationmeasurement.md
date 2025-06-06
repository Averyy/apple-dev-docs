# MTRBaseClusterOzoneConcentrationMeasurement

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
class MTRBaseClusterOzoneConcentrationMeasurement
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterozoneconcentrationmeasurement/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributeattributelist(completion:).md)
- [func readAttributeAverageMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributeaveragemeasuredvalue(completion:).md)
- [func readAttributeAverageMeasuredValueWindow(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributeaveragemeasuredvaluewindow(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributeclusterrevision(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeLevelValue(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributelevelvalue(completion:).md)
- [func readAttributeMaxMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributemaxmeasuredvalue(completion:).md)
- [func readAttributeMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributemeasuredvalue(completion:).md)
- [func readAttributeMeasurementMedium(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributemeasurementmedium(completion:).md)
- [func readAttributeMeasurementUnit(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributemeasurementunit(completion:).md)
- [func readAttributeMinMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributeminmeasuredvalue(completion:).md)
- [func readAttributePeakMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributepeakmeasuredvalue(completion:).md)
- [func readAttributePeakMeasuredValueWindow(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributepeakmeasuredvaluewindow(completion:).md)
- [func readAttributeUncertainty(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributeuncertainty(completion:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAverageMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/subscribeattributeaveragemeasuredvalue(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAverageMeasuredValueWindow(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/subscribeattributeaveragemeasuredvaluewindow(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLevelValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/subscribeattributelevelvalue(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMaxMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/subscribeattributemaxmeasuredvalue(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/subscribeattributemeasuredvalue(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMeasurementMedium(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/subscribeattributemeasurementmedium(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMeasurementUnit(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/subscribeattributemeasurementunit(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMinMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/subscribeattributeminmeasuredvalue(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePeakMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/subscribeattributepeakmeasuredvalue(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePeakMeasuredValueWindow(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/subscribeattributepeakmeasuredvaluewindow(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeUncertainty(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/subscribeattributeuncertainty(with:subscriptionestablished:reporthandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAverageMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributeaveragemeasuredvalue(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAverageMeasuredValueWindow(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributeaveragemeasuredvaluewindow(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeLevelValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributelevelvalue(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMaxMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributemaxmeasuredvalue(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributemeasuredvalue(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMeasurementMedium(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributemeasurementmedium(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMeasurementUnit(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributemeasurementunit(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMinMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributeminmeasuredvalue(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePeakMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributepeakmeasuredvalue(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePeakMeasuredValueWindow(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributepeakmeasuredvaluewindow(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeUncertainty(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterozoneconcentrationmeasurement/readattributeuncertainty(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterozoneconcentrationmeasurement)*