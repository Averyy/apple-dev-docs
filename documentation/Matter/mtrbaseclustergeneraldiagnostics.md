# MTRBaseClusterGeneralDiagnostics

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
class MTRBaseClusterGeneralDiagnostics
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclustergeneraldiagnostics/init(device:endpoint:queue:).md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclustergeneraldiagnostics/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeActiveHardwareFaults(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeactivehardwarefaults(completion:).md)
- [func readAttributeActiveHardwareFaults(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeactivehardwarefaults(completionhandler:).md)
- [func readAttributeActiveNetworkFaults(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeactivenetworkfaults(completion:).md)
- [func readAttributeActiveNetworkFaults(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeactivenetworkfaults(completionhandler:).md)
- [func readAttributeActiveRadioFaults(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeactiveradiofaults(completion:).md)
- [func readAttributeActiveRadioFaults(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeactiveradiofaults(completionhandler:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeattributelist(completion:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeattributelist(completionhandler:).md)
- [func readAttributeBootReason(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributebootreason(completion:).md)
- [func readAttributeBootReasons(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributebootreasons(completionhandler:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeclusterrevision(completion:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributefeaturemap(completion:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributefeaturemap(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributegeneratedcommandlist(completionhandler:).md)
- [func readAttributeNetworkInterfaces(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributenetworkinterfaces(completion:).md)
- [func readAttributeNetworkInterfaces(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributenetworkinterfaces(completionhandler:).md)
- [func readAttributeRebootCount(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributerebootcount(completion:).md)
- [func readAttributeRebootCount(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributerebootcount(completionhandler:).md)
- [func readAttributeTestEventTriggersEnabled(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributetesteventtriggersenabled(completion:).md)
- [func readAttributeTestEventTriggersEnabled(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributetesteventtriggersenabled(completionhandler:).md)
- [func readAttributeTotalOperationalHours(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributetotaloperationalhours(completion:).md)
- [func readAttributeTotalOperationalHours(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributetotaloperationalhours(completionhandler:).md)
- [func readAttributeUpTime(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeuptime(completion:).md)
- [func readAttributeUpTime(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeuptime(completionhandler:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeActiveHardwareFaults(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributeactivehardwarefaults(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeActiveHardwareFaults(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributeactivehardwarefaults(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeActiveNetworkFaults(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributeactivenetworkfaults(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeActiveNetworkFaults(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributeactivenetworkfaults(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeActiveRadioFaults(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributeactiveradiofaults(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeActiveRadioFaults(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributeactiveradiofaults(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBootReason(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributebootreason(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBootReasons(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributebootreasons(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeNetworkInterfaces(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributenetworkinterfaces(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeNetworkInterfaces(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributenetworkinterfaces(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeRebootCount(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributerebootcount(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeRebootCount(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributerebootcount(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTestEventTriggersEnabled(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributetesteventtriggersenabled(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTestEventTriggersEnabled(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributetesteventtriggersenabled(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTotalOperationalHours(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributetotaloperationalhours(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTotalOperationalHours(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributetotaloperationalhours(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeUpTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributeuptime(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeUpTime(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/subscribeattributeuptime(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func testEventTrigger(with: MTRGeneralDiagnosticsClusterTestEventTriggerParams, completion: ((any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/testeventtrigger(with:completion:).md)
- [func testEventTrigger(with: MTRGeneralDiagnosticsClusterTestEventTriggerParams, completionHandler: ((any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/testeventtrigger(with:completionhandler:).md)
- [func payloadTestRequest(with: MTRGeneralDiagnosticsClusterPayloadTestRequestParams, completion: (MTRGeneralDiagnosticsClusterPayloadTestResponseParams?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/payloadtestrequest(with:completion:).md)
  Command PayloadTestRequest
- [func timeSnapshot(completion: (MTRGeneralDiagnosticsClusterTimeSnapshotResponseParams?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/timesnapshot(completion:).md)
- [func timeSnapshot(with: MTRGeneralDiagnosticsClusterTimeSnapshotParams?, completion: (MTRGeneralDiagnosticsClusterTimeSnapshotResponseParams?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/timesnapshot(with:completion:).md)
  Command TimeSnapshot
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeActiveHardwareFaults(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeactivehardwarefaults(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeActiveHardwareFaults(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeactivehardwarefaults(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeActiveNetworkFaults(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeactivenetworkfaults(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeActiveNetworkFaults(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeactivenetworkfaults(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeActiveRadioFaults(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeactiveradiofaults(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeActiveRadioFaults(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeactiveradiofaults(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeBootReason(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributebootreason(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeBootReasons(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributebootreasons(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeNetworkInterfaces(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributenetworkinterfaces(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeNetworkInterfaces(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributenetworkinterfaces(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeRebootCount(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributerebootcount(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeRebootCount(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributerebootcount(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeTestEventTriggersEnabled(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributetesteventtriggersenabled(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeTestEventTriggersEnabled(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributetesteventtriggersenabled(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeTotalOperationalHours(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributetotaloperationalhours(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeTotalOperationalHours(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributetotaloperationalhours(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeUpTime(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeuptime(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeUpTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustergeneraldiagnostics/readattributeuptime(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustergeneraldiagnostics)*