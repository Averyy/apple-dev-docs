# MTRBaseClusterSmokeCOAlarm

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
class MTRBaseClusterSmokeCOAlarm
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclustersmokecoalarm/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributeattributelist(completion:).md)
- [func readAttributeBatteryAlert(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributebatteryalert(completion:).md)
- [func readAttributeCOState(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributecostate(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributeclusterrevision(completion:).md)
- [func readAttributeContaminationState(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributecontaminationstate(completion:).md)
- [func readAttributeDeviceMuted(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributedevicemuted(completion:).md)
- [func readAttributeEndOfServiceAlert(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributeendofservicealert(completion:).md)
- [func readAttributeExpiryDate(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributeexpirydate(completion:).md)
- [func readAttributeExpressedState(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributeexpressedstate(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeHardwareFaultAlert(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributehardwarefaultalert(completion:).md)
- [func readAttributeInterconnectCOAlarm(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributeinterconnectcoalarm(completion:).md)
- [func readAttributeInterconnectSmoke(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributeinterconnectsmoke(completion:).md)
- [func readAttributeSmokeSensitivityLevel(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributesmokesensitivitylevel(completion:).md)
- [func readAttributeSmokeState(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributesmokestate(completion:).md)
- [func readAttributeTestInProgress(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributetestinprogress(completion:).md)
- [func selfTestRequest(completion: ((any Error)?) -> Void)](mtrbaseclustersmokecoalarm/selftestrequest(completion:).md)
- [func selfTestRequest(with: MTRSmokeCOAlarmClusterSelfTestRequestParams?, completion: ((any Error)?) -> Void)](mtrbaseclustersmokecoalarm/selftestrequest(with:completion:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBatteryAlert(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/subscribeattributebatteryalert(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCOState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/subscribeattributecostate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeContaminationState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/subscribeattributecontaminationstate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeDeviceMuted(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/subscribeattributedevicemuted(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeEndOfServiceAlert(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/subscribeattributeendofservicealert(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeExpiryDate(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/subscribeattributeexpirydate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeExpressedState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/subscribeattributeexpressedstate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeHardwareFaultAlert(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/subscribeattributehardwarefaultalert(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeInterconnectCOAlarm(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/subscribeattributeinterconnectcoalarm(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeInterconnectSmoke(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/subscribeattributeinterconnectsmoke(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSmokeSensitivityLevel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/subscribeattributesmokesensitivitylevel(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSmokeState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/subscribeattributesmokestate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTestInProgress(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/subscribeattributetestinprogress(with:subscriptionestablished:reporthandler:).md)
- [func writeAttributeSmokeSensitivityLevel(withValue: NSNumber, completion: ((any Error)?) -> Void)](mtrbaseclustersmokecoalarm/writeattributesmokesensitivitylevel(withvalue:completion:).md)
- [func writeAttributeSmokeSensitivityLevel(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclustersmokecoalarm/writeattributesmokesensitivitylevel(withvalue:params:completion:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeBatteryAlert(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributebatteryalert(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCOState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributecostate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeContaminationState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributecontaminationstate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeDeviceMuted(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributedevicemuted(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeEndOfServiceAlert(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributeendofservicealert(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeExpiryDate(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributeexpirydate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeExpressedState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributeexpressedstate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeHardwareFaultAlert(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributehardwarefaultalert(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeInterconnectCOAlarm(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributeinterconnectcoalarm(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeInterconnectSmoke(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributeinterconnectsmoke(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSmokeSensitivityLevel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributesmokesensitivitylevel(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSmokeState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributesmokestate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeTestInProgress(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustersmokecoalarm/readattributetestinprogress(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustersmokecoalarm)*