# MTRBaseClusterOtaSoftwareUpdateRequestor

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use MTRBaseClusterOTASoftwareUpdateRequestor

## Declaration

```swift
class MTRBaseClusterOtaSoftwareUpdateRequestor
```

```objc
@interface MTRBaseClusterOtaSoftwareUpdateRequestor : MTRBaseClusterOTASoftwareUpdateRequestor
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/init%28device,endpoint,queue%29.md)
### Instance Methods
- [func announceOtaProvider(with: MTROtaSoftwareUpdateRequestorClusterAnnounceOtaProviderParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/announceotaprovider%28with,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeDefaultOtaProviders(with: MTRReadParams?, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributedefaultotaproviders%28with,completionhandler%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func readAttributeUpdatePossible(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeupdatepossible%28completionhandler%29.md)
- [func readAttributeUpdateState(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeupdatestate%28completionhandler%29.md)
- [func readAttributeUpdateStateProgress(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeupdatestateprogress%28completionhandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeDefaultOtaProviders(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/subscribeattributedefaultotaproviders%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeUpdatePossible(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/subscribeattributeupdatepossible%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeUpdateState(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/subscribeattributeupdatestate%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeUpdateStateProgress(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/subscribeattributeupdatestateprogress%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeDefaultOtaProviders(withValue: [Any], completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/writeattributedefaultotaproviders%28withvalue,completionhandler%29.md)
- [func writeAttributeDefaultOtaProviders(withValue: [Any], params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/writeattributedefaultotaproviders%28withvalue,params,completionhandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeDefaultOtaProviders(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributedefaultotaproviders%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeUpdatePossible(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeupdatepossible%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeUpdateState(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeupdatestate%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeUpdateStateProgress(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeupdatestateprogress%28withattributecache,endpoint,queue,completionhandler%29.md)

## Relationships

### Inherits From
- [MTRBaseClusterOTASoftwareUpdateRequestor](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterotasoftwareupdaterequestor-35vsy)*