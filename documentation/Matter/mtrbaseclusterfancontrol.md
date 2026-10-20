# MTRBaseClusterFanControl

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
class MTRBaseClusterFanControl
```

```objc
@interface MTRBaseClusterFanControl : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclusterfancontrol/init%28device,endpoint,queue%29.md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterfancontrol/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeAirflowDirection(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributeairflowdirection%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributeattributelist%28completion%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributeclusterrevision%28completion%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeFanMode(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributefanmode%28completion%29.md)
- [func readAttributeFanMode(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributefanmode%28completionhandler%29.md)
- [func readAttributeFanModeSequence(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributefanmodesequence%28completion%29.md)
- [func readAttributeFanModeSequence(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributefanmodesequence%28completionhandler%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributefeaturemap%28completion%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func readAttributePercentCurrent(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributepercentcurrent%28completion%29.md)
- [func readAttributePercentCurrent(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributepercentcurrent%28completionhandler%29.md)
- [func readAttributePercentSetting(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributepercentsetting%28completion%29.md)
- [func readAttributePercentSetting(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributepercentsetting%28completionhandler%29.md)
- [func readAttributeRockSetting(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributerocksetting%28completion%29.md)
- [func readAttributeRockSetting(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributerocksetting%28completionhandler%29.md)
- [func readAttributeRockSupport(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributerocksupport%28completion%29.md)
- [func readAttributeRockSupport(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributerocksupport%28completionhandler%29.md)
- [func readAttributeSpeedCurrent(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributespeedcurrent%28completion%29.md)
- [func readAttributeSpeedCurrent(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributespeedcurrent%28completionhandler%29.md)
- [func readAttributeSpeedMax(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributespeedmax%28completion%29.md)
- [func readAttributeSpeedMax(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributespeedmax%28completionhandler%29.md)
- [func readAttributeSpeedSetting(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributespeedsetting%28completion%29.md)
- [func readAttributeSpeedSetting(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributespeedsetting%28completionhandler%29.md)
- [func readAttributeWindSetting(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributewindsetting%28completion%29.md)
- [func readAttributeWindSetting(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributewindsetting%28completionhandler%29.md)
- [func readAttributeWindSupport(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributewindsupport%28completion%29.md)
- [func readAttributeWindSupport(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributewindsupport%28completionhandler%29.md)
- [func step(with: MTRFanControlClusterStepParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/step%28with,completion%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAirflowDirection(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributeairflowdirection%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFanMode(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributefanmode%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFanMode(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributefanmode%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFanModeSequence(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributefanmodesequence%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFanModeSequence(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributefanmodesequence%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePercentCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributepercentcurrent%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePercentCurrent(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributepercentcurrent%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePercentSetting(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributepercentsetting%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePercentSetting(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributepercentsetting%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeRockSetting(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributerocksetting%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeRockSetting(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributerocksetting%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeRockSupport(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributerocksupport%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeRockSupport(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributerocksupport%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSpeedCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributespeedcurrent%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSpeedCurrent(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributespeedcurrent%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSpeedMax(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributespeedmax%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSpeedMax(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributespeedmax%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSpeedSetting(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributespeedsetting%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSpeedSetting(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributespeedsetting%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeWindSetting(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributewindsetting%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeWindSetting(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributewindsetting%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeWindSupport(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributewindsupport%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeWindSupport(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/subscribeattributewindsupport%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeAirflowDirection(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributeairflowdirection%28withvalue,completion%29.md)
- [func writeAttributeAirflowDirection(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributeairflowdirection%28withvalue,params,completion%29.md)
- [func writeAttributeFanMode(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributefanmode%28withvalue,completion%29.md)
- [func writeAttributeFanMode(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributefanmode%28withvalue,completionhandler%29.md)
- [func writeAttributeFanMode(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributefanmode%28withvalue,params,completion%29.md)
- [func writeAttributeFanMode(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributefanmode%28withvalue,params,completionhandler%29.md)
- [func writeAttributeFanModeSequence(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributefanmodesequence%28withvalue,completion%29.md)
- [func writeAttributeFanModeSequence(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributefanmodesequence%28withvalue,completionhandler%29.md)
- [func writeAttributeFanModeSequence(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributefanmodesequence%28withvalue,params,completion%29.md)
- [func writeAttributeFanModeSequence(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributefanmodesequence%28withvalue,params,completionhandler%29.md)
- [func writeAttributePercentSetting(withValue: NSNumber?, completion: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributepercentsetting%28withvalue,completion%29.md)
- [func writeAttributePercentSetting(withValue: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributepercentsetting%28withvalue,completionhandler%29.md)
- [func writeAttributePercentSetting(withValue: NSNumber?, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributepercentsetting%28withvalue,params,completion%29.md)
- [func writeAttributePercentSetting(withValue: NSNumber?, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributepercentsetting%28withvalue,params,completionhandler%29.md)
- [func writeAttributeRockSetting(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributerocksetting%28withvalue,completion%29.md)
- [func writeAttributeRockSetting(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributerocksetting%28withvalue,completionhandler%29.md)
- [func writeAttributeRockSetting(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributerocksetting%28withvalue,params,completion%29.md)
- [func writeAttributeRockSetting(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributerocksetting%28withvalue,params,completionhandler%29.md)
- [func writeAttributeSpeedSetting(withValue: NSNumber?, completion: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributespeedsetting%28withvalue,completion%29.md)
- [func writeAttributeSpeedSetting(withValue: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributespeedsetting%28withvalue,completionhandler%29.md)
- [func writeAttributeSpeedSetting(withValue: NSNumber?, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributespeedsetting%28withvalue,params,completion%29.md)
- [func writeAttributeSpeedSetting(withValue: NSNumber?, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributespeedsetting%28withvalue,params,completionhandler%29.md)
- [func writeAttributeWindSetting(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributewindsetting%28withvalue,completion%29.md)
- [func writeAttributeWindSetting(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributewindsetting%28withvalue,completionhandler%29.md)
- [func writeAttributeWindSetting(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributewindsetting%28withvalue,params,completion%29.md)
- [func writeAttributeWindSetting(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterfancontrol/writeattributewindsetting%28withvalue,params,completionhandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAirflowDirection(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributeairflowdirection%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFanMode(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributefanmode%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFanMode(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributefanmode%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFanModeSequence(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributefanmodesequence%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFanModeSequence(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributefanmodesequence%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePercentCurrent(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributepercentcurrent%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributePercentCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributepercentcurrent%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePercentSetting(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributepercentsetting%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributePercentSetting(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributepercentsetting%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeRockSetting(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributerocksetting%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeRockSetting(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributerocksetting%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeRockSupport(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributerocksupport%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeRockSupport(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributerocksupport%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSpeedCurrent(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributespeedcurrent%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeSpeedCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributespeedcurrent%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSpeedMax(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributespeedmax%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeSpeedMax(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributespeedmax%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSpeedSetting(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributespeedsetting%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeSpeedSetting(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributespeedsetting%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeWindSetting(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributewindsetting%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeWindSetting(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributewindsetting%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeWindSupport(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributewindsupport%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeWindSupport(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterfancontrol/readattributewindsupport%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterfancontrol)*