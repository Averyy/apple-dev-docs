# MTRBaseClusterElectricalPowerMeasurement

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
class MTRBaseClusterElectricalPowerMeasurement
```

```objc
@interface MTRBaseClusterElectricalPowerMeasurement : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterelectricalpowermeasurement/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAccuracy(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeaccuracy%28completion%29.md)
- [func readAttributeActiveCurrent(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeactivecurrent%28completion%29.md)
- [func readAttributeActivePower(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeactivepower%28completion%29.md)
- [func readAttributeApparentCurrent(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeapparentcurrent%28completion%29.md)
- [func readAttributeApparentPower(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeapparentpower%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeattributelist%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeclusterrevision%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributefeaturemap%28completion%29.md)
- [func readAttributeFrequency(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributefrequency%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeHarmonicCurrents(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeharmoniccurrents%28completion%29.md)
- [func readAttributeHarmonicPhases(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeharmonicphases%28completion%29.md)
- [func readAttributeNeutralCurrent(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeneutralcurrent%28completion%29.md)
- [func readAttributeNumberOfMeasurementTypes(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributenumberofmeasurementtypes%28completion%29.md)
- [func readAttributePowerFactor(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributepowerfactor%28completion%29.md)
- [func readAttributePowerMode(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributepowermode%28completion%29.md)
- [func readAttributeRMSCurrent(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributermscurrent%28completion%29.md)
- [func readAttributeRMSPower(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributermspower%28completion%29.md)
- [func readAttributeRMSVoltage(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributermsvoltage%28completion%29.md)
- [func readAttributeRanges(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeranges%28completion%29.md)
- [func readAttributeReactiveCurrent(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributereactivecurrent%28completion%29.md)
- [func readAttributeReactivePower(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributereactivepower%28completion%29.md)
- [func readAttributeVoltage(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributevoltage%28completion%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAccuracy(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributeaccuracy%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeActiveCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributeactivecurrent%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeActivePower(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributeactivepower%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeApparentCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributeapparentcurrent%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeApparentPower(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributeapparentpower%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFrequency(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributefrequency%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeHarmonicCurrents(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributeharmoniccurrents%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeHarmonicPhases(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributeharmonicphases%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeNeutralCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributeneutralcurrent%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeNumberOfMeasurementTypes(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributenumberofmeasurementtypes%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePowerFactor(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributepowerfactor%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePowerMode(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributepowermode%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeRMSCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributermscurrent%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeRMSPower(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributermspower%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeRMSVoltage(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributermsvoltage%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeRanges(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributeranges%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeReactiveCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributereactivecurrent%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeReactivePower(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributereactivepower%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeVoltage(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/subscribeattributevoltage%28with,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAccuracy(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeaccuracy%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeActiveCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeactivecurrent%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeActivePower(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeactivepower%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeApparentCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeapparentcurrent%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeApparentPower(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeapparentpower%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFrequency(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributefrequency%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeHarmonicCurrents(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeharmoniccurrents%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeHarmonicPhases(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeharmonicphases%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeNeutralCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeneutralcurrent%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeNumberOfMeasurementTypes(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributenumberofmeasurementtypes%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePowerFactor(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributepowerfactor%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePowerMode(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributepowermode%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeRMSCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributermscurrent%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeRMSPower(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributermspower%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeRMSVoltage(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributermsvoltage%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeRanges(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributeranges%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeReactiveCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributereactivecurrent%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeReactivePower(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributereactivepower%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeVoltage(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterelectricalpowermeasurement/readattributevoltage%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterelectricalpowermeasurement)*