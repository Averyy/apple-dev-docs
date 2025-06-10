# MTRBaseClusterOnOff

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
class MTRBaseClusterOnOff
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclusteronoff/init(device:endpoint:queue:).md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusteronoff/init(device:endpointid:queue:).md)
### Instance Methods
- [func off(completion: ((any Error)?) -> Void)](mtrbaseclusteronoff/off(completion:).md)
- [func off(completionHandler: ((any Error)?) -> Void)](mtrbaseclusteronoff/off(completionhandler:).md)
- [func off(with: MTROnOffClusterOffParams?, completion: ((any Error)?) -> Void)](mtrbaseclusteronoff/off(with:completion:).md)
- [func off(with: MTROnOffClusterOffParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusteronoff/off(with:completionhandler:).md)
- [func offWithEffect(with: MTROnOffClusterOffWithEffectParams, completion: ((any Error)?) -> Void)](mtrbaseclusteronoff/offwitheffect(with:completion:).md)
- [func offWithEffect(with: MTROnOffClusterOffWithEffectParams, completionHandler: ((any Error)?) -> Void)](mtrbaseclusteronoff/offwitheffect(with:completionhandler:).md)
- [func on(completion: ((any Error)?) -> Void)](mtrbaseclusteronoff/on(completion:).md)
- [func on(completionHandler: ((any Error)?) -> Void)](mtrbaseclusteronoff/on(completionhandler:).md)
- [func on(with: MTROnOffClusterOnParams?, completion: ((any Error)?) -> Void)](mtrbaseclusteronoff/on(with:completion:).md)
- [func on(with: MTROnOffClusterOnParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusteronoff/on(with:completionhandler:).md)
- [func onWithRecallGlobalScene(completion: ((any Error)?) -> Void)](mtrbaseclusteronoff/onwithrecallglobalscene(completion:).md)
- [func onWithRecallGlobalScene(completionHandler: ((any Error)?) -> Void)](mtrbaseclusteronoff/onwithrecallglobalscene(completionhandler:).md)
- [func onWithRecallGlobalScene(with: MTROnOffClusterOnWithRecallGlobalSceneParams?, completion: ((any Error)?) -> Void)](mtrbaseclusteronoff/onwithrecallglobalscene(with:completion:).md)
- [func onWithRecallGlobalScene(with: MTROnOffClusterOnWithRecallGlobalSceneParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusteronoff/onwithrecallglobalscene(with:completionhandler:).md)
- [func onWithTimedOff(with: MTROnOffClusterOnWithTimedOffParams, completion: ((any Error)?) -> Void)](mtrbaseclusteronoff/onwithtimedoff(with:completion:).md)
- [func onWithTimedOff(with: MTROnOffClusterOnWithTimedOffParams, completionHandler: ((any Error)?) -> Void)](mtrbaseclusteronoff/onwithtimedoff(with:completionhandler:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeattributelist(completion:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeattributelist(completionhandler:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeclusterrevision(completion:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributefeaturemap(completion:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributefeaturemap(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributegeneratedcommandlist(completionhandler:).md)
- [func readAttributeGlobalSceneControl(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeglobalscenecontrol(completion:).md)
- [func readAttributeGlobalSceneControl(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeglobalscenecontrol(completionhandler:).md)
- [func readAttributeOffWaitTime(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeoffwaittime(completion:).md)
- [func readAttributeOffWaitTime(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeoffwaittime(completionhandler:).md)
- [func readAttributeOnOff(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeonoff(completion:).md)
- [func readAttributeOnOff(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeonoff(completionhandler:).md)
- [func readAttributeOnTime(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeontime(completion:).md)
- [func readAttributeOnTime(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeontime(completionhandler:).md)
- [func readAttributeStartUp(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributestartup(completion:).md)
- [func readAttributeStartUp(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributestartup(completionhandler:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGlobalSceneControl(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributeglobalscenecontrol(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGlobalSceneControl(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributeglobalscenecontrol(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOffWaitTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributeoffwaittime(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOffWaitTime(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributeoffwaittime(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOnOff(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributeonoff(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOnOff(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributeonoff(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOnTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributeontime(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOnTime(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributeontime(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeStartUp(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributestartup(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeStartUp(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/subscribeattributestartup(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func toggle(completion: ((any Error)?) -> Void)](mtrbaseclusteronoff/toggle(completion:).md)
- [func toggle(completionHandler: ((any Error)?) -> Void)](mtrbaseclusteronoff/toggle(completionhandler:).md)
- [func toggle(with: MTROnOffClusterToggleParams?, completion: ((any Error)?) -> Void)](mtrbaseclusteronoff/toggle(with:completion:).md)
- [func toggle(with: MTROnOffClusterToggleParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusteronoff/toggle(with:completionhandler:).md)
- [func writeAttributeOffWaitTime(withValue: NSNumber, completion: ((any Error)?) -> Void)](mtrbaseclusteronoff/writeattributeoffwaittime(withvalue:completion:).md)
- [func writeAttributeOffWaitTime(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](mtrbaseclusteronoff/writeattributeoffwaittime(withvalue:completionhandler:).md)
- [func writeAttributeOffWaitTime(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusteronoff/writeattributeoffwaittime(withvalue:params:completion:).md)
- [func writeAttributeOffWaitTime(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusteronoff/writeattributeoffwaittime(withvalue:params:completionhandler:).md)
- [func writeAttributeOnTime(withValue: NSNumber, completion: ((any Error)?) -> Void)](mtrbaseclusteronoff/writeattributeontime(withvalue:completion:).md)
- [func writeAttributeOnTime(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](mtrbaseclusteronoff/writeattributeontime(withvalue:completionhandler:).md)
- [func writeAttributeOnTime(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusteronoff/writeattributeontime(withvalue:params:completion:).md)
- [func writeAttributeOnTime(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusteronoff/writeattributeontime(withvalue:params:completionhandler:).md)
- [func writeAttributeStartUp(withValue: NSNumber?, completion: ((any Error)?) -> Void)](mtrbaseclusteronoff/writeattributestartup(withvalue:completion:).md)
- [func writeAttributeStartUp(withValue: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusteronoff/writeattributestartup(withvalue:completionhandler:).md)
- [func writeAttributeStartUp(withValue: NSNumber?, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusteronoff/writeattributestartup(withvalue:params:completion:).md)
- [func writeAttributeStartUp(withValue: NSNumber?, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusteronoff/writeattributestartup(withvalue:params:completionhandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGlobalSceneControl(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeglobalscenecontrol(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGlobalSceneControl(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeglobalscenecontrol(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeOffWaitTime(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeoffwaittime(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeOffWaitTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeoffwaittime(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeOnOff(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeonoff(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeOnOff(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeonoff(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeOnTime(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeontime(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeOnTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributeontime(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeStartUp(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributestartup(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeStartUp(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteronoff/readattributestartup(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteronoff)*