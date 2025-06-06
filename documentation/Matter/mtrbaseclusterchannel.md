# MTRBaseClusterChannel

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
class MTRBaseClusterChannel
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclusterchannel/init(device:endpoint:queue:).md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterchannel/init(device:endpointid:queue:).md)
### Instance Methods
- [func change(with: MTRChannelClusterChangeChannelParams, completion: (MTRChannelClusterChangeChannelResponseParams?, (any Error)?) -> Void)](mtrbaseclusterchannel/change(with:completion:).md)
- [func change(with: MTRChannelClusterChangeChannelParams, completionHandler: (MTRChannelClusterChangeChannelResponseParams?, (any Error)?) -> Void)](mtrbaseclusterchannel/change(with:completionhandler:).md)
- [func changeByNumber(with: MTRChannelClusterChangeChannelByNumberParams, completion: MTRStatusCompletion)](mtrbaseclusterchannel/changebynumber(with:completion:).md)
- [func changeByNumber(with: MTRChannelClusterChangeChannelByNumberParams, completionHandler: MTRStatusCompletion)](mtrbaseclusterchannel/changebynumber(with:completionhandler:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributeattributelist(completion:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributeattributelist(completionhandler:).md)
- [func readAttributeChannelList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributechannellist(completion:).md)
- [func readAttributeChannelList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributechannellist(completionhandler:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributeclusterrevision(completion:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeCurrentChannel(completion: (MTRChannelClusterChannelInfoStruct?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributecurrentchannel(completion:).md)
- [func readAttributeCurrentChannel(completionHandler: (MTRChannelClusterChannelInfo?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributecurrentchannel(completionhandler:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributefeaturemap(completion:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributefeaturemap(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributegeneratedcommandlist(completionhandler:).md)
- [func readAttributeLineup(completion: (MTRChannelClusterLineupInfoStruct?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributelineup(completion:).md)
- [func readAttributeLineup(completionHandler: (MTRChannelClusterLineupInfo?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributelineup(completionhandler:).md)
- [func skip(with: MTRChannelClusterSkipChannelParams, completion: MTRStatusCompletion)](mtrbaseclusterchannel/skip(with:completion:).md)
- [func skip(with: MTRChannelClusterSkipChannelParams, completionHandler: MTRStatusCompletion)](mtrbaseclusterchannel/skip(with:completionhandler:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeChannelList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/subscribeattributechannellist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeChannelList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/subscribeattributechannellist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterchannel/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterchannel/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCurrentChannel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRChannelClusterChannelInfoStruct?, (any Error)?) -> Void)](mtrbaseclusterchannel/subscribeattributecurrentchannel(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCurrentChannel(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRChannelClusterChannelInfo?, (any Error)?) -> Void)](mtrbaseclusterchannel/subscribeattributecurrentchannel(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterchannel/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterchannel/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLineup(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRChannelClusterLineupInfoStruct?, (any Error)?) -> Void)](mtrbaseclusterchannel/subscribeattributelineup(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLineup(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRChannelClusterLineupInfo?, (any Error)?) -> Void)](mtrbaseclusterchannel/subscribeattributelineup(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func cancelRecordProgram(with: MTRChannelClusterCancelRecordProgramParams, completion: MTRStatusCompletion)](mtrbaseclusterchannel/cancelrecordprogram(with:completion:).md)
  Command CancelRecordProgram
- [func getProgramGuide(completion: (MTRChannelClusterProgramGuideResponseParams?, (any Error)?) -> Void)](mtrbaseclusterchannel/getprogramguide(completion:).md)
- [func getProgramGuide(with: MTRChannelClusterGetProgramGuideParams?, completion: (MTRChannelClusterProgramGuideResponseParams?, (any Error)?) -> Void)](mtrbaseclusterchannel/getprogramguide(with:completion:).md)
  Command GetProgramGuide
- [func recordProgram(with: MTRChannelClusterRecordProgramParams, completion: MTRStatusCompletion)](mtrbaseclusterchannel/recordprogram(with:completion:).md)
  Command RecordProgram
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeChannelList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributechannellist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeChannelList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributechannellist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCurrentChannel(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (MTRChannelClusterChannelInfo?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributecurrentchannel(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeCurrentChannel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRChannelClusterChannelInfoStruct?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributecurrentchannel(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeLineup(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (MTRChannelClusterLineupInfo?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributelineup(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeLineup(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRChannelClusterLineupInfoStruct?, (any Error)?) -> Void)](mtrbaseclusterchannel/readattributelineup(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterchannel)*