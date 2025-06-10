# MTRClusterOperationalCredentials

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
class MTRClusterOperationalCredentials
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusteroperationalcredentials/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusteroperationalcredentials/init(device:endpointid:queue:).md)
### Instance Methods
- [func addNOC(with: MTROperationalCredentialsClusterAddNOCParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalcredentials/addnoc(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func addNOC(with: MTROperationalCredentialsClusterAddNOCParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalcredentials/addnoc(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func addTrustedRootCertificate(with: MTROperationalCredentialsClusterAddTrustedRootCertificateParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusteroperationalcredentials/addtrustedrootcertificate(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func addTrustedRootCertificate(with: MTROperationalCredentialsClusterAddTrustedRootCertificateParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusteroperationalcredentials/addtrustedrootcertificate(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func attestationRequest(with: MTROperationalCredentialsClusterAttestationRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalCredentialsClusterAttestationResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalcredentials/attestationrequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func attestationRequest(with: MTROperationalCredentialsClusterAttestationRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTROperationalCredentialsClusterAttestationResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalcredentials/attestationrequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func certificateChainRequest(with: MTROperationalCredentialsClusterCertificateChainRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalCredentialsClusterCertificateChainResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalcredentials/certificatechainrequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func certificateChainRequest(with: MTROperationalCredentialsClusterCertificateChainRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTROperationalCredentialsClusterCertificateChainResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalcredentials/certificatechainrequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func csrRequest(with: MTROperationalCredentialsClusterCSRRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalCredentialsClusterCSRResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalcredentials/csrrequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func csrRequest(with: MTROperationalCredentialsClusterCSRRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTROperationalCredentialsClusterCSRResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalcredentials/csrrequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalcredentials/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalcredentials/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalcredentials/readattributeclusterrevision(with:).md)
- [func readAttributeCommissionedFabrics(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalcredentials/readattributecommissionedfabrics(with:).md)
- [func readAttributeCurrentFabricIndex(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalcredentials/readattributecurrentfabricindex(with:).md)
- [func readAttributeFabrics(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalcredentials/readattributefabrics(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalcredentials/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalcredentials/readattributegeneratedcommandlist(with:).md)
- [func readAttributeNOCs(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalcredentials/readattributenocs(with:).md)
- [func readAttributeSupportedFabrics(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalcredentials/readattributesupportedfabrics(with:).md)
- [func readAttributeTrustedRootCertificates(with: MTRReadParams?) -> [String : Any]?](mtrclusteroperationalcredentials/readattributetrustedrootcertificates(with:).md)
- [func removeFabric(with: MTROperationalCredentialsClusterRemoveFabricParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalcredentials/removefabric(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func removeFabric(with: MTROperationalCredentialsClusterRemoveFabricParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalcredentials/removefabric(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func updateFabricLabel(with: MTROperationalCredentialsClusterUpdateFabricLabelParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalcredentials/updatefabriclabel(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func updateFabricLabel(with: MTROperationalCredentialsClusterUpdateFabricLabelParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalcredentials/updatefabriclabel(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func updateNOC(with: MTROperationalCredentialsClusterUpdateNOCParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalcredentials/updatenoc(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func updateNOC(with: MTROperationalCredentialsClusterUpdateNOCParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](mtrclusteroperationalcredentials/updatenoc(with:expectedvalues:expectedvalueinterval:completionhandler:).md)

## Relationships

### Inherits From
- [MTRGenericCluster](mtrgenericcluster.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteroperationalcredentials)*