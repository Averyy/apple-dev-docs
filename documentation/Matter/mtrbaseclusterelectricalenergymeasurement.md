# MTRBaseClusterElectricalEnergyMeasurement

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
class MTRBaseClusterElectricalEnergyMeasurement
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterelectricalenergymeasurement/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAccuracy(completion: (MTRElectricalEnergyMeasurementClusterMeasurementAccuracyStruct?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributeaccuracy(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributeattributelist(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributeclusterrevision(completion:).md)
- [func readAttributeCumulativeEnergyExported(completion: (MTRElectricalEnergyMeasurementClusterEnergyMeasurementStruct?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributecumulativeenergyexported(completion:).md)
- [func readAttributeCumulativeEnergyImported(completion: (MTRElectricalEnergyMeasurementClusterEnergyMeasurementStruct?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributecumulativeenergyimported(completion:).md)
- [func readAttributeCumulativeEnergyReset(completion: (MTRElectricalEnergyMeasurementClusterCumulativeEnergyResetStruct?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributecumulativeenergyreset(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributegeneratedcommandlist(completion:).md)
- [func readAttributePeriodicEnergyExported(completion: (MTRElectricalEnergyMeasurementClusterEnergyMeasurementStruct?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributeperiodicenergyexported(completion:).md)
- [func readAttributePeriodicEnergyImported(completion: (MTRElectricalEnergyMeasurementClusterEnergyMeasurementStruct?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributeperiodicenergyimported(completion:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAccuracy(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRElectricalEnergyMeasurementClusterMeasurementAccuracyStruct?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/subscribeattributeaccuracy(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCumulativeEnergyExported(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRElectricalEnergyMeasurementClusterEnergyMeasurementStruct?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/subscribeattributecumulativeenergyexported(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCumulativeEnergyImported(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRElectricalEnergyMeasurementClusterEnergyMeasurementStruct?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/subscribeattributecumulativeenergyimported(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCumulativeEnergyReset(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRElectricalEnergyMeasurementClusterCumulativeEnergyResetStruct?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/subscribeattributecumulativeenergyreset(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePeriodicEnergyExported(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRElectricalEnergyMeasurementClusterEnergyMeasurementStruct?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/subscribeattributeperiodicenergyexported(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePeriodicEnergyImported(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRElectricalEnergyMeasurementClusterEnergyMeasurementStruct?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/subscribeattributeperiodicenergyimported(with:subscriptionestablished:reporthandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAccuracy(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRElectricalEnergyMeasurementClusterMeasurementAccuracyStruct?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributeaccuracy(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCumulativeEnergyExported(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRElectricalEnergyMeasurementClusterEnergyMeasurementStruct?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributecumulativeenergyexported(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCumulativeEnergyImported(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRElectricalEnergyMeasurementClusterEnergyMeasurementStruct?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributecumulativeenergyimported(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCumulativeEnergyReset(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRElectricalEnergyMeasurementClusterCumulativeEnergyResetStruct?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributecumulativeenergyreset(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePeriodicEnergyExported(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRElectricalEnergyMeasurementClusterEnergyMeasurementStruct?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributeperiodicenergyexported(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePeriodicEnergyImported(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRElectricalEnergyMeasurementClusterEnergyMeasurementStruct?, (any Error)?) -> Void)](mtrbaseclusterelectricalenergymeasurement/readattributeperiodicenergyimported(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterelectricalenergymeasurement)*