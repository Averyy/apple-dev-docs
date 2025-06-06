# MTRBaseClusterBarrierControl

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
class MTRBaseClusterBarrierControl
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclusterbarriercontrol/init(device:endpoint:queue:).md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterbarriercontrol/init(device:endpointid:queue:).md)
### Instance Methods
- [func barrierControlGoToPercent(with: MTRBarrierControlClusterBarrierControlGoToPercentParams, completion: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/barriercontrolgotopercent(with:completion:).md)
- [func barrierControlGoToPercent(with: MTRBarrierControlClusterBarrierControlGoToPercentParams, completionHandler: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/barriercontrolgotopercent(with:completionhandler:).md)
- [func barrierControlStop(completion: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/barriercontrolstop(completion:).md)
- [func barrierControlStop(completionHandler: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/barriercontrolstop(completionhandler:).md)
- [func barrierControlStop(with: MTRBarrierControlClusterBarrierControlStopParams?, completion: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/barriercontrolstop(with:completion:).md)
- [func barrierControlStop(with: MTRBarrierControlClusterBarrierControlStopParams?, completionHandler: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/barriercontrolstop(with:completionhandler:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributeattributelist(completion:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributeattributelist(completionhandler:).md)
- [func readAttributeBarrierCapabilities(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercapabilities(completion:).md)
- [func readAttributeBarrierCapabilities(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercapabilities(completionhandler:).md)
- [func readAttributeBarrierCloseEvents(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercloseevents(completion:).md)
- [func readAttributeBarrierCloseEvents(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercloseevents(completionhandler:).md)
- [func readAttributeBarrierClosePeriod(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercloseperiod(completion:).md)
- [func readAttributeBarrierClosePeriod(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercloseperiod(completionhandler:).md)
- [func readAttributeBarrierCommandCloseEvents(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercommandcloseevents(completion:).md)
- [func readAttributeBarrierCommandCloseEvents(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercommandcloseevents(completionhandler:).md)
- [func readAttributeBarrierCommandOpenEvents(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercommandopenevents(completion:).md)
- [func readAttributeBarrierCommandOpenEvents(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercommandopenevents(completionhandler:).md)
- [func readAttributeBarrierMovingState(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriermovingstate(completion:).md)
- [func readAttributeBarrierMovingState(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriermovingstate(completionhandler:).md)
- [func readAttributeBarrierOpenEvents(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarrieropenevents(completion:).md)
- [func readAttributeBarrierOpenEvents(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarrieropenevents(completionhandler:).md)
- [func readAttributeBarrierOpenPeriod(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarrieropenperiod(completion:).md)
- [func readAttributeBarrierOpenPeriod(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarrieropenperiod(completionhandler:).md)
- [func readAttributeBarrierPosition(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarrierposition(completion:).md)
- [func readAttributeBarrierPosition(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarrierposition(completionhandler:).md)
- [func readAttributeBarrierSafetyStatus(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriersafetystatus(completion:).md)
- [func readAttributeBarrierSafetyStatus(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriersafetystatus(completionhandler:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributeclusterrevision(completion:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributefeaturemap(completion:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributefeaturemap(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributegeneratedcommandlist(completionhandler:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierCapabilities(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarriercapabilities(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierCapabilities(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarriercapabilities(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierCloseEvents(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarriercloseevents(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierCloseEvents(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarriercloseevents(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierClosePeriod(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarriercloseperiod(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierClosePeriod(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarriercloseperiod(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierCommandCloseEvents(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarriercommandcloseevents(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierCommandCloseEvents(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarriercommandcloseevents(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierCommandOpenEvents(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarriercommandopenevents(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierCommandOpenEvents(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarriercommandopenevents(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierMovingState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarriermovingstate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierMovingState(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarriermovingstate(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierOpenEvents(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarrieropenevents(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierOpenEvents(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarrieropenevents(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierOpenPeriod(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarrieropenperiod(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierOpenPeriod(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarrieropenperiod(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierPosition(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarrierposition(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierPosition(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarrierposition(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierSafetyStatus(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarriersafetystatus(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBarrierSafetyStatus(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributebarriersafetystatus(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func writeAttributeBarrierCloseEvents(withValue: NSNumber, completion: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarriercloseevents(withvalue:completion:).md)
- [func writeAttributeBarrierCloseEvents(withValue: NSNumber, completionHandler: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarriercloseevents(withvalue:completionhandler:).md)
- [func writeAttributeBarrierCloseEvents(withValue: NSNumber, params: MTRWriteParams?, completion: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarriercloseevents(withvalue:params:completion:).md)
- [func writeAttributeBarrierCloseEvents(withValue: NSNumber, params: MTRWriteParams?, completionHandler: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarriercloseevents(withvalue:params:completionhandler:).md)
- [func writeAttributeBarrierClosePeriod(withValue: NSNumber, completion: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarriercloseperiod(withvalue:completion:).md)
- [func writeAttributeBarrierClosePeriod(withValue: NSNumber, completionHandler: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarriercloseperiod(withvalue:completionhandler:).md)
- [func writeAttributeBarrierClosePeriod(withValue: NSNumber, params: MTRWriteParams?, completion: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarriercloseperiod(withvalue:params:completion:).md)
- [func writeAttributeBarrierClosePeriod(withValue: NSNumber, params: MTRWriteParams?, completionHandler: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarriercloseperiod(withvalue:params:completionhandler:).md)
- [func writeAttributeBarrierCommandCloseEvents(withValue: NSNumber, completion: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarriercommandcloseevents(withvalue:completion:).md)
- [func writeAttributeBarrierCommandCloseEvents(withValue: NSNumber, completionHandler: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarriercommandcloseevents(withvalue:completionhandler:).md)
- [func writeAttributeBarrierCommandCloseEvents(withValue: NSNumber, params: MTRWriteParams?, completion: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarriercommandcloseevents(withvalue:params:completion:).md)
- [func writeAttributeBarrierCommandCloseEvents(withValue: NSNumber, params: MTRWriteParams?, completionHandler: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarriercommandcloseevents(withvalue:params:completionhandler:).md)
- [func writeAttributeBarrierCommandOpenEvents(withValue: NSNumber, completion: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarriercommandopenevents(withvalue:completion:).md)
- [func writeAttributeBarrierCommandOpenEvents(withValue: NSNumber, completionHandler: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarriercommandopenevents(withvalue:completionhandler:).md)
- [func writeAttributeBarrierCommandOpenEvents(withValue: NSNumber, params: MTRWriteParams?, completion: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarriercommandopenevents(withvalue:params:completion:).md)
- [func writeAttributeBarrierCommandOpenEvents(withValue: NSNumber, params: MTRWriteParams?, completionHandler: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarriercommandopenevents(withvalue:params:completionhandler:).md)
- [func writeAttributeBarrierOpenEvents(withValue: NSNumber, completion: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarrieropenevents(withvalue:completion:).md)
- [func writeAttributeBarrierOpenEvents(withValue: NSNumber, completionHandler: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarrieropenevents(withvalue:completionhandler:).md)
- [func writeAttributeBarrierOpenEvents(withValue: NSNumber, params: MTRWriteParams?, completion: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarrieropenevents(withvalue:params:completion:).md)
- [func writeAttributeBarrierOpenEvents(withValue: NSNumber, params: MTRWriteParams?, completionHandler: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarrieropenevents(withvalue:params:completionhandler:).md)
- [func writeAttributeBarrierOpenPeriod(withValue: NSNumber, completion: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarrieropenperiod(withvalue:completion:).md)
- [func writeAttributeBarrierOpenPeriod(withValue: NSNumber, completionHandler: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarrieropenperiod(withvalue:completionhandler:).md)
- [func writeAttributeBarrierOpenPeriod(withValue: NSNumber, params: MTRWriteParams?, completion: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarrieropenperiod(withvalue:params:completion:).md)
- [func writeAttributeBarrierOpenPeriod(withValue: NSNumber, params: MTRWriteParams?, completionHandler: MTRStatusCompletion)](mtrbaseclusterbarriercontrol/writeattributebarrieropenperiod(withvalue:params:completionhandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeBarrierCapabilities(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercapabilities(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeBarrierCapabilities(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercapabilities(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeBarrierCloseEvents(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercloseevents(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeBarrierCloseEvents(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercloseevents(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeBarrierClosePeriod(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercloseperiod(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeBarrierClosePeriod(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercloseperiod(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeBarrierCommandCloseEvents(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercommandcloseevents(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeBarrierCommandCloseEvents(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercommandcloseevents(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeBarrierCommandOpenEvents(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercommandopenevents(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeBarrierCommandOpenEvents(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriercommandopenevents(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeBarrierMovingState(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriermovingstate(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeBarrierMovingState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriermovingstate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeBarrierOpenEvents(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarrieropenevents(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeBarrierOpenEvents(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarrieropenevents(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeBarrierOpenPeriod(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarrieropenperiod(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeBarrierOpenPeriod(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarrieropenperiod(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeBarrierPosition(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarrierposition(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeBarrierPosition(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarrierposition(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeBarrierSafetyStatus(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriersafetystatus(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeBarrierSafetyStatus(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributebarriersafetystatus(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbarriercontrol/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbarriercontrol)*