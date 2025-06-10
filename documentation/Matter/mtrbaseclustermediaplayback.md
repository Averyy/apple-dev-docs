# MTRBaseClusterMediaPlayback

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
class MTRBaseClusterMediaPlayback
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclustermediaplayback/init(device:endpoint:queue:).md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclustermediaplayback/init(device:endpointid:queue:).md)
### Instance Methods
- [func fastForward(completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/fastforward(completion:).md)
- [func fastForward(completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/fastforward(completionhandler:).md)
- [func fastForward(with: MTRMediaPlaybackClusterFastForwardParams?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/fastforward(with:completion:).md)
- [func fastForward(with: MTRMediaPlaybackClusterFastForwardParams?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/fastforward(with:completionhandler:).md)
- [func next(completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/next(completion:).md)
- [func next(completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/next(completionhandler:).md)
- [func next(with: MTRMediaPlaybackClusterNextParams?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/next(with:completion:).md)
- [func next(with: MTRMediaPlaybackClusterNextParams?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/next(with:completionhandler:).md)
- [func pause(completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/pause(completion:).md)
- [func pause(completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/pause(completionhandler:).md)
- [func pause(with: MTRMediaPlaybackClusterPauseParams?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/pause(with:completion:).md)
- [func pause(with: MTRMediaPlaybackClusterPauseParams?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/pause(with:completionhandler:).md)
- [func play(completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/play(completion:).md)
- [func play(completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/play(completionhandler:).md)
- [func play(with: MTRMediaPlaybackClusterPlayParams?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/play(with:completion:).md)
- [func play(with: MTRMediaPlaybackClusterPlayParams?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/play(with:completionhandler:).md)
- [func previous(completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/previous(completion:).md)
- [func previous(completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/previous(completionhandler:).md)
- [func previous(with: MTRMediaPlaybackClusterPreviousParams?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/previous(with:completion:).md)
- [func previous(with: MTRMediaPlaybackClusterPreviousParams?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/previous(with:completionhandler:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeattributelist(completion:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeattributelist(completionhandler:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeclusterrevision(completion:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeCurrentState(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributecurrentstate(completion:).md)
- [func readAttributeCurrentState(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributecurrentstate(completionhandler:).md)
- [func readAttributeDuration(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeduration(completion:).md)
- [func readAttributeDuration(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeduration(completionhandler:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributefeaturemap(completion:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributefeaturemap(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributegeneratedcommandlist(completionhandler:).md)
- [func readAttributePlaybackSpeed(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeplaybackspeed(completion:).md)
- [func readAttributePlaybackSpeed(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeplaybackspeed(completionhandler:).md)
- [func readAttributeSampledPosition(completion: (MTRMediaPlaybackClusterPlaybackPositionStruct?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributesampledposition(completion:).md)
- [func readAttributeSampledPosition(completionHandler: (MTRMediaPlaybackClusterPlaybackPosition?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributesampledposition(completionhandler:).md)
- [func readAttributeSeekRangeEnd(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeseekrangeend(completion:).md)
- [func readAttributeSeekRangeEnd(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeseekrangeend(completionhandler:).md)
- [func readAttributeSeekRangeStart(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeseekrangestart(completion:).md)
- [func readAttributeSeekRangeStart(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeseekrangestart(completionhandler:).md)
- [func readAttributeStartTime(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributestarttime(completion:).md)
- [func readAttributeStartTime(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributestarttime(completionhandler:).md)
- [func rewind(completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/rewind(completion:).md)
- [func rewind(completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/rewind(completionhandler:).md)
- [func rewind(with: MTRMediaPlaybackClusterRewindParams?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/rewind(with:completion:).md)
- [func rewind(with: MTRMediaPlaybackClusterRewindParams?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/rewind(with:completionhandler:).md)
- [func seek(with: MTRMediaPlaybackClusterSeekParams, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/seek(with:completion:).md)
- [func seek(with: MTRMediaPlaybackClusterSeekParams, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/seek(with:completionhandler:).md)
- [func skipBackward(with: MTRMediaPlaybackClusterSkipBackwardParams, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/skipbackward(with:completion:).md)
- [func skipBackward(with: MTRMediaPlaybackClusterSkipBackwardParams, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/skipbackward(with:completionhandler:).md)
- [func skipForward(with: MTRMediaPlaybackClusterSkipForwardParams, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/skipforward(with:completion:).md)
- [func skipForward(with: MTRMediaPlaybackClusterSkipForwardParams, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/skipforward(with:completionhandler:).md)
- [func startOver(completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/startover(completion:).md)
- [func startOver(completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/startover(completionhandler:).md)
- [func startOver(with: MTRMediaPlaybackClusterStartOverParams?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/startover(with:completion:).md)
- [func startOver(with: MTRMediaPlaybackClusterStartOverParams?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/startover(with:completionhandler:).md)
- [func stop(completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/stop(completion:).md)
- [func stop(completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/stop(completionhandler:).md)
- [func stop(with: MTRMediaPlaybackClusterStopParams?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/stop(with:completion:).md)
- [func stop(with: MTRMediaPlaybackClusterStopPlaybackParams?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/stop(with:completionhandler:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCurrentState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributecurrentstate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCurrentState(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributecurrentstate(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeDuration(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributeduration(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeDuration(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributeduration(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePlaybackSpeed(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributeplaybackspeed(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePlaybackSpeed(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributeplaybackspeed(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSampledPosition(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRMediaPlaybackClusterPlaybackPositionStruct?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributesampledposition(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSampledPosition(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRMediaPlaybackClusterPlaybackPosition?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributesampledposition(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSeekRangeEnd(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributeseekrangeend(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSeekRangeEnd(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributeseekrangeend(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSeekRangeStart(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributeseekrangestart(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSeekRangeStart(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributeseekrangestart(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeStartTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributestarttime(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeStartTime(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/subscribeattributestarttime(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func activateAudioTrack(with: MTRMediaPlaybackClusterActivateAudioTrackParams, completion: ((any Error)?) -> Void)](mtrbaseclustermediaplayback/activateaudiotrack(with:completion:).md)
  Command ActivateAudioTrack
- [func activateTextTrack(with: MTRMediaPlaybackClusterActivateTextTrackParams, completion: ((any Error)?) -> Void)](mtrbaseclustermediaplayback/activatetexttrack(with:completion:).md)
  Command ActivateTextTrack
- [func deactivateTextTrack(completion: ((any Error)?) -> Void)](mtrbaseclustermediaplayback/deactivatetexttrack(completion:).md)
- [func deactivateTextTrack(with: MTRMediaPlaybackClusterDeactivateTextTrackParams?, completion: ((any Error)?) -> Void)](mtrbaseclustermediaplayback/deactivatetexttrack(with:completion:).md)
  Command DeactivateTextTrack
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCurrentState(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributecurrentstate(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeCurrentState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributecurrentstate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeDuration(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeduration(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeDuration(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeduration(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePlaybackSpeed(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeplaybackspeed(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributePlaybackSpeed(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeplaybackspeed(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSampledPosition(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (MTRMediaPlaybackClusterPlaybackPosition?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributesampledposition(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeSampledPosition(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRMediaPlaybackClusterPlaybackPositionStruct?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributesampledposition(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSeekRangeEnd(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeseekrangeend(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeSeekRangeEnd(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeseekrangeend(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSeekRangeStart(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeseekrangestart(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeSeekRangeStart(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributeseekrangestart(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeStartTime(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributestarttime(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeStartTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermediaplayback/readattributestarttime(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustermediaplayback)*