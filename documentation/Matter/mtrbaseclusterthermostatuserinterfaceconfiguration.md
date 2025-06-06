# MTRBaseClusterThermostatUserInterfaceConfiguration

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
class MTRBaseClusterThermostatUserInterfaceConfiguration
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclusterthermostatuserinterfaceconfiguration/init(device:endpoint:queue:).md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterthermostatuserinterfaceconfiguration/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeattributelist(completion:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeattributelist(completionhandler:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeclusterrevision(completion:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributefeaturemap(completion:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributefeaturemap(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributegeneratedcommandlist(completionhandler:).md)
- [func readAttributeKeypadLockout(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributekeypadlockout(completion:).md)
- [func readAttributeKeypadLockout(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributekeypadlockout(completionhandler:).md)
- [func readAttributeScheduleProgrammingVisibility(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributescheduleprogrammingvisibility(completion:).md)
- [func readAttributeScheduleProgrammingVisibility(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributescheduleprogrammingvisibility(completionhandler:).md)
- [func readAttributeTemperatureDisplayMode(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributetemperaturedisplaymode(completion:).md)
- [func readAttributeTemperatureDisplayMode(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributetemperaturedisplaymode(completionhandler:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeKeypadLockout(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributekeypadlockout(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeKeypadLockout(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributekeypadlockout(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeScheduleProgrammingVisibility(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributescheduleprogrammingvisibility(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeScheduleProgrammingVisibility(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributescheduleprogrammingvisibility(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTemperatureDisplayMode(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributetemperaturedisplaymode(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTemperatureDisplayMode(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributetemperaturedisplaymode(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func writeAttributeKeypadLockout(withValue: NSNumber, completion: MTRStatusCompletion)](mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributekeypadlockout(withvalue:completion:).md)
- [func writeAttributeKeypadLockout(withValue: NSNumber, completionHandler: MTRStatusCompletion)](mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributekeypadlockout(withvalue:completionhandler:).md)
- [func writeAttributeKeypadLockout(withValue: NSNumber, params: MTRWriteParams?, completion: MTRStatusCompletion)](mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributekeypadlockout(withvalue:params:completion:).md)
- [func writeAttributeKeypadLockout(withValue: NSNumber, params: MTRWriteParams?, completionHandler: MTRStatusCompletion)](mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributekeypadlockout(withvalue:params:completionhandler:).md)
- [func writeAttributeScheduleProgrammingVisibility(withValue: NSNumber, completion: MTRStatusCompletion)](mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributescheduleprogrammingvisibility(withvalue:completion:).md)
- [func writeAttributeScheduleProgrammingVisibility(withValue: NSNumber, completionHandler: MTRStatusCompletion)](mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributescheduleprogrammingvisibility(withvalue:completionhandler:).md)
- [func writeAttributeScheduleProgrammingVisibility(withValue: NSNumber, params: MTRWriteParams?, completion: MTRStatusCompletion)](mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributescheduleprogrammingvisibility(withvalue:params:completion:).md)
- [func writeAttributeScheduleProgrammingVisibility(withValue: NSNumber, params: MTRWriteParams?, completionHandler: MTRStatusCompletion)](mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributescheduleprogrammingvisibility(withvalue:params:completionhandler:).md)
- [func writeAttributeTemperatureDisplayMode(withValue: NSNumber, completion: MTRStatusCompletion)](mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributetemperaturedisplaymode(withvalue:completion:).md)
- [func writeAttributeTemperatureDisplayMode(withValue: NSNumber, completionHandler: MTRStatusCompletion)](mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributetemperaturedisplaymode(withvalue:completionhandler:).md)
- [func writeAttributeTemperatureDisplayMode(withValue: NSNumber, params: MTRWriteParams?, completion: MTRStatusCompletion)](mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributetemperaturedisplaymode(withvalue:params:completion:).md)
- [func writeAttributeTemperatureDisplayMode(withValue: NSNumber, params: MTRWriteParams?, completionHandler: MTRStatusCompletion)](mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributetemperaturedisplaymode(withvalue:params:completionhandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeKeypadLockout(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributekeypadlockout(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeKeypadLockout(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributekeypadlockout(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeScheduleProgrammingVisibility(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributescheduleprogrammingvisibility(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeScheduleProgrammingVisibility(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributescheduleprogrammingvisibility(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeTemperatureDisplayMode(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributetemperaturedisplaymode(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeTemperatureDisplayMode(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthermostatuserinterfaceconfiguration/readattributetemperaturedisplaymode(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterthermostatuserinterfaceconfiguration)*