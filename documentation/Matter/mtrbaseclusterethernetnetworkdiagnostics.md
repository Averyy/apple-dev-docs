# MTRBaseClusterEthernetNetworkDiagnostics

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRBaseClusterEthernetNetworkDiagnostics
```

```objc
@interface MTRBaseClusterEthernetNetworkDiagnostics : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclusterethernetnetworkdiagnostics/init%28device,endpoint,queue%29.md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterethernetnetworkdiagnostics/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributeattributelist%28completion%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeCarrierDetect(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributecarrierdetect%28completion%29.md)
- [func readAttributeCarrierDetect(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributecarrierdetect%28completionhandler%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributeclusterrevision%28completion%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeCollisionCount(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributecollisioncount%28completion%29.md)
- [func readAttributeCollisionCount(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributecollisioncount%28completionhandler%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributefeaturemap%28completion%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeFullDuplex(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributefullduplex%28completion%29.md)
- [func readAttributeFullDuplex(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributefullduplex%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func readAttributeOverrunCount(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributeoverruncount%28completion%29.md)
- [func readAttributeOverrunCount(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributeoverruncount%28completionhandler%29.md)
- [func readAttributePHYRate(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributephyrate%28completion%29.md)
- [func readAttributePHYRate(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributephyrate%28completionhandler%29.md)
- [func readAttributePacketRxCount(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributepacketrxcount%28completion%29.md)
- [func readAttributePacketRxCount(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributepacketrxcount%28completionhandler%29.md)
- [func readAttributePacketTxCount(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributepackettxcount%28completion%29.md)
- [func readAttributePacketTxCount(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributepackettxcount%28completionhandler%29.md)
- [func readAttributeTimeSinceReset(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributetimesincereset%28completion%29.md)
- [func readAttributeTimeSinceReset(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributetimesincereset%28completionhandler%29.md)
- [func readAttributeTxErrCount(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributetxerrcount%28completion%29.md)
- [func readAttributeTxErrCount(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributetxerrcount%28completionhandler%29.md)
- [func resetCounts(completion: ((any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/resetcounts%28completion%29.md)
- [func resetCounts(completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/resetcounts%28completionhandler%29.md)
- [func resetCounts(with: MTREthernetNetworkDiagnosticsClusterResetCountsParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/resetcounts%28with,completion%29.md)
- [func resetCounts(with: MTREthernetNetworkDiagnosticsClusterResetCountsParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/resetcounts%28with,completionhandler%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCarrierDetect(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributecarrierdetect%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCarrierDetect(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributecarrierdetect%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCollisionCount(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributecollisioncount%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCollisionCount(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributecollisioncount%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFullDuplex(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributefullduplex%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFullDuplex(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributefullduplex%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOverrunCount(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributeoverruncount%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOverrunCount(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributeoverruncount%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePHYRate(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributephyrate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePHYRate(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributephyrate%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePacketRxCount(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributepacketrxcount%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePacketRxCount(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributepacketrxcount%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePacketTxCount(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributepackettxcount%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePacketTxCount(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributepackettxcount%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTimeSinceReset(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributetimesincereset%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTimeSinceReset(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributetimesincereset%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTxErrCount(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributetxerrcount%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTxErrCount(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/subscribeattributetxerrcount%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCarrierDetect(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributecarrierdetect%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeCarrierDetect(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributecarrierdetect%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCollisionCount(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributecollisioncount%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeCollisionCount(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributecollisioncount%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFullDuplex(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributefullduplex%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFullDuplex(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributefullduplex%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeOverrunCount(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributeoverruncount%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeOverrunCount(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributeoverruncount%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePHYRate(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributephyrate%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributePHYRate(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributephyrate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePacketRxCount(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributepacketrxcount%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributePacketRxCount(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributepacketrxcount%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePacketTxCount(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributepackettxcount%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributePacketTxCount(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributepackettxcount%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeTimeSinceReset(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributetimesincereset%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeTimeSinceReset(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributetimesincereset%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeTxErrCount(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributetxerrcount%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeTxErrCount(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterethernetnetworkdiagnostics/readattributetxerrcount%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterethernetnetworkdiagnostics)*