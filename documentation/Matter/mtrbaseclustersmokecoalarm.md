# MTRBaseClusterSmokeCOAlarm

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
class MTRBaseClusterSmokeCOAlarm
```

```objc
@interface MTRBaseClusterSmokeCOAlarm : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclustersmokecoalarm/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributeattributelist%28completion%29.md)
- [func readAttributeBatteryAlert(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributebatteryalert%28completion%29.md)
- [func readAttributeCOState(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributecostate%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributeclusterrevision%28completion%29.md)
- [func readAttributeContaminationState(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributecontaminationstate%28completion%29.md)
- [func readAttributeDeviceMuted(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributedevicemuted%28completion%29.md)
- [func readAttributeEndOfServiceAlert(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributeendofservicealert%28completion%29.md)
- [func readAttributeExpiryDate(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributeexpirydate%28completion%29.md)
- [func readAttributeExpressedState(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributeexpressedstate%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeHardwareFaultAlert(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributehardwarefaultalert%28completion%29.md)
- [func readAttributeInterconnectCOAlarm(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributeinterconnectcoalarm%28completion%29.md)
- [func readAttributeInterconnectSmoke(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributeinterconnectsmoke%28completion%29.md)
- [func readAttributeSmokeSensitivityLevel(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributesmokesensitivitylevel%28completion%29.md)
- [func readAttributeSmokeState(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributesmokestate%28completion%29.md)
- [func readAttributeTestInProgress(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributetestinprogress%28completion%29.md)
- [func selfTestRequest(completion: ((any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/selftestrequest%28completion%29.md)
- [func selfTestRequest(with: MTRSmokeCOAlarmClusterSelfTestRequestParams?, completion: ((any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/selftestrequest%28with,completion%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBatteryAlert(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/subscribeattributebatteryalert%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCOState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/subscribeattributecostate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeContaminationState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/subscribeattributecontaminationstate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeDeviceMuted(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/subscribeattributedevicemuted%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeEndOfServiceAlert(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/subscribeattributeendofservicealert%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeExpiryDate(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/subscribeattributeexpirydate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeExpressedState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/subscribeattributeexpressedstate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeHardwareFaultAlert(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/subscribeattributehardwarefaultalert%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeInterconnectCOAlarm(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/subscribeattributeinterconnectcoalarm%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeInterconnectSmoke(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/subscribeattributeinterconnectsmoke%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSmokeSensitivityLevel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/subscribeattributesmokesensitivitylevel%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSmokeState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/subscribeattributesmokestate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTestInProgress(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/subscribeattributetestinprogress%28with,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeSmokeSensitivityLevel(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/writeattributesmokesensitivitylevel%28withvalue,completion%29.md)
- [func writeAttributeSmokeSensitivityLevel(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/writeattributesmokesensitivitylevel%28withvalue,params,completion%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeBatteryAlert(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributebatteryalert%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCOState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributecostate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeContaminationState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributecontaminationstate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeDeviceMuted(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributedevicemuted%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeEndOfServiceAlert(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributeendofservicealert%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeExpiryDate(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributeexpirydate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeExpressedState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributeexpressedstate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeHardwareFaultAlert(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributehardwarefaultalert%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeInterconnectCOAlarm(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributeinterconnectcoalarm%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeInterconnectSmoke(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributeinterconnectsmoke%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSmokeSensitivityLevel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributesmokesensitivitylevel%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSmokeState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributesmokestate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeTestInProgress(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustersmokecoalarm/readattributetestinprogress%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustersmokecoalarm)*