# MTRBaseClusterThermostatUserInterfaceConfiguration

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
class MTRBaseClusterThermostatUserInterfaceConfiguration
```

```objc
@interface MTRBaseClusterThermostatUserInterfaceConfiguration : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclusterthermostatuserinterfaceconfiguration/init%28device,endpoint,queue%29.md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterthermostatuserinterfaceconfiguration/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeattributelist%28completion%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeclusterrevision%28completion%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributefeaturemap%28completion%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func readAttributeKeypadLockout(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributekeypadlockout%28completion%29.md)
- [func readAttributeKeypadLockout(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributekeypadlockout%28completionhandler%29.md)
- [func readAttributeScheduleProgrammingVisibility(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributescheduleprogrammingvisibility%28completion%29.md)
- [func readAttributeScheduleProgrammingVisibility(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributescheduleprogrammingvisibility%28completionhandler%29.md)
- [func readAttributeTemperatureDisplayMode(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributetemperaturedisplaymode%28completion%29.md)
- [func readAttributeTemperatureDisplayMode(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributetemperaturedisplaymode%28completionhandler%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeKeypadLockout(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributekeypadlockout%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeKeypadLockout(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributekeypadlockout%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeScheduleProgrammingVisibility(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributescheduleprogrammingvisibility%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeScheduleProgrammingVisibility(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributescheduleprogrammingvisibility%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTemperatureDisplayMode(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributetemperaturedisplaymode%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTemperatureDisplayMode(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/subscribeattributetemperaturedisplaymode%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeKeypadLockout(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributekeypadlockout%28withvalue,completion%29.md)
- [func writeAttributeKeypadLockout(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributekeypadlockout%28withvalue,completionhandler%29.md)
- [func writeAttributeKeypadLockout(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributekeypadlockout%28withvalue,params,completion%29.md)
- [func writeAttributeKeypadLockout(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributekeypadlockout%28withvalue,params,completionhandler%29.md)
- [func writeAttributeScheduleProgrammingVisibility(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributescheduleprogrammingvisibility%28withvalue,completion%29.md)
- [func writeAttributeScheduleProgrammingVisibility(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributescheduleprogrammingvisibility%28withvalue,completionhandler%29.md)
- [func writeAttributeScheduleProgrammingVisibility(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributescheduleprogrammingvisibility%28withvalue,params,completion%29.md)
- [func writeAttributeScheduleProgrammingVisibility(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributescheduleprogrammingvisibility%28withvalue,params,completionhandler%29.md)
- [func writeAttributeTemperatureDisplayMode(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributetemperaturedisplaymode%28withvalue,completion%29.md)
- [func writeAttributeTemperatureDisplayMode(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributetemperaturedisplaymode%28withvalue,completionhandler%29.md)
- [func writeAttributeTemperatureDisplayMode(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributetemperaturedisplaymode%28withvalue,params,completion%29.md)
- [func writeAttributeTemperatureDisplayMode(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/writeattributetemperaturedisplaymode%28withvalue,params,completionhandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeKeypadLockout(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributekeypadlockout%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeKeypadLockout(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributekeypadlockout%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeScheduleProgrammingVisibility(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributescheduleprogrammingvisibility%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeScheduleProgrammingVisibility(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributescheduleprogrammingvisibility%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeTemperatureDisplayMode(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributetemperaturedisplaymode%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeTemperatureDisplayMode(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthermostatuserinterfaceconfiguration/readattributetemperaturedisplaymode%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterthermostatuserinterfaceconfiguration)*