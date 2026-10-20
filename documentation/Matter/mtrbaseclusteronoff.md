# MTRBaseClusterOnOff

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
class MTRBaseClusterOnOff
```

```objc
@interface MTRBaseClusterOnOff : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclusteronoff/init%28device,endpoint,queue%29.md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusteronoff/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func off(completion: ((any Error)?) -> Void)](./mtrbaseclusteronoff/off%28completion%29.md)
- [func off(completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteronoff/off%28completionhandler%29.md)
- [func off(with: MTROnOffClusterOffParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusteronoff/off%28with,completion%29.md)
- [func off(with: MTROnOffClusterOffParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteronoff/off%28with,completionhandler%29.md)
- [func offWithEffect(with: MTROnOffClusterOffWithEffectParams, completion: ((any Error)?) -> Void)](./mtrbaseclusteronoff/offwitheffect%28with,completion%29.md)
- [func offWithEffect(with: MTROnOffClusterOffWithEffectParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteronoff/offwitheffect%28with,completionhandler%29.md)
- [func on(completion: ((any Error)?) -> Void)](./mtrbaseclusteronoff/on%28completion%29.md)
- [func on(completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteronoff/on%28completionhandler%29.md)
- [func on(with: MTROnOffClusterOnParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusteronoff/on%28with,completion%29.md)
- [func on(with: MTROnOffClusterOnParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteronoff/on%28with,completionhandler%29.md)
- [func onWithRecallGlobalScene(completion: ((any Error)?) -> Void)](./mtrbaseclusteronoff/onwithrecallglobalscene%28completion%29.md)
- [func onWithRecallGlobalScene(completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteronoff/onwithrecallglobalscene%28completionhandler%29.md)
- [func onWithRecallGlobalScene(with: MTROnOffClusterOnWithRecallGlobalSceneParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusteronoff/onwithrecallglobalscene%28with,completion%29.md)
- [func onWithRecallGlobalScene(with: MTROnOffClusterOnWithRecallGlobalSceneParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteronoff/onwithrecallglobalscene%28with,completionhandler%29.md)
- [func onWithTimedOff(with: MTROnOffClusterOnWithTimedOffParams, completion: ((any Error)?) -> Void)](./mtrbaseclusteronoff/onwithtimedoff%28with,completion%29.md)
- [func onWithTimedOff(with: MTROnOffClusterOnWithTimedOffParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteronoff/onwithtimedoff%28with,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeattributelist%28completion%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeclusterrevision%28completion%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributefeaturemap%28completion%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func readAttributeGlobalSceneControl(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeglobalscenecontrol%28completion%29.md)
- [func readAttributeGlobalSceneControl(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeglobalscenecontrol%28completionhandler%29.md)
- [func readAttributeOffWaitTime(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeoffwaittime%28completion%29.md)
- [func readAttributeOffWaitTime(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeoffwaittime%28completionhandler%29.md)
- [func readAttributeOnOff(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeonoff%28completion%29.md)
- [func readAttributeOnOff(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeonoff%28completionhandler%29.md)
- [func readAttributeOnTime(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeontime%28completion%29.md)
- [func readAttributeOnTime(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeontime%28completionhandler%29.md)
- [func readAttributeStartUp(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributestartup%28completion%29.md)
- [func readAttributeStartUp(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributestartup%28completionhandler%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGlobalSceneControl(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributeglobalscenecontrol%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGlobalSceneControl(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributeglobalscenecontrol%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOffWaitTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributeoffwaittime%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOffWaitTime(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributeoffwaittime%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOnOff(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributeonoff%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOnOff(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributeonoff%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOnTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributeontime%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOnTime(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributeontime%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeStartUp(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributestartup%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeStartUp(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/subscribeattributestartup%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func toggle(completion: ((any Error)?) -> Void)](./mtrbaseclusteronoff/toggle%28completion%29.md)
- [func toggle(completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteronoff/toggle%28completionhandler%29.md)
- [func toggle(with: MTROnOffClusterToggleParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusteronoff/toggle%28with,completion%29.md)
- [func toggle(with: MTROnOffClusterToggleParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteronoff/toggle%28with,completionhandler%29.md)
- [func writeAttributeOffWaitTime(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusteronoff/writeattributeoffwaittime%28withvalue,completion%29.md)
- [func writeAttributeOffWaitTime(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteronoff/writeattributeoffwaittime%28withvalue,completionhandler%29.md)
- [func writeAttributeOffWaitTime(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusteronoff/writeattributeoffwaittime%28withvalue,params,completion%29.md)
- [func writeAttributeOffWaitTime(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteronoff/writeattributeoffwaittime%28withvalue,params,completionhandler%29.md)
- [func writeAttributeOnTime(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusteronoff/writeattributeontime%28withvalue,completion%29.md)
- [func writeAttributeOnTime(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteronoff/writeattributeontime%28withvalue,completionhandler%29.md)
- [func writeAttributeOnTime(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusteronoff/writeattributeontime%28withvalue,params,completion%29.md)
- [func writeAttributeOnTime(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteronoff/writeattributeontime%28withvalue,params,completionhandler%29.md)
- [func writeAttributeStartUp(withValue: NSNumber?, completion: ((any Error)?) -> Void)](./mtrbaseclusteronoff/writeattributestartup%28withvalue,completion%29.md)
- [func writeAttributeStartUp(withValue: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteronoff/writeattributestartup%28withvalue,completionhandler%29.md)
- [func writeAttributeStartUp(withValue: NSNumber?, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusteronoff/writeattributestartup%28withvalue,params,completion%29.md)
- [func writeAttributeStartUp(withValue: NSNumber?, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteronoff/writeattributestartup%28withvalue,params,completionhandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGlobalSceneControl(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeglobalscenecontrol%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGlobalSceneControl(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeglobalscenecontrol%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeOffWaitTime(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeoffwaittime%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeOffWaitTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeoffwaittime%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeOnOff(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeonoff%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeOnOff(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeonoff%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeOnTime(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeontime%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeOnTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributeontime%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeStartUp(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributestartup%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeStartUp(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteronoff/readattributestartup%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteronoff)*