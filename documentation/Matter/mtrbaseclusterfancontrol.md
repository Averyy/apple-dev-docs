# MTRBaseClusterFanControl

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
class MTRBaseClusterFanControl
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclusterfancontrol/init(device:endpoint:queue:).md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterfancontrol/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeAirflowDirection(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributeairflowdirection(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributeattributelist(completion:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributeattributelist(completionhandler:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributeclusterrevision(completion:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeFanMode(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributefanmode(completion:).md)
- [func readAttributeFanMode(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributefanmode(completionhandler:).md)
- [func readAttributeFanModeSequence(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributefanmodesequence(completion:).md)
- [func readAttributeFanModeSequence(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributefanmodesequence(completionhandler:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributefeaturemap(completion:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributefeaturemap(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributegeneratedcommandlist(completionhandler:).md)
- [func readAttributePercentCurrent(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributepercentcurrent(completion:).md)
- [func readAttributePercentCurrent(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributepercentcurrent(completionhandler:).md)
- [func readAttributePercentSetting(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributepercentsetting(completion:).md)
- [func readAttributePercentSetting(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributepercentsetting(completionhandler:).md)
- [func readAttributeRockSetting(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributerocksetting(completion:).md)
- [func readAttributeRockSetting(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributerocksetting(completionhandler:).md)
- [func readAttributeRockSupport(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributerocksupport(completion:).md)
- [func readAttributeRockSupport(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributerocksupport(completionhandler:).md)
- [func readAttributeSpeedCurrent(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributespeedcurrent(completion:).md)
- [func readAttributeSpeedCurrent(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributespeedcurrent(completionhandler:).md)
- [func readAttributeSpeedMax(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributespeedmax(completion:).md)
- [func readAttributeSpeedMax(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributespeedmax(completionhandler:).md)
- [func readAttributeSpeedSetting(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributespeedsetting(completion:).md)
- [func readAttributeSpeedSetting(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributespeedsetting(completionhandler:).md)
- [func readAttributeWindSetting(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributewindsetting(completion:).md)
- [func readAttributeWindSetting(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributewindsetting(completionhandler:).md)
- [func readAttributeWindSupport(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributewindsupport(completion:).md)
- [func readAttributeWindSupport(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributewindsupport(completionhandler:).md)
- [func step(with: MTRFanControlClusterStepParams, completion: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/step(with:completion:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAirflowDirection(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributeairflowdirection(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFanMode(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributefanmode(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFanMode(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributefanmode(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFanModeSequence(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributefanmodesequence(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFanModeSequence(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributefanmodesequence(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePercentCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributepercentcurrent(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePercentCurrent(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributepercentcurrent(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePercentSetting(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributepercentsetting(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePercentSetting(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributepercentsetting(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeRockSetting(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributerocksetting(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeRockSetting(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributerocksetting(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeRockSupport(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributerocksupport(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeRockSupport(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributerocksupport(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSpeedCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributespeedcurrent(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSpeedCurrent(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributespeedcurrent(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSpeedMax(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributespeedmax(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSpeedMax(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributespeedmax(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSpeedSetting(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributespeedsetting(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSpeedSetting(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributespeedsetting(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeWindSetting(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributewindsetting(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeWindSetting(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributewindsetting(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeWindSupport(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributewindsupport(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeWindSupport(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/subscribeattributewindsupport(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func writeAttributeAirflowDirection(withValue: NSNumber, completion: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributeairflowdirection(withvalue:completion:).md)
- [func writeAttributeAirflowDirection(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributeairflowdirection(withvalue:params:completion:).md)
- [func writeAttributeFanMode(withValue: NSNumber, completion: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributefanmode(withvalue:completion:).md)
- [func writeAttributeFanMode(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributefanmode(withvalue:completionhandler:).md)
- [func writeAttributeFanMode(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributefanmode(withvalue:params:completion:).md)
- [func writeAttributeFanMode(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributefanmode(withvalue:params:completionhandler:).md)
- [func writeAttributeFanModeSequence(withValue: NSNumber, completion: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributefanmodesequence(withvalue:completion:).md)
- [func writeAttributeFanModeSequence(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributefanmodesequence(withvalue:completionhandler:).md)
- [func writeAttributeFanModeSequence(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributefanmodesequence(withvalue:params:completion:).md)
- [func writeAttributeFanModeSequence(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributefanmodesequence(withvalue:params:completionhandler:).md)
- [func writeAttributePercentSetting(withValue: NSNumber?, completion: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributepercentsetting(withvalue:completion:).md)
- [func writeAttributePercentSetting(withValue: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributepercentsetting(withvalue:completionhandler:).md)
- [func writeAttributePercentSetting(withValue: NSNumber?, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributepercentsetting(withvalue:params:completion:).md)
- [func writeAttributePercentSetting(withValue: NSNumber?, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributepercentsetting(withvalue:params:completionhandler:).md)
- [func writeAttributeRockSetting(withValue: NSNumber, completion: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributerocksetting(withvalue:completion:).md)
- [func writeAttributeRockSetting(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributerocksetting(withvalue:completionhandler:).md)
- [func writeAttributeRockSetting(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributerocksetting(withvalue:params:completion:).md)
- [func writeAttributeRockSetting(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributerocksetting(withvalue:params:completionhandler:).md)
- [func writeAttributeSpeedSetting(withValue: NSNumber?, completion: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributespeedsetting(withvalue:completion:).md)
- [func writeAttributeSpeedSetting(withValue: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributespeedsetting(withvalue:completionhandler:).md)
- [func writeAttributeSpeedSetting(withValue: NSNumber?, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributespeedsetting(withvalue:params:completion:).md)
- [func writeAttributeSpeedSetting(withValue: NSNumber?, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributespeedsetting(withvalue:params:completionhandler:).md)
- [func writeAttributeWindSetting(withValue: NSNumber, completion: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributewindsetting(withvalue:completion:).md)
- [func writeAttributeWindSetting(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributewindsetting(withvalue:completionhandler:).md)
- [func writeAttributeWindSetting(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributewindsetting(withvalue:params:completion:).md)
- [func writeAttributeWindSetting(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusterfancontrol/writeattributewindsetting(withvalue:params:completionhandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAirflowDirection(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributeairflowdirection(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFanMode(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributefanmode(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFanMode(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributefanmode(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFanModeSequence(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributefanmodesequence(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFanModeSequence(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributefanmodesequence(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePercentCurrent(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributepercentcurrent(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributePercentCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributepercentcurrent(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePercentSetting(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributepercentsetting(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributePercentSetting(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributepercentsetting(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeRockSetting(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributerocksetting(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeRockSetting(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributerocksetting(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeRockSupport(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributerocksupport(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeRockSupport(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributerocksupport(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSpeedCurrent(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributespeedcurrent(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeSpeedCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributespeedcurrent(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSpeedMax(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributespeedmax(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeSpeedMax(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributespeedmax(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSpeedSetting(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributespeedsetting(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeSpeedSetting(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributespeedsetting(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeWindSetting(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributewindsetting(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeWindSetting(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributewindsetting(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeWindSupport(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributewindsupport(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeWindSupport(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterfancontrol/readattributewindsupport(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterfancontrol)*