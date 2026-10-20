# MTRClusterOperationalCredentials

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
class MTRClusterOperationalCredentials
```

```objc
@interface MTRClusterOperationalCredentials : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusteroperationalcredentials/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusteroperationalcredentials/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func addNOC(with: MTROperationalCredentialsClusterAddNOCParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalcredentials/addnoc%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func addNOC(with: MTROperationalCredentialsClusterAddNOCParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalcredentials/addnoc%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func addTrustedRootCertificate(with: MTROperationalCredentialsClusterAddTrustedRootCertificateParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteroperationalcredentials/addtrustedrootcertificate%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func addTrustedRootCertificate(with: MTROperationalCredentialsClusterAddTrustedRootCertificateParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteroperationalcredentials/addtrustedrootcertificate%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func attestationRequest(with: MTROperationalCredentialsClusterAttestationRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalCredentialsClusterAttestationResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalcredentials/attestationrequest%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func attestationRequest(with: MTROperationalCredentialsClusterAttestationRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTROperationalCredentialsClusterAttestationResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalcredentials/attestationrequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func certificateChainRequest(with: MTROperationalCredentialsClusterCertificateChainRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalCredentialsClusterCertificateChainResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalcredentials/certificatechainrequest%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func certificateChainRequest(with: MTROperationalCredentialsClusterCertificateChainRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTROperationalCredentialsClusterCertificateChainResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalcredentials/certificatechainrequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func csrRequest(with: MTROperationalCredentialsClusterCSRRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalCredentialsClusterCSRResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalcredentials/csrrequest%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func csrRequest(with: MTROperationalCredentialsClusterCSRRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTROperationalCredentialsClusterCSRResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalcredentials/csrrequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalcredentials/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalcredentials/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalcredentials/readattributeclusterrevision%28with%29.md)
- [func readAttributeCommissionedFabrics(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalcredentials/readattributecommissionedfabrics%28with%29.md)
- [func readAttributeCurrentFabricIndex(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalcredentials/readattributecurrentfabricindex%28with%29.md)
- [func readAttributeFabrics(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalcredentials/readattributefabrics%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalcredentials/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalcredentials/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeNOCs(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalcredentials/readattributenocs%28with%29.md)
- [func readAttributeSupportedFabrics(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalcredentials/readattributesupportedfabrics%28with%29.md)
- [func readAttributeTrustedRootCertificates(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroperationalcredentials/readattributetrustedrootcertificates%28with%29.md)
- [func removeFabric(with: MTROperationalCredentialsClusterRemoveFabricParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalcredentials/removefabric%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func removeFabric(with: MTROperationalCredentialsClusterRemoveFabricParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalcredentials/removefabric%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func updateFabricLabel(with: MTROperationalCredentialsClusterUpdateFabricLabelParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalcredentials/updatefabriclabel%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func updateFabricLabel(with: MTROperationalCredentialsClusterUpdateFabricLabelParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalcredentials/updatefabriclabel%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func updateNOC(with: MTROperationalCredentialsClusterUpdateNOCParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalcredentials/updatenoc%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func updateNOC(with: MTROperationalCredentialsClusterUpdateNOCParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)](./mtrclusteroperationalcredentials/updatenoc%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)

## Relationships

### Inherits From
- [MTRGenericCluster](./mtrgenericcluster.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteroperationalcredentials)*