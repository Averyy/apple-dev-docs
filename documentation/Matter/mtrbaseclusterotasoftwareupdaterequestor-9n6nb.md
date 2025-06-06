# MTRBaseClusterOTASoftwareUpdateRequestor

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
class MTRBaseClusterOTASoftwareUpdateRequestor
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/init(device:endpointid:queue:).md)
### Instance Methods
- [func announceOTAProvider(with: MTROTASoftwareUpdateRequestorClusterAnnounceOTAProviderParams, completion: MTRStatusCompletion)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/announceotaprovider(with:completion:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeattributelist(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeclusterrevision(completion:).md)
- [func readAttributeDefaultOTAProviders(with: MTRReadParams?, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributedefaultotaproviders(with:completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeUpdatePossible(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeupdatepossible(completion:).md)
- [func readAttributeUpdateState(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeupdatestate(completion:).md)
- [func readAttributeUpdateStateProgress(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeupdatestateprogress(completion:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeDefaultOTAProviders(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/subscribeattributedefaultotaproviders(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeUpdatePossible(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/subscribeattributeupdatepossible(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeUpdateState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/subscribeattributeupdatestate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeUpdateStateProgress(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/subscribeattributeupdatestateprogress(with:subscriptionestablished:reporthandler:).md)
- [func writeAttributeDefaultOTAProviders(withValue: [Any], completion: MTRStatusCompletion)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/writeattributedefaultotaproviders(withvalue:completion:).md)
- [func writeAttributeDefaultOTAProviders(withValue: [Any], params: MTRWriteParams?, completion: MTRStatusCompletion)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/writeattributedefaultotaproviders(withvalue:params:completion:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeDefaultOTAProviders(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributedefaultotaproviders(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeUpdatePossible(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeupdatepossible(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeUpdateState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeupdatestate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeUpdateStateProgress(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeupdatestateprogress(withclusterstatecache:endpoint:queue:completion:).md)

## Relationships

### Inherits From
- [MTRGenericBaseCluster](mtrgenericbasecluster.md)
### Inherited By
- [MTRBaseClusterOtaSoftwareUpdateRequestor](mtrbaseclusterotasoftwareupdaterequestor-35vsy.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterotasoftwareupdaterequestor-9n6nb)*