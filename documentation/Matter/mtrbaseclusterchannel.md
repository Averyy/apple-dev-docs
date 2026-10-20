# MTRBaseClusterChannel

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
class MTRBaseClusterChannel
```

```objc
@interface MTRBaseClusterChannel : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclusterchannel/init%28device,endpoint,queue%29.md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterchannel/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func change(with: MTRChannelClusterChangeChannelParams, completion: (MTRChannelClusterChangeChannelResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterchannel/change%28with,completion%29.md)
- [func change(with: MTRChannelClusterChangeChannelParams, completionHandler: (MTRChannelClusterChangeChannelResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterchannel/change%28with,completionhandler%29.md)
- [func changeByNumber(with: MTRChannelClusterChangeChannelByNumberParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterchannel/changebynumber%28with,completion%29.md)
- [func changeByNumber(with: MTRChannelClusterChangeChannelByNumberParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterchannel/changebynumber%28with,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributeattributelist%28completion%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeChannelList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributechannellist%28completion%29.md)
- [func readAttributeChannelList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributechannellist%28completionhandler%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributeclusterrevision%28completion%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeCurrentChannel(completion: (MTRChannelClusterChannelInfoStruct?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributecurrentchannel%28completion%29.md)
- [func readAttributeCurrentChannel(completionHandler: (MTRChannelClusterChannelInfo?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributecurrentchannel%28completionhandler%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributefeaturemap%28completion%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func readAttributeLineup(completion: (MTRChannelClusterLineupInfoStruct?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributelineup%28completion%29.md)
- [func readAttributeLineup(completionHandler: (MTRChannelClusterLineupInfo?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributelineup%28completionhandler%29.md)
- [func skip(with: MTRChannelClusterSkipChannelParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterchannel/skip%28with,completion%29.md)
- [func skip(with: MTRChannelClusterSkipChannelParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterchannel/skip%28with,completionhandler%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeChannelList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/subscribeattributechannellist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeChannelList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/subscribeattributechannellist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterchannel/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterchannel/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCurrentChannel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRChannelClusterChannelInfoStruct?, (any Error)?) -> Void)](./mtrbaseclusterchannel/subscribeattributecurrentchannel%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCurrentChannel(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRChannelClusterChannelInfo?, (any Error)?) -> Void)](./mtrbaseclusterchannel/subscribeattributecurrentchannel%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterchannel/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterchannel/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeLineup(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRChannelClusterLineupInfoStruct?, (any Error)?) -> Void)](./mtrbaseclusterchannel/subscribeattributelineup%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeLineup(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRChannelClusterLineupInfo?, (any Error)?) -> Void)](./mtrbaseclusterchannel/subscribeattributelineup%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func cancelRecordProgram(with: MTRChannelClusterCancelRecordProgramParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterchannel/cancelrecordprogram%28with,completion%29.md)
  Command CancelRecordProgram
- [func getProgramGuide(completion: (MTRChannelClusterProgramGuideResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterchannel/getprogramguide%28completion%29.md)
- [func getProgramGuide(with: MTRChannelClusterGetProgramGuideParams?, completion: (MTRChannelClusterProgramGuideResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterchannel/getprogramguide%28with,completion%29.md)
  Command GetProgramGuide
- [func recordProgram(with: MTRChannelClusterRecordProgramParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterchannel/recordprogram%28with,completion%29.md)
  Command RecordProgram
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeChannelList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributechannellist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeChannelList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributechannellist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCurrentChannel(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (MTRChannelClusterChannelInfo?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributecurrentchannel%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeCurrentChannel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRChannelClusterChannelInfoStruct?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributecurrentchannel%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeLineup(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (MTRChannelClusterLineupInfo?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributelineup%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeLineup(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRChannelClusterLineupInfoStruct?, (any Error)?) -> Void)](./mtrbaseclusterchannel/readattributelineup%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterchannel)*