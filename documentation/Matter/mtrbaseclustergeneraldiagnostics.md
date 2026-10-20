# MTRBaseClusterGeneralDiagnostics

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
class MTRBaseClusterGeneralDiagnostics
```

```objc
@interface MTRBaseClusterGeneralDiagnostics : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclustergeneraldiagnostics/init%28device,endpoint,queue%29.md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclustergeneraldiagnostics/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeActiveHardwareFaults(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeactivehardwarefaults%28completion%29.md)
- [func readAttributeActiveHardwareFaults(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeactivehardwarefaults%28completionhandler%29.md)
- [func readAttributeActiveNetworkFaults(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeactivenetworkfaults%28completion%29.md)
- [func readAttributeActiveNetworkFaults(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeactivenetworkfaults%28completionhandler%29.md)
- [func readAttributeActiveRadioFaults(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeactiveradiofaults%28completion%29.md)
- [func readAttributeActiveRadioFaults(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeactiveradiofaults%28completionhandler%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeattributelist%28completion%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeBootReason(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributebootreason%28completion%29.md)
- [func readAttributeBootReasons(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributebootreasons%28completionhandler%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeclusterrevision%28completion%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributefeaturemap%28completion%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func readAttributeNetworkInterfaces(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributenetworkinterfaces%28completion%29.md)
- [func readAttributeNetworkInterfaces(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributenetworkinterfaces%28completionhandler%29.md)
- [func readAttributeRebootCount(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributerebootcount%28completion%29.md)
- [func readAttributeRebootCount(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributerebootcount%28completionhandler%29.md)
- [func readAttributeTestEventTriggersEnabled(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributetesteventtriggersenabled%28completion%29.md)
- [func readAttributeTestEventTriggersEnabled(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributetesteventtriggersenabled%28completionhandler%29.md)
- [func readAttributeTotalOperationalHours(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributetotaloperationalhours%28completion%29.md)
- [func readAttributeTotalOperationalHours(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributetotaloperationalhours%28completionhandler%29.md)
- [func readAttributeUpTime(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeuptime%28completion%29.md)
- [func readAttributeUpTime(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeuptime%28completionhandler%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeActiveHardwareFaults(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributeactivehardwarefaults%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeActiveHardwareFaults(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributeactivehardwarefaults%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeActiveNetworkFaults(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributeactivenetworkfaults%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeActiveNetworkFaults(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributeactivenetworkfaults%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeActiveRadioFaults(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributeactiveradiofaults%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeActiveRadioFaults(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributeactiveradiofaults%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBootReason(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributebootreason%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBootReasons(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributebootreasons%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeNetworkInterfaces(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributenetworkinterfaces%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeNetworkInterfaces(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributenetworkinterfaces%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeRebootCount(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributerebootcount%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeRebootCount(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributerebootcount%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTestEventTriggersEnabled(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributetesteventtriggersenabled%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTestEventTriggersEnabled(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributetesteventtriggersenabled%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTotalOperationalHours(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributetotaloperationalhours%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTotalOperationalHours(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributetotaloperationalhours%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeUpTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributeuptime%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeUpTime(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/subscribeattributeuptime%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func testEventTrigger(with: MTRGeneralDiagnosticsClusterTestEventTriggerParams, completion: ((any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/testeventtrigger%28with,completion%29.md)
- [func testEventTrigger(with: MTRGeneralDiagnosticsClusterTestEventTriggerParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/testeventtrigger%28with,completionhandler%29.md)
- [func payloadTestRequest(with: MTRGeneralDiagnosticsClusterPayloadTestRequestParams, completion: (MTRGeneralDiagnosticsClusterPayloadTestResponseParams?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/payloadtestrequest%28with,completion%29.md)
  Command PayloadTestRequest
- [func timeSnapshot(completion: (MTRGeneralDiagnosticsClusterTimeSnapshotResponseParams?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/timesnapshot%28completion%29.md)
- [func timeSnapshot(with: MTRGeneralDiagnosticsClusterTimeSnapshotParams?, completion: (MTRGeneralDiagnosticsClusterTimeSnapshotResponseParams?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/timesnapshot%28with,completion%29.md)
  Command TimeSnapshot
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeActiveHardwareFaults(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeactivehardwarefaults%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeActiveHardwareFaults(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeactivehardwarefaults%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeActiveNetworkFaults(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeactivenetworkfaults%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeActiveNetworkFaults(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeactivenetworkfaults%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeActiveRadioFaults(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeactiveradiofaults%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeActiveRadioFaults(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeactiveradiofaults%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeBootReason(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributebootreason%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeBootReasons(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributebootreasons%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeNetworkInterfaces(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributenetworkinterfaces%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeNetworkInterfaces(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributenetworkinterfaces%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeRebootCount(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributerebootcount%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeRebootCount(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributerebootcount%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeTestEventTriggersEnabled(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributetesteventtriggersenabled%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeTestEventTriggersEnabled(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributetesteventtriggersenabled%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeTotalOperationalHours(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributetotaloperationalhours%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeTotalOperationalHours(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributetotaloperationalhours%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeUpTime(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeuptime%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeUpTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustergeneraldiagnostics/readattributeuptime%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustergeneraldiagnostics)*