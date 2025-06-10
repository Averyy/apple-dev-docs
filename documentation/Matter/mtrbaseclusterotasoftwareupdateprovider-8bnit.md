# MTRBaseClusterOTASoftwareUpdateProvider

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
class MTRBaseClusterOTASoftwareUpdateProvider
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterotasoftwareupdateprovider-8bnit/init(device:endpointid:queue:).md)
### Instance Methods
- [func applyUpdateRequest(with: MTROTASoftwareUpdateProviderClusterApplyUpdateRequestParams, completion: (MTROTASoftwareUpdateProviderClusterApplyUpdateResponseParams?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdateprovider-8bnit/applyupdaterequest(with:completion:).md)
- [func notifyUpdateApplied(with: MTROTASoftwareUpdateProviderClusterNotifyUpdateAppliedParams, completion: ((any Error)?) -> Void)](mtrbaseclusterotasoftwareupdateprovider-8bnit/notifyupdateapplied(with:completion:).md)
- [func queryImage(with: MTROTASoftwareUpdateProviderClusterQueryImageParams, completion: (MTROTASoftwareUpdateProviderClusterQueryImageResponseParams?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdateprovider-8bnit/queryimage(with:completion:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdateprovider-8bnit/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdateprovider-8bnit/readattributeattributelist(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdateprovider-8bnit/readattributeclusterrevision(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdateprovider-8bnit/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdateprovider-8bnit/readattributegeneratedcommandlist(completion:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdateprovider-8bnit/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdateprovider-8bnit/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdateprovider-8bnit/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdateprovider-8bnit/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdateprovider-8bnit/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdateprovider-8bnit/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdateprovider-8bnit/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdateprovider-8bnit/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdateprovider-8bnit/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterotasoftwareupdateprovider-8bnit/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)

## Relationships

### Inherits From
- [MTRGenericBaseCluster](mtrgenericbasecluster.md)
### Inherited By
- [MTRBaseClusterOtaSoftwareUpdateProvider](mtrbaseclusterotasoftwareupdateprovider-2vync.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterotasoftwareupdateprovider-8bnit)*