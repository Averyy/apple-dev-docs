# MTRBaseClusterOperationalCredentials

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
class MTRBaseClusterOperationalCredentials
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclusteroperationalcredentials/init(device:endpoint:queue:).md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusteroperationalcredentials/init(device:endpointid:queue:).md)
### Instance Methods
- [func addNOC(with: MTROperationalCredentialsClusterAddNOCParams, completion: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/addnoc(with:completion:).md)
- [func addNOC(with: MTROperationalCredentialsClusterAddNOCParams, completionHandler: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/addnoc(with:completionhandler:).md)
- [func addTrustedRootCertificate(with: MTROperationalCredentialsClusterAddTrustedRootCertificateParams, completion: ((any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/addtrustedrootcertificate(with:completion:).md)
- [func addTrustedRootCertificate(with: MTROperationalCredentialsClusterAddTrustedRootCertificateParams, completionHandler: ((any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/addtrustedrootcertificate(with:completionhandler:).md)
- [func attestationRequest(with: MTROperationalCredentialsClusterAttestationRequestParams, completion: (MTROperationalCredentialsClusterAttestationResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/attestationrequest(with:completion:).md)
- [func attestationRequest(with: MTROperationalCredentialsClusterAttestationRequestParams, completionHandler: (MTROperationalCredentialsClusterAttestationResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/attestationrequest(with:completionhandler:).md)
- [func certificateChainRequest(with: MTROperationalCredentialsClusterCertificateChainRequestParams, completion: (MTROperationalCredentialsClusterCertificateChainResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/certificatechainrequest(with:completion:).md)
- [func certificateChainRequest(with: MTROperationalCredentialsClusterCertificateChainRequestParams, completionHandler: (MTROperationalCredentialsClusterCertificateChainResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/certificatechainrequest(with:completionhandler:).md)
- [func csrRequest(with: MTROperationalCredentialsClusterCSRRequestParams, completion: (MTROperationalCredentialsClusterCSRResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/csrrequest(with:completion:).md)
- [func csrRequest(with: MTROperationalCredentialsClusterCSRRequestParams, completionHandler: (MTROperationalCredentialsClusterCSRResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/csrrequest(with:completionhandler:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributeattributelist(completion:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributeattributelist(completionhandler:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributeclusterrevision(completion:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeCommissionedFabrics(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributecommissionedfabrics(completion:).md)
- [func readAttributeCommissionedFabrics(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributecommissionedfabrics(completionhandler:).md)
- [func readAttributeCurrentFabricIndex(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributecurrentfabricindex(completion:).md)
- [func readAttributeCurrentFabricIndex(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributecurrentfabricindex(completionhandler:).md)
- [func readAttributeFabrics(with: MTRReadParams?, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributefabrics(with:completion:).md)
- [func readAttributeFabrics(with: MTRReadParams?, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributefabrics(with:completionhandler:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributefeaturemap(completion:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributefeaturemap(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributegeneratedcommandlist(completionhandler:).md)
- [func readAttributeNOCs(with: MTRReadParams?, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributenocs(with:completion:).md)
- [func readAttributeNOCs(with: MTRReadParams?, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributenocs(with:completionhandler:).md)
- [func readAttributeSupportedFabrics(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributesupportedfabrics(completion:).md)
- [func readAttributeSupportedFabrics(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributesupportedfabrics(completionhandler:).md)
- [func readAttributeTrustedRootCertificates(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributetrustedrootcertificates(completion:).md)
- [func readAttributeTrustedRootCertificates(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributetrustedrootcertificates(completionhandler:).md)
- [func removeFabric(with: MTROperationalCredentialsClusterRemoveFabricParams, completion: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/removefabric(with:completion:).md)
- [func removeFabric(with: MTROperationalCredentialsClusterRemoveFabricParams, completionHandler: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/removefabric(with:completionhandler:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCommissionedFabrics(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributecommissionedfabrics(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCommissionedFabrics(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributecommissionedfabrics(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCurrentFabricIndex(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributecurrentfabricindex(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCurrentFabricIndex(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributecurrentfabricindex(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFabrics(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributefabrics(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFabrics(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributefabrics(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeNOCs(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributenocs(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeNOCs(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributenocs(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSupportedFabrics(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributesupportedfabrics(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSupportedFabrics(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributesupportedfabrics(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTrustedRootCertificates(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributetrustedrootcertificates(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTrustedRootCertificates(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/subscribeattributetrustedrootcertificates(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func updateFabricLabel(with: MTROperationalCredentialsClusterUpdateFabricLabelParams, completion: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/updatefabriclabel(with:completion:).md)
- [func updateFabricLabel(with: MTROperationalCredentialsClusterUpdateFabricLabelParams, completionHandler: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/updatefabriclabel(with:completionhandler:).md)
- [func updateNOC(with: MTROperationalCredentialsClusterUpdateNOCParams, completion: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/updatenoc(with:completion:).md)
- [func updateNOC(with: MTROperationalCredentialsClusterUpdateNOCParams, completionHandler: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/updatenoc(with:completionhandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCommissionedFabrics(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributecommissionedfabrics(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeCommissionedFabrics(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributecommissionedfabrics(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCurrentFabricIndex(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributecurrentfabricindex(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeCurrentFabricIndex(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributecurrentfabricindex(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFabrics(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributefabrics(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFabrics(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributefabrics(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeNOCs(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributenocs(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeNOCs(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributenocs(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSupportedFabrics(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributesupportedfabrics(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeSupportedFabrics(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributesupportedfabrics(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeTrustedRootCertificates(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributetrustedrootcertificates(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeTrustedRootCertificates(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusteroperationalcredentials/readattributetrustedrootcertificates(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteroperationalcredentials)*