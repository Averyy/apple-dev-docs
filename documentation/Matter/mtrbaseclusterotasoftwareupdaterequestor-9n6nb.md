# MTRBaseClusterOTASoftwareUpdateRequestor

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRBaseClusterOTASoftwareUpdateRequestor : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func announceOTAProvider(with: MTROTASoftwareUpdateRequestorClusterAnnounceOTAProviderParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/announceotaprovider%28with,completion%29.md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeattributelist%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeclusterrevision%28completion%29.md)
- [func readAttributeDefaultOTAProviders(with: MTRReadParams?, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributedefaultotaproviders%28with,completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeUpdatePossible(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeupdatepossible%28completion%29.md)
- [func readAttributeUpdateState(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeupdatestate%28completion%29.md)
- [func readAttributeUpdateStateProgress(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeupdatestateprogress%28completion%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeDefaultOTAProviders(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/subscribeattributedefaultotaproviders%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeUpdatePossible(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/subscribeattributeupdatepossible%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeUpdateState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/subscribeattributeupdatestate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeUpdateStateProgress(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/subscribeattributeupdatestateprogress%28with,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeDefaultOTAProviders(withValue: [Any], completion: ((any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/writeattributedefaultotaproviders%28withvalue,completion%29.md)
- [func writeAttributeDefaultOTAProviders(withValue: [Any], params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/writeattributedefaultotaproviders%28withvalue,params,completion%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeDefaultOTAProviders(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributedefaultotaproviders%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeUpdatePossible(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeupdatepossible%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeUpdateState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeupdatestate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeUpdateStateProgress(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributeupdatestateprogress%28withclusterstatecache,endpoint,queue,completion%29.md)

## Relationships

### Inherits From
- [MTRGenericBaseCluster](./mtrgenericbasecluster.md)
### Inherited By
- [MTRBaseClusterOtaSoftwareUpdateRequestor](./mtrbaseclusterotasoftwareupdaterequestor-35vsy.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterotasoftwareupdaterequestor-9n6nb)*