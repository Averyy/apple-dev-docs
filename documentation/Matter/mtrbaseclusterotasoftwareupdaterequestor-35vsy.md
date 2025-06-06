# MTRBaseClusterOtaSoftwareUpdateRequestor

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
class MTRBaseClusterOtaSoftwareUpdateRequestor
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/init(device:endpoint:queue:).md)
### Instance Methods
- [func announceOtaProvider(with: MTROtaSoftwareUpdateRequestorClusterAnnounceOtaProviderParams, completionHandler: MTRStatusCompletion)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/announceotaprovider(with:completionhandler:).md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeattributelist(completionhandler:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeDefaultOtaProviders(with: MTRReadParams?, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributedefaultotaproviders(with:completionhandler:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributefeaturemap(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributegeneratedcommandlist(completionhandler:).md)
- [func readAttributeUpdatePossible(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeupdatepossible(completionhandler:).md)
- [func readAttributeUpdateState(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeupdatestate(completionhandler:).md)
- [func readAttributeUpdateStateProgress(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeupdatestateprogress(completionhandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeDefaultOtaProviders(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/subscribeattributedefaultotaproviders(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeUpdatePossible(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/subscribeattributeupdatepossible(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeUpdateState(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/subscribeattributeupdatestate(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeUpdateStateProgress(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/subscribeattributeupdatestateprogress(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func writeAttributeDefaultOtaProviders(withValue: [Any], completionHandler: MTRStatusCompletion)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/writeattributedefaultotaproviders(withvalue:completionhandler:).md)
- [func writeAttributeDefaultOtaProviders(withValue: [Any], params: MTRWriteParams?, completionHandler: MTRStatusCompletion)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/writeattributedefaultotaproviders(withvalue:params:completionhandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeDefaultOtaProviders(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributedefaultotaproviders(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeUpdatePossible(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeupdatepossible(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeUpdateState(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeupdatestate(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeUpdateStateProgress(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-35vsy/readattributeupdatestateprogress(withattributecache:endpoint:queue:completionhandler:).md)

## Relationships

### Inherits From
- [MTRBaseClusterOTASoftwareUpdateRequestor](mtrbaseclusterotasoftwareupdaterequestor-9n6nb.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterotasoftwareupdaterequestor-35vsy)*