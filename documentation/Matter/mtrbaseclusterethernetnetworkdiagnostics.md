# MTRBaseClusterEthernetNetworkDiagnostics

**Framework**: Matter  
**Kind**: class

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

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclusterethernetnetworkdiagnostics/init(device:endpoint:queue:).md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterethernetnetworkdiagnostics/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributeattributelist(completion:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributeattributelist(completionhandler:).md)
- [func readAttributeCarrierDetect(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributecarrierdetect(completion:).md)
- [func readAttributeCarrierDetect(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributecarrierdetect(completionhandler:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributeclusterrevision(completion:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeCollisionCount(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributecollisioncount(completion:).md)
- [func readAttributeCollisionCount(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributecollisioncount(completionhandler:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributefeaturemap(completion:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributefeaturemap(completionhandler:).md)
- [func readAttributeFullDuplex(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributefullduplex(completion:).md)
- [func readAttributeFullDuplex(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributefullduplex(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributegeneratedcommandlist(completionhandler:).md)
- [func readAttributeOverrunCount(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributeoverruncount(completion:).md)
- [func readAttributeOverrunCount(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributeoverruncount(completionhandler:).md)
- [func readAttributePHYRate(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributephyrate(completion:).md)
- [func readAttributePHYRate(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributephyrate(completionhandler:).md)
- [func readAttributePacketRxCount(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributepacketrxcount(completion:).md)
- [func readAttributePacketRxCount(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributepacketrxcount(completionhandler:).md)
- [func readAttributePacketTxCount(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributepackettxcount(completion:).md)
- [func readAttributePacketTxCount(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributepackettxcount(completionhandler:).md)
- [func readAttributeTimeSinceReset(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributetimesincereset(completion:).md)
- [func readAttributeTimeSinceReset(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributetimesincereset(completionhandler:).md)
- [func readAttributeTxErrCount(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributetxerrcount(completion:).md)
- [func readAttributeTxErrCount(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributetxerrcount(completionhandler:).md)
- [func resetCounts(completion: ((any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/resetcounts(completion:).md)
- [func resetCounts(completionHandler: ((any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/resetcounts(completionhandler:).md)
- [func resetCounts(with: MTREthernetNetworkDiagnosticsClusterResetCountsParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/resetcounts(with:completion:).md)
- [func resetCounts(with: MTREthernetNetworkDiagnosticsClusterResetCountsParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/resetcounts(with:completionhandler:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCarrierDetect(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributecarrierdetect(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCarrierDetect(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributecarrierdetect(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCollisionCount(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributecollisioncount(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCollisionCount(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributecollisioncount(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFullDuplex(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributefullduplex(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFullDuplex(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributefullduplex(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOverrunCount(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributeoverruncount(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOverrunCount(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributeoverruncount(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePHYRate(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributephyrate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePHYRate(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributephyrate(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePacketRxCount(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributepacketrxcount(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePacketRxCount(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributepacketrxcount(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePacketTxCount(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributepackettxcount(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePacketTxCount(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributepackettxcount(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTimeSinceReset(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributetimesincereset(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTimeSinceReset(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributetimesincereset(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTxErrCount(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributetxerrcount(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTxErrCount(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/subscribeattributetxerrcount(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCarrierDetect(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributecarrierdetect(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeCarrierDetect(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributecarrierdetect(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCollisionCount(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributecollisioncount(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeCollisionCount(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributecollisioncount(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFullDuplex(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributefullduplex(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFullDuplex(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributefullduplex(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeOverrunCount(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributeoverruncount(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeOverrunCount(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributeoverruncount(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePHYRate(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributephyrate(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributePHYRate(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributephyrate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePacketRxCount(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributepacketrxcount(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributePacketRxCount(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributepacketrxcount(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePacketTxCount(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributepackettxcount(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributePacketTxCount(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributepackettxcount(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeTimeSinceReset(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributetimesincereset(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeTimeSinceReset(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributetimesincereset(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeTxErrCount(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributetxerrcount(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeTxErrCount(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterethernetnetworkdiagnostics/readattributetxerrcount(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterethernetnetworkdiagnostics)*