# MTRBaseClusterCarbonDioxideConcentrationMeasurement

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
class MTRBaseClusterCarbonDioxideConcentrationMeasurement
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclustercarbondioxideconcentrationmeasurement/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributeattributelist(completion:).md)
- [func readAttributeAverageMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributeaveragemeasuredvalue(completion:).md)
- [func readAttributeAverageMeasuredValueWindow(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributeaveragemeasuredvaluewindow(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributeclusterrevision(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeLevelValue(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributelevelvalue(completion:).md)
- [func readAttributeMaxMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributemaxmeasuredvalue(completion:).md)
- [func readAttributeMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributemeasuredvalue(completion:).md)
- [func readAttributeMeasurementMedium(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributemeasurementmedium(completion:).md)
- [func readAttributeMeasurementUnit(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributemeasurementunit(completion:).md)
- [func readAttributeMinMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributeminmeasuredvalue(completion:).md)
- [func readAttributePeakMeasuredValue(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributepeakmeasuredvalue(completion:).md)
- [func readAttributePeakMeasuredValueWindow(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributepeakmeasuredvaluewindow(completion:).md)
- [func readAttributeUncertainty(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributeuncertainty(completion:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAverageMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/subscribeattributeaveragemeasuredvalue(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAverageMeasuredValueWindow(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/subscribeattributeaveragemeasuredvaluewindow(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLevelValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/subscribeattributelevelvalue(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMaxMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/subscribeattributemaxmeasuredvalue(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/subscribeattributemeasuredvalue(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMeasurementMedium(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/subscribeattributemeasurementmedium(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMeasurementUnit(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/subscribeattributemeasurementunit(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMinMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/subscribeattributeminmeasuredvalue(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePeakMeasuredValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/subscribeattributepeakmeasuredvalue(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePeakMeasuredValueWindow(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/subscribeattributepeakmeasuredvaluewindow(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeUncertainty(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/subscribeattributeuncertainty(with:subscriptionestablished:reporthandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAverageMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributeaveragemeasuredvalue(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAverageMeasuredValueWindow(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributeaveragemeasuredvaluewindow(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeLevelValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributelevelvalue(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMaxMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributemaxmeasuredvalue(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributemeasuredvalue(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMeasurementMedium(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributemeasurementmedium(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMeasurementUnit(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributemeasurementunit(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMinMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributeminmeasuredvalue(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePeakMeasuredValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributepeakmeasuredvalue(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePeakMeasuredValueWindow(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributepeakmeasuredvaluewindow(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeUncertainty(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustercarbondioxideconcentrationmeasurement/readattributeuncertainty(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustercarbondioxideconcentrationmeasurement)*