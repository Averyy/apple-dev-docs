# MTRBaseClusterOperationalCredentials

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
class MTRBaseClusterOperationalCredentials
```

```objc
@interface MTRBaseClusterOperationalCredentials : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclusteroperationalcredentials/init%28device,endpoint,queue%29.md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusteroperationalcredentials/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func addNOC(with: MTROperationalCredentialsClusterAddNOCParams, completion: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/addnoc%28with,completion%29.md)
- [func addNOC(with: MTROperationalCredentialsClusterAddNOCParams, completionHandler: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/addnoc%28with,completionhandler%29.md)
- [func addTrustedRootCertificate(with: MTROperationalCredentialsClusterAddTrustedRootCertificateParams, completion: ((any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/addtrustedrootcertificate%28with,completion%29.md)
- [func addTrustedRootCertificate(with: MTROperationalCredentialsClusterAddTrustedRootCertificateParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/addtrustedrootcertificate%28with,completionhandler%29.md)
- [func attestationRequest(with: MTROperationalCredentialsClusterAttestationRequestParams, completion: (MTROperationalCredentialsClusterAttestationResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/attestationrequest%28with,completion%29.md)
- [func attestationRequest(with: MTROperationalCredentialsClusterAttestationRequestParams, completionHandler: (MTROperationalCredentialsClusterAttestationResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/attestationrequest%28with,completionhandler%29.md)
- [func certificateChainRequest(with: MTROperationalCredentialsClusterCertificateChainRequestParams, completion: (MTROperationalCredentialsClusterCertificateChainResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/certificatechainrequest%28with,completion%29.md)
- [func certificateChainRequest(with: MTROperationalCredentialsClusterCertificateChainRequestParams, completionHandler: (MTROperationalCredentialsClusterCertificateChainResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/certificatechainrequest%28with,completionhandler%29.md)
- [func csrRequest(with: MTROperationalCredentialsClusterCSRRequestParams, completion: (MTROperationalCredentialsClusterCSRResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/csrrequest%28with,completion%29.md)
- [func csrRequest(with: MTROperationalCredentialsClusterCSRRequestParams, completionHandler: (MTROperationalCredentialsClusterCSRResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/csrrequest%28with,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributeattributelist%28completion%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributeclusterrevision%28completion%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeCommissionedFabrics(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributecommissionedfabrics%28completion%29.md)
- [func readAttributeCommissionedFabrics(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributecommissionedfabrics%28completionhandler%29.md)
- [func readAttributeCurrentFabricIndex(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributecurrentfabricindex%28completion%29.md)
- [func readAttributeCurrentFabricIndex(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributecurrentfabricindex%28completionhandler%29.md)
- [func readAttributeFabrics(with: MTRReadParams?, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributefabrics%28with,completion%29.md)
- [func readAttributeFabrics(with: MTRReadParams?, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributefabrics%28with,completionhandler%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributefeaturemap%28completion%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func readAttributeNOCs(with: MTRReadParams?, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributenocs%28with,completion%29.md)
- [func readAttributeNOCs(with: MTRReadParams?, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributenocs%28with,completionhandler%29.md)
- [func readAttributeSupportedFabrics(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributesupportedfabrics%28completion%29.md)
- [func readAttributeSupportedFabrics(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributesupportedfabrics%28completionhandler%29.md)
- [func readAttributeTrustedRootCertificates(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributetrustedrootcertificates%28completion%29.md)
- [func readAttributeTrustedRootCertificates(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributetrustedrootcertificates%28completionhandler%29.md)
- [func removeFabric(with: MTROperationalCredentialsClusterRemoveFabricParams, completion: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/removefabric%28with,completion%29.md)
- [func removeFabric(with: MTROperationalCredentialsClusterRemoveFabricParams, completionHandler: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/removefabric%28with,completionhandler%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCommissionedFabrics(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributecommissionedfabrics%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCommissionedFabrics(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributecommissionedfabrics%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCurrentFabricIndex(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributecurrentfabricindex%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCurrentFabricIndex(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributecurrentfabricindex%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFabrics(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributefabrics%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFabrics(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributefabrics%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeNOCs(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributenocs%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeNOCs(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributenocs%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSupportedFabrics(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributesupportedfabrics%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSupportedFabrics(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributesupportedfabrics%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTrustedRootCertificates(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributetrustedrootcertificates%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTrustedRootCertificates(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/subscribeattributetrustedrootcertificates%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func updateFabricLabel(with: MTROperationalCredentialsClusterUpdateFabricLabelParams, completion: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/updatefabriclabel%28with,completion%29.md)
- [func updateFabricLabel(with: MTROperationalCredentialsClusterUpdateFabricLabelParams, completionHandler: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/updatefabriclabel%28with,completionhandler%29.md)
- [func updateNOC(with: MTROperationalCredentialsClusterUpdateNOCParams, completion: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/updatenoc%28with,completion%29.md)
- [func updateNOC(with: MTROperationalCredentialsClusterUpdateNOCParams, completionHandler: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/updatenoc%28with,completionhandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCommissionedFabrics(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributecommissionedfabrics%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeCommissionedFabrics(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributecommissionedfabrics%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCurrentFabricIndex(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributecurrentfabricindex%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeCurrentFabricIndex(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributecurrentfabricindex%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFabrics(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributefabrics%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFabrics(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributefabrics%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeNOCs(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributenocs%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeNOCs(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributenocs%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSupportedFabrics(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributesupportedfabrics%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeSupportedFabrics(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributesupportedfabrics%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeTrustedRootCertificates(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributetrustedrootcertificates%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeTrustedRootCertificates(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteroperationalcredentials/readattributetrustedrootcertificates%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteroperationalcredentials)*