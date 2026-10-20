# MTRBaseClusterValveConfigurationAndControl

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRBaseClusterValveConfigurationAndControl : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclustervalveconfigurationandcontrol/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func close(completion: ((any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/close%28completion%29.md)
- [func close(with: MTRValveConfigurationAndControlClusterCloseParams?, completion: ((any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/close%28with,completion%29.md)
- [func open(completion: ((any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/open%28completion%29.md)
- [func open(with: MTRValveConfigurationAndControlClusterOpenParams?, completion: ((any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/open%28with,completion%29.md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributeattributelist%28completion%29.md)
- [func readAttributeAutoCloseTime(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributeautoclosetime%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributeclusterrevision%28completion%29.md)
- [func readAttributeCurrentLevel(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributecurrentlevel%28completion%29.md)
- [func readAttributeCurrentState(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributecurrentstate%28completion%29.md)
- [func readAttributeDefaultOpenDuration(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributedefaultopenduration%28completion%29.md)
- [func readAttributeDefaultOpenLevel(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributedefaultopenlevel%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeLevelStep(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributelevelstep%28completion%29.md)
- [func readAttributeOpenDuration(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributeopenduration%28completion%29.md)
- [func readAttributeRemainingDuration(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributeremainingduration%28completion%29.md)
- [func readAttributeTargetLevel(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributetargetlevel%28completion%29.md)
- [func readAttributeTargetState(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributetargetstate%28completion%29.md)
- [func readAttributeValveFault(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributevalvefault%28completion%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAutoCloseTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/subscribeattributeautoclosetime%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCurrentLevel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/subscribeattributecurrentlevel%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCurrentState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/subscribeattributecurrentstate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeDefaultOpenDuration(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/subscribeattributedefaultopenduration%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeDefaultOpenLevel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/subscribeattributedefaultopenlevel%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeLevelStep(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/subscribeattributelevelstep%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOpenDuration(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/subscribeattributeopenduration%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeRemainingDuration(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/subscribeattributeremainingduration%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTargetLevel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/subscribeattributetargetlevel%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTargetState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/subscribeattributetargetstate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeValveFault(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/subscribeattributevalvefault%28with,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeDefaultOpenDuration(withValue: NSNumber?, completion: ((any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/writeattributedefaultopenduration%28withvalue,completion%29.md)
- [func writeAttributeDefaultOpenDuration(withValue: NSNumber?, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/writeattributedefaultopenduration%28withvalue,params,completion%29.md)
- [func writeAttributeDefaultOpenLevel(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/writeattributedefaultopenlevel%28withvalue,completion%29.md)
- [func writeAttributeDefaultOpenLevel(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/writeattributedefaultopenlevel%28withvalue,params,completion%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAutoCloseTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributeautoclosetime%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCurrentLevel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributecurrentlevel%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCurrentState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributecurrentstate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeDefaultOpenDuration(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributedefaultopenduration%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeDefaultOpenLevel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributedefaultopenlevel%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeLevelStep(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributelevelstep%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeOpenDuration(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributeopenduration%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeRemainingDuration(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributeremainingduration%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeTargetLevel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributetargetlevel%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeTargetState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributetargetstate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeValveFault(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustervalveconfigurationandcontrol/readattributevalvefault%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustervalveconfigurationandcontrol)*