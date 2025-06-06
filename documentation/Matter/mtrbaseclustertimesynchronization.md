# MTRBaseClusterTimeSynchronization

**Framework**: Matter  
**Kind**: class

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

#### Overview

Accurate time is required for a number of reasons, including scheduling, display and validating security materials.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclustertimesynchronization/init(device:endpointid:queue:).md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributeattributelist(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributeclusterrevision(completion:).md)
- [func readAttributeDSTOffset(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributedstoffset(completion:).md)
- [func readAttributeDSTOffsetListMaxSize(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributedstoffsetlistmaxsize(completion:).md)
- [func readAttributeDefaultNTP(completion: (String?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributedefaultntp(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeGranularity(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributegranularity(completion:).md)
- [func readAttributeLocalTime(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributelocaltime(completion:).md)
- [func readAttributeNTPServerAvailable(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributentpserveravailable(completion:).md)
- [func readAttributeSupportsDNSResolve(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributesupportsdnsresolve(completion:).md)
- [func readAttributeTimeSource(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributetimesource(completion:).md)
- [func readAttributeTimeZone(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributetimezone(completion:).md)
- [func readAttributeTimeZoneDatabase(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributetimezonedatabase(completion:).md)
- [func readAttributeTimeZoneListMaxSize(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributetimezonelistmaxsize(completion:).md)
- [func readAttributeTrustedTimeSource(completion: (MTRTimeSynchronizationClusterTrustedTimeSourceStruct?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributetrustedtimesource(completion:).md)
- [func readAttributeUTCTime(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributeutctime(completion:).md)
- [func setDSTOffsetWith(MTRTimeSynchronizationClusterSetDSTOffsetParams, completion: MTRStatusCompletion)](mtrbaseclustertimesynchronization/setdstoffsetwith(_:completion:).md)
  Command SetDSTOffset
- [func setDefaultNTPWith(MTRTimeSynchronizationClusterSetDefaultNTPParams, completion: MTRStatusCompletion)](mtrbaseclustertimesynchronization/setdefaultntpwith(_:completion:).md)
  Command SetDefaultNTP
- [func setTimeZoneWith(MTRTimeSynchronizationClusterSetTimeZoneParams, completion: (MTRTimeSynchronizationClusterSetTimeZoneResponseParams?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/settimezonewith(_:completion:).md)
  Command SetTimeZone
- [func setTrustedTimeSourceWith(MTRTimeSynchronizationClusterSetTrustedTimeSourceParams, completion: MTRStatusCompletion)](mtrbaseclustertimesynchronization/settrustedtimesourcewith(_:completion:).md)
  Command SetTrustedTimeSource
- [func setUTCTimeWith(MTRTimeSynchronizationClusterSetUTCTimeParams, completion: MTRStatusCompletion)](mtrbaseclustertimesynchronization/setutctimewith(_:completion:).md)
  Command SetUTCTime
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeDSTOffset(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/subscribeattributedstoffset(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeDSTOffsetListMaxSize(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/subscribeattributedstoffsetlistmaxsize(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeDefaultNTP(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/subscribeattributedefaultntp(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGranularity(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/subscribeattributegranularity(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLocalTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/subscribeattributelocaltime(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeNTPServerAvailable(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/subscribeattributentpserveravailable(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSupportsDNSResolve(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/subscribeattributesupportsdnsresolve(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTimeSource(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/subscribeattributetimesource(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTimeZone(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/subscribeattributetimezone(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTimeZoneDatabase(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/subscribeattributetimezonedatabase(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTimeZoneListMaxSize(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/subscribeattributetimezonelistmaxsize(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTrustedTimeSource(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRTimeSynchronizationClusterTrustedTimeSourceStruct?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/subscribeattributetrustedtimesource(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeUTCTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/subscribeattributeutctime(with:subscriptionestablished:reporthandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeDSTOffset(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributedstoffset(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeDSTOffsetListMaxSize(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributedstoffsetlistmaxsize(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeDefaultNTP(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributedefaultntp(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGranularity(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributegranularity(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeLocalTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributelocaltime(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeNTPServerAvailable(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributentpserveravailable(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSupportsDNSResolve(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributesupportsdnsresolve(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeTimeSource(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributetimesource(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeTimeZone(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributetimezone(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeTimeZoneDatabase(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributetimezonedatabase(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeTimeZoneListMaxSize(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributetimezonelistmaxsize(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeTrustedTimeSource(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRTimeSynchronizationClusterTrustedTimeSourceStruct?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributetrustedtimesource(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeUTCTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertimesynchronization/readattributeutctime(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustertimesynchronization)*