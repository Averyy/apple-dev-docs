# MTRBaseClusterBarrierControl

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+ - Deprecated in 18.2
- iPadOS 16.1+ - Deprecated in 18.2
- Mac Catalyst 16.1+ - Deprecated in 18.2
- macOS 13.0+ - Deprecated in 15.2
- tvOS 16.1+ - Deprecated in 18.2
- visionOS 1.0+ - Deprecated in 2.2
- watchOS 9.1+ - Deprecated in 11.2

> **Deprecated**: BarrierControl is deprecated and will be removed

## Declaration

```swift
class MTRBaseClusterBarrierControl
```

```objc
@interface MTRBaseClusterBarrierControl : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclusterbarriercontrol/init%28device,endpoint,queue%29.md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterbarriercontrol/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func barrierControlGoToPercent(with: MTRBarrierControlClusterBarrierControlGoToPercentParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/barriercontrolgotopercent%28with,completion%29.md)
- [func barrierControlGoToPercent(with: MTRBarrierControlClusterBarrierControlGoToPercentParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/barriercontrolgotopercent%28with,completionhandler%29.md)
- [func barrierControlStop(completion: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/barriercontrolstop%28completion%29.md)
- [func barrierControlStop(completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/barriercontrolstop%28completionhandler%29.md)
- [func barrierControlStop(with: MTRBarrierControlClusterBarrierControlStopParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/barriercontrolstop%28with,completion%29.md)
- [func barrierControlStop(with: MTRBarrierControlClusterBarrierControlStopParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/barriercontrolstop%28with,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributeattributelist%28completion%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeBarrierCapabilities(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercapabilities%28completion%29.md)
- [func readAttributeBarrierCapabilities(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercapabilities%28completionhandler%29.md)
- [func readAttributeBarrierCloseEvents(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercloseevents%28completion%29.md)
- [func readAttributeBarrierCloseEvents(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercloseevents%28completionhandler%29.md)
- [func readAttributeBarrierClosePeriod(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercloseperiod%28completion%29.md)
- [func readAttributeBarrierClosePeriod(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercloseperiod%28completionhandler%29.md)
- [func readAttributeBarrierCommandCloseEvents(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercommandcloseevents%28completion%29.md)
- [func readAttributeBarrierCommandCloseEvents(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercommandcloseevents%28completionhandler%29.md)
- [func readAttributeBarrierCommandOpenEvents(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercommandopenevents%28completion%29.md)
- [func readAttributeBarrierCommandOpenEvents(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercommandopenevents%28completionhandler%29.md)
- [func readAttributeBarrierMovingState(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriermovingstate%28completion%29.md)
- [func readAttributeBarrierMovingState(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriermovingstate%28completionhandler%29.md)
- [func readAttributeBarrierOpenEvents(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarrieropenevents%28completion%29.md)
- [func readAttributeBarrierOpenEvents(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarrieropenevents%28completionhandler%29.md)
- [func readAttributeBarrierOpenPeriod(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarrieropenperiod%28completion%29.md)
- [func readAttributeBarrierOpenPeriod(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarrieropenperiod%28completionhandler%29.md)
- [func readAttributeBarrierPosition(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarrierposition%28completion%29.md)
- [func readAttributeBarrierPosition(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarrierposition%28completionhandler%29.md)
- [func readAttributeBarrierSafetyStatus(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriersafetystatus%28completion%29.md)
- [func readAttributeBarrierSafetyStatus(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriersafetystatus%28completionhandler%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributeclusterrevision%28completion%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributefeaturemap%28completion%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierCapabilities(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarriercapabilities%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierCapabilities(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarriercapabilities%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierCloseEvents(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarriercloseevents%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierCloseEvents(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarriercloseevents%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierClosePeriod(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarriercloseperiod%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierClosePeriod(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarriercloseperiod%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierCommandCloseEvents(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarriercommandcloseevents%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierCommandCloseEvents(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarriercommandcloseevents%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierCommandOpenEvents(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarriercommandopenevents%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierCommandOpenEvents(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarriercommandopenevents%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierMovingState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarriermovingstate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierMovingState(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarriermovingstate%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierOpenEvents(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarrieropenevents%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierOpenEvents(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarrieropenevents%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierOpenPeriod(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarrieropenperiod%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierOpenPeriod(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarrieropenperiod%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierPosition(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarrierposition%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierPosition(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarrierposition%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierSafetyStatus(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarriersafetystatus%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBarrierSafetyStatus(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributebarriersafetystatus%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeBarrierCloseEvents(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarriercloseevents%28withvalue,completion%29.md)
- [func writeAttributeBarrierCloseEvents(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarriercloseevents%28withvalue,completionhandler%29.md)
- [func writeAttributeBarrierCloseEvents(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarriercloseevents%28withvalue,params,completion%29.md)
- [func writeAttributeBarrierCloseEvents(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarriercloseevents%28withvalue,params,completionhandler%29.md)
- [func writeAttributeBarrierClosePeriod(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarriercloseperiod%28withvalue,completion%29.md)
- [func writeAttributeBarrierClosePeriod(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarriercloseperiod%28withvalue,completionhandler%29.md)
- [func writeAttributeBarrierClosePeriod(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarriercloseperiod%28withvalue,params,completion%29.md)
- [func writeAttributeBarrierClosePeriod(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarriercloseperiod%28withvalue,params,completionhandler%29.md)
- [func writeAttributeBarrierCommandCloseEvents(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarriercommandcloseevents%28withvalue,completion%29.md)
- [func writeAttributeBarrierCommandCloseEvents(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarriercommandcloseevents%28withvalue,completionhandler%29.md)
- [func writeAttributeBarrierCommandCloseEvents(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarriercommandcloseevents%28withvalue,params,completion%29.md)
- [func writeAttributeBarrierCommandCloseEvents(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarriercommandcloseevents%28withvalue,params,completionhandler%29.md)
- [func writeAttributeBarrierCommandOpenEvents(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarriercommandopenevents%28withvalue,completion%29.md)
- [func writeAttributeBarrierCommandOpenEvents(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarriercommandopenevents%28withvalue,completionhandler%29.md)
- [func writeAttributeBarrierCommandOpenEvents(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarriercommandopenevents%28withvalue,params,completion%29.md)
- [func writeAttributeBarrierCommandOpenEvents(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarriercommandopenevents%28withvalue,params,completionhandler%29.md)
- [func writeAttributeBarrierOpenEvents(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarrieropenevents%28withvalue,completion%29.md)
- [func writeAttributeBarrierOpenEvents(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarrieropenevents%28withvalue,completionhandler%29.md)
- [func writeAttributeBarrierOpenEvents(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarrieropenevents%28withvalue,params,completion%29.md)
- [func writeAttributeBarrierOpenEvents(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarrieropenevents%28withvalue,params,completionhandler%29.md)
- [func writeAttributeBarrierOpenPeriod(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarrieropenperiod%28withvalue,completion%29.md)
- [func writeAttributeBarrierOpenPeriod(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarrieropenperiod%28withvalue,completionhandler%29.md)
- [func writeAttributeBarrierOpenPeriod(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarrieropenperiod%28withvalue,params,completion%29.md)
- [func writeAttributeBarrierOpenPeriod(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/writeattributebarrieropenperiod%28withvalue,params,completionhandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeBarrierCapabilities(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercapabilities%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeBarrierCapabilities(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercapabilities%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeBarrierCloseEvents(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercloseevents%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeBarrierCloseEvents(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercloseevents%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeBarrierClosePeriod(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercloseperiod%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeBarrierClosePeriod(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercloseperiod%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeBarrierCommandCloseEvents(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercommandcloseevents%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeBarrierCommandCloseEvents(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercommandcloseevents%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeBarrierCommandOpenEvents(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercommandopenevents%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeBarrierCommandOpenEvents(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriercommandopenevents%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeBarrierMovingState(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriermovingstate%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeBarrierMovingState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriermovingstate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeBarrierOpenEvents(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarrieropenevents%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeBarrierOpenEvents(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarrieropenevents%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeBarrierOpenPeriod(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarrieropenperiod%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeBarrierOpenPeriod(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarrieropenperiod%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeBarrierPosition(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarrierposition%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeBarrierPosition(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarrierposition%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeBarrierSafetyStatus(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriersafetystatus%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeBarrierSafetyStatus(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributebarriersafetystatus%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbarriercontrol/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbarriercontrol)*