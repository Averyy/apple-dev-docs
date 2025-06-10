# MTRBaseClusterValveConfigurationAndControl

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
class MTRBaseClusterValveConfigurationAndControl
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclustervalveconfigurationandcontrol/init(device:endpointid:queue:).md)
### Instance Methods
- [func close(completion: ((any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/close(completion:).md)
- [func close(with: MTRValveConfigurationAndControlClusterCloseParams?, completion: ((any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/close(with:completion:).md)
- [func open(completion: ((any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/open(completion:).md)
- [func open(with: MTRValveConfigurationAndControlClusterOpenParams?, completion: ((any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/open(with:completion:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributeattributelist(completion:).md)
- [func readAttributeAutoCloseTime(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributeautoclosetime(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributeclusterrevision(completion:).md)
- [func readAttributeCurrentLevel(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributecurrentlevel(completion:).md)
- [func readAttributeCurrentState(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributecurrentstate(completion:).md)
- [func readAttributeDefaultOpenDuration(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributedefaultopenduration(completion:).md)
- [func readAttributeDefaultOpenLevel(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributedefaultopenlevel(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeLevelStep(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributelevelstep(completion:).md)
- [func readAttributeOpenDuration(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributeopenduration(completion:).md)
- [func readAttributeRemainingDuration(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributeremainingduration(completion:).md)
- [func readAttributeTargetLevel(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributetargetlevel(completion:).md)
- [func readAttributeTargetState(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributetargetstate(completion:).md)
- [func readAttributeValveFault(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributevalvefault(completion:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAutoCloseTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/subscribeattributeautoclosetime(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCurrentLevel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/subscribeattributecurrentlevel(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCurrentState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/subscribeattributecurrentstate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeDefaultOpenDuration(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/subscribeattributedefaultopenduration(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeDefaultOpenLevel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/subscribeattributedefaultopenlevel(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLevelStep(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/subscribeattributelevelstep(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOpenDuration(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/subscribeattributeopenduration(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeRemainingDuration(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/subscribeattributeremainingduration(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTargetLevel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/subscribeattributetargetlevel(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTargetState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/subscribeattributetargetstate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeValveFault(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/subscribeattributevalvefault(with:subscriptionestablished:reporthandler:).md)
- [func writeAttributeDefaultOpenDuration(withValue: NSNumber?, completion: ((any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/writeattributedefaultopenduration(withvalue:completion:).md)
- [func writeAttributeDefaultOpenDuration(withValue: NSNumber?, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/writeattributedefaultopenduration(withvalue:params:completion:).md)
- [func writeAttributeDefaultOpenLevel(withValue: NSNumber, completion: ((any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/writeattributedefaultopenlevel(withvalue:completion:).md)
- [func writeAttributeDefaultOpenLevel(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/writeattributedefaultopenlevel(withvalue:params:completion:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAutoCloseTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributeautoclosetime(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCurrentLevel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributecurrentlevel(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCurrentState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributecurrentstate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeDefaultOpenDuration(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributedefaultopenduration(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeDefaultOpenLevel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributedefaultopenlevel(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeLevelStep(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributelevelstep(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeOpenDuration(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributeopenduration(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeRemainingDuration(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributeremainingduration(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeTargetLevel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributetargetlevel(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeTargetState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributetargetstate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeValveFault(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustervalveconfigurationandcontrol/readattributevalvefault(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustervalveconfigurationandcontrol)*