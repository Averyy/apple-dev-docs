# MTRBaseClusterMediaPlayback

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
class MTRBaseClusterMediaPlayback
```

```objc
@interface MTRBaseClusterMediaPlayback : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclustermediaplayback/init%28device,endpoint,queue%29.md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclustermediaplayback/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func fastForward(completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/fastforward%28completion%29.md)
- [func fastForward(completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/fastforward%28completionhandler%29.md)
- [func fastForward(with: MTRMediaPlaybackClusterFastForwardParams?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/fastforward%28with,completion%29.md)
- [func fastForward(with: MTRMediaPlaybackClusterFastForwardParams?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/fastforward%28with,completionhandler%29.md)
- [func next(completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/next%28completion%29.md)
- [func next(completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/next%28completionhandler%29.md)
- [func next(with: MTRMediaPlaybackClusterNextParams?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/next%28with,completion%29.md)
- [func next(with: MTRMediaPlaybackClusterNextParams?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/next%28with,completionhandler%29.md)
- [func pause(completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/pause%28completion%29.md)
- [func pause(completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/pause%28completionhandler%29.md)
- [func pause(with: MTRMediaPlaybackClusterPauseParams?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/pause%28with,completion%29.md)
- [func pause(with: MTRMediaPlaybackClusterPauseParams?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/pause%28with,completionhandler%29.md)
- [func play(completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/play%28completion%29.md)
- [func play(completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/play%28completionhandler%29.md)
- [func play(with: MTRMediaPlaybackClusterPlayParams?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/play%28with,completion%29.md)
- [func play(with: MTRMediaPlaybackClusterPlayParams?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/play%28with,completionhandler%29.md)
- [func previous(completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/previous%28completion%29.md)
- [func previous(completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/previous%28completionhandler%29.md)
- [func previous(with: MTRMediaPlaybackClusterPreviousParams?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/previous%28with,completion%29.md)
- [func previous(with: MTRMediaPlaybackClusterPreviousParams?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/previous%28with,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeattributelist%28completion%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeclusterrevision%28completion%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeCurrentState(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributecurrentstate%28completion%29.md)
- [func readAttributeCurrentState(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributecurrentstate%28completionhandler%29.md)
- [func readAttributeDuration(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeduration%28completion%29.md)
- [func readAttributeDuration(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeduration%28completionhandler%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributefeaturemap%28completion%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func readAttributePlaybackSpeed(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeplaybackspeed%28completion%29.md)
- [func readAttributePlaybackSpeed(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeplaybackspeed%28completionhandler%29.md)
- [func readAttributeSampledPosition(completion: (MTRMediaPlaybackClusterPlaybackPositionStruct?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributesampledposition%28completion%29.md)
- [func readAttributeSampledPosition(completionHandler: (MTRMediaPlaybackClusterPlaybackPosition?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributesampledposition%28completionhandler%29.md)
- [func readAttributeSeekRangeEnd(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeseekrangeend%28completion%29.md)
- [func readAttributeSeekRangeEnd(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeseekrangeend%28completionhandler%29.md)
- [func readAttributeSeekRangeStart(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeseekrangestart%28completion%29.md)
- [func readAttributeSeekRangeStart(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeseekrangestart%28completionhandler%29.md)
- [func readAttributeStartTime(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributestarttime%28completion%29.md)
- [func readAttributeStartTime(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributestarttime%28completionhandler%29.md)
- [func rewind(completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/rewind%28completion%29.md)
- [func rewind(completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/rewind%28completionhandler%29.md)
- [func rewind(with: MTRMediaPlaybackClusterRewindParams?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/rewind%28with,completion%29.md)
- [func rewind(with: MTRMediaPlaybackClusterRewindParams?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/rewind%28with,completionhandler%29.md)
- [func seek(with: MTRMediaPlaybackClusterSeekParams, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/seek%28with,completion%29.md)
- [func seek(with: MTRMediaPlaybackClusterSeekParams, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/seek%28with,completionhandler%29.md)
- [func skipBackward(with: MTRMediaPlaybackClusterSkipBackwardParams, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/skipbackward%28with,completion%29.md)
- [func skipBackward(with: MTRMediaPlaybackClusterSkipBackwardParams, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/skipbackward%28with,completionhandler%29.md)
- [func skipForward(with: MTRMediaPlaybackClusterSkipForwardParams, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/skipforward%28with,completion%29.md)
- [func skipForward(with: MTRMediaPlaybackClusterSkipForwardParams, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/skipforward%28with,completionhandler%29.md)
- [func startOver(completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/startover%28completion%29.md)
- [func startOver(completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/startover%28completionhandler%29.md)
- [func startOver(with: MTRMediaPlaybackClusterStartOverParams?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/startover%28with,completion%29.md)
- [func startOver(with: MTRMediaPlaybackClusterStartOverParams?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/startover%28with,completionhandler%29.md)
- [func stop(completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/stop%28completion%29.md)
- [func stop(completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/stop%28completionhandler%29.md)
- [func stop(with: MTRMediaPlaybackClusterStopParams?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/stop%28with,completion%29.md)
- [func stop(with: MTRMediaPlaybackClusterStopPlaybackParams?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/stop%28with,completionhandler%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCurrentState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributecurrentstate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCurrentState(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributecurrentstate%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeDuration(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributeduration%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeDuration(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributeduration%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePlaybackSpeed(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributeplaybackspeed%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePlaybackSpeed(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributeplaybackspeed%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSampledPosition(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRMediaPlaybackClusterPlaybackPositionStruct?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributesampledposition%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSampledPosition(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRMediaPlaybackClusterPlaybackPosition?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributesampledposition%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSeekRangeEnd(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributeseekrangeend%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSeekRangeEnd(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributeseekrangeend%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSeekRangeStart(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributeseekrangestart%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSeekRangeStart(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributeseekrangestart%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeStartTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributestarttime%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeStartTime(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/subscribeattributestarttime%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func activateAudioTrack(with: MTRMediaPlaybackClusterActivateAudioTrackParams, completion: ((any Error)?) -> Void)](./mtrbaseclustermediaplayback/activateaudiotrack%28with,completion%29.md)
  Command ActivateAudioTrack
- [func activateTextTrack(with: MTRMediaPlaybackClusterActivateTextTrackParams, completion: ((any Error)?) -> Void)](./mtrbaseclustermediaplayback/activatetexttrack%28with,completion%29.md)
  Command ActivateTextTrack
- [func deactivateTextTrack(completion: ((any Error)?) -> Void)](./mtrbaseclustermediaplayback/deactivatetexttrack%28completion%29.md)
- [func deactivateTextTrack(with: MTRMediaPlaybackClusterDeactivateTextTrackParams?, completion: ((any Error)?) -> Void)](./mtrbaseclustermediaplayback/deactivatetexttrack%28with,completion%29.md)
  Command DeactivateTextTrack
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCurrentState(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributecurrentstate%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeCurrentState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributecurrentstate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeDuration(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeduration%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeDuration(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeduration%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePlaybackSpeed(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeplaybackspeed%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributePlaybackSpeed(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeplaybackspeed%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSampledPosition(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (MTRMediaPlaybackClusterPlaybackPosition?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributesampledposition%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeSampledPosition(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRMediaPlaybackClusterPlaybackPositionStruct?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributesampledposition%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSeekRangeEnd(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeseekrangeend%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeSeekRangeEnd(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeseekrangeend%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSeekRangeStart(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeseekrangestart%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeSeekRangeStart(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributeseekrangestart%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeStartTime(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributestarttime%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeStartTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermediaplayback/readattributestarttime%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustermediaplayback)*