# MTRBaseClusterElectricalPowerMeasurement

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
class MTRBaseClusterElectricalPowerMeasurement
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterelectricalpowermeasurement/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAccuracy(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeaccuracy(completion:).md)
- [func readAttributeActiveCurrent(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeactivecurrent(completion:).md)
- [func readAttributeActivePower(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeactivepower(completion:).md)
- [func readAttributeApparentCurrent(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeapparentcurrent(completion:).md)
- [func readAttributeApparentPower(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeapparentpower(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeattributelist(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeclusterrevision(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributefeaturemap(completion:).md)
- [func readAttributeFrequency(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributefrequency(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeHarmonicCurrents(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeharmoniccurrents(completion:).md)
- [func readAttributeHarmonicPhases(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeharmonicphases(completion:).md)
- [func readAttributeNeutralCurrent(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeneutralcurrent(completion:).md)
- [func readAttributeNumberOfMeasurementTypes(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributenumberofmeasurementtypes(completion:).md)
- [func readAttributePowerFactor(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributepowerfactor(completion:).md)
- [func readAttributePowerMode(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributepowermode(completion:).md)
- [func readAttributeRMSCurrent(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributermscurrent(completion:).md)
- [func readAttributeRMSPower(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributermspower(completion:).md)
- [func readAttributeRMSVoltage(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributermsvoltage(completion:).md)
- [func readAttributeRanges(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeranges(completion:).md)
- [func readAttributeReactiveCurrent(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributereactivecurrent(completion:).md)
- [func readAttributeReactivePower(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributereactivepower(completion:).md)
- [func readAttributeVoltage(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributevoltage(completion:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAccuracy(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributeaccuracy(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeActiveCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributeactivecurrent(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeActivePower(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributeactivepower(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeApparentCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributeapparentcurrent(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeApparentPower(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributeapparentpower(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFrequency(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributefrequency(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeHarmonicCurrents(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributeharmoniccurrents(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeHarmonicPhases(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributeharmonicphases(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeNeutralCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributeneutralcurrent(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeNumberOfMeasurementTypes(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributenumberofmeasurementtypes(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePowerFactor(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributepowerfactor(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePowerMode(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributepowermode(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeRMSCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributermscurrent(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeRMSPower(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributermspower(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeRMSVoltage(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributermsvoltage(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeRanges(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributeranges(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeReactiveCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributereactivecurrent(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeReactivePower(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributereactivepower(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeVoltage(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/subscribeattributevoltage(with:subscriptionestablished:reporthandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAccuracy(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeaccuracy(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeActiveCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeactivecurrent(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeActivePower(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeactivepower(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeApparentCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeapparentcurrent(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeApparentPower(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeapparentpower(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFrequency(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributefrequency(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeHarmonicCurrents(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeharmoniccurrents(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeHarmonicPhases(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeharmonicphases(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeNeutralCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeneutralcurrent(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeNumberOfMeasurementTypes(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributenumberofmeasurementtypes(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePowerFactor(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributepowerfactor(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePowerMode(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributepowermode(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeRMSCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributermscurrent(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeRMSPower(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributermspower(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeRMSVoltage(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributermsvoltage(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeRanges(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributeranges(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeReactiveCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributereactivecurrent(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeReactivePower(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributereactivepower(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeVoltage(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterelectricalpowermeasurement/readattributevoltage(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterelectricalpowermeasurement)*