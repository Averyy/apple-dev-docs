# MTRBaseClusterTimeSynchronization

**Framework**: Matter  
**Kind**: class  
**Role**: Class

Cluster Time Synchronization

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
class MTRBaseClusterTimeSynchronization
```

```objc
@interface MTRBaseClusterTimeSynchronization : MTRGenericBaseCluster
```

#### Overview

Accurate time is required for a number of reasons, including scheduling, display and validating security materials.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclustertimesynchronization/init%28device,endpointid,queue%29.md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributeattributelist%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributeclusterrevision%28completion%29.md)
- [func readAttributeDSTOffset(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributedstoffset%28completion%29.md)
- [func readAttributeDSTOffsetListMaxSize(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributedstoffsetlistmaxsize%28completion%29.md)
- [func readAttributeDefaultNTP(completion: (String?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributedefaultntp%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeGranularity(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributegranularity%28completion%29.md)
- [func readAttributeLocalTime(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributelocaltime%28completion%29.md)
- [func readAttributeNTPServerAvailable(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributentpserveravailable%28completion%29.md)
- [func readAttributeSupportsDNSResolve(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributesupportsdnsresolve%28completion%29.md)
- [func readAttributeTimeSource(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributetimesource%28completion%29.md)
- [func readAttributeTimeZone(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributetimezone%28completion%29.md)
- [func readAttributeTimeZoneDatabase(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributetimezonedatabase%28completion%29.md)
- [func readAttributeTimeZoneListMaxSize(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributetimezonelistmaxsize%28completion%29.md)
- [func readAttributeTrustedTimeSource(completion: (MTRTimeSynchronizationClusterTrustedTimeSourceStruct?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributetrustedtimesource%28completion%29.md)
- [func readAttributeUTCTime(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributeutctime%28completion%29.md)
- [func setDSTOffsetWith(MTRTimeSynchronizationClusterSetDSTOffsetParams, completion: ((any Error)?) -> Void)](./mtrbaseclustertimesynchronization/setdstoffsetwith%28_,completion%29.md)
  Command SetDSTOffset
- [func setDefaultNTPWith(MTRTimeSynchronizationClusterSetDefaultNTPParams, completion: ((any Error)?) -> Void)](./mtrbaseclustertimesynchronization/setdefaultntpwith%28_,completion%29.md)
  Command SetDefaultNTP
- [func setTimeZoneWith(MTRTimeSynchronizationClusterSetTimeZoneParams, completion: (MTRTimeSynchronizationClusterSetTimeZoneResponseParams?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/settimezonewith%28_,completion%29.md)
  Command SetTimeZone
- [func setTrustedTimeSourceWith(MTRTimeSynchronizationClusterSetTrustedTimeSourceParams, completion: ((any Error)?) -> Void)](./mtrbaseclustertimesynchronization/settrustedtimesourcewith%28_,completion%29.md)
  Command SetTrustedTimeSource
- [func setUTCTimeWith(MTRTimeSynchronizationClusterSetUTCTimeParams, completion: ((any Error)?) -> Void)](./mtrbaseclustertimesynchronization/setutctimewith%28_,completion%29.md)
  Command SetUTCTime
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeDSTOffset(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/subscribeattributedstoffset%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeDSTOffsetListMaxSize(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/subscribeattributedstoffsetlistmaxsize%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeDefaultNTP(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/subscribeattributedefaultntp%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGranularity(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/subscribeattributegranularity%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeLocalTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/subscribeattributelocaltime%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeNTPServerAvailable(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/subscribeattributentpserveravailable%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSupportsDNSResolve(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/subscribeattributesupportsdnsresolve%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTimeSource(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/subscribeattributetimesource%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTimeZone(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/subscribeattributetimezone%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTimeZoneDatabase(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/subscribeattributetimezonedatabase%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTimeZoneListMaxSize(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/subscribeattributetimezonelistmaxsize%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTrustedTimeSource(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRTimeSynchronizationClusterTrustedTimeSourceStruct?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/subscribeattributetrustedtimesource%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeUTCTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/subscribeattributeutctime%28with,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeDSTOffset(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributedstoffset%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeDSTOffsetListMaxSize(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributedstoffsetlistmaxsize%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeDefaultNTP(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributedefaultntp%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGranularity(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributegranularity%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeLocalTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributelocaltime%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeNTPServerAvailable(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributentpserveravailable%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSupportsDNSResolve(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributesupportsdnsresolve%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeTimeSource(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributetimesource%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeTimeZone(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributetimezone%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeTimeZoneDatabase(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributetimezonedatabase%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeTimeZoneListMaxSize(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributetimezonelistmaxsize%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeTrustedTimeSource(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRTimeSynchronizationClusterTrustedTimeSourceStruct?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributetrustedtimesource%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeUTCTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertimesynchronization/readattributeutctime%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustertimesynchronization)*