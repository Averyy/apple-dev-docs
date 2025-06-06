# MTRCertificates

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
class MTRCertificates
```

## Mentions

- [Onboarding a Matter device](onboarding-a-matter-device.md)

## Topics

### Type Methods
- [class func convertMatterCertificate(Data) -> Data?](mtrcertificates/convertmattercertificate(_:).md)
- [class func convertX509Certificate(Data) -> Data?](mtrcertificates/convertx509certificate(_:).md)
- [class func createCertificateSigningRequest(any MTRKeypair) throws -> Data](mtrcertificates/createcertificatesigningrequest(_:).md)
- [class func createIntermediateCertificate(any MTRKeypair, rootCertificate: Data, intermediatePublicKey: SecKey, issuerID: NSNumber?, fabricID: NSNumber?) throws -> Data](mtrcertificates/createintermediatecertificate(_:rootcertificate:intermediatepublickey:issuerid:fabricid:).md)
- [class func createIntermediateCertificate(any MTRKeypair, rootCertificate: Data, intermediatePublicKey: SecKey, issuerID: NSNumber?, fabricID: NSNumber?, validityPeriod: DateInterval) throws -> Data](mtrcertificates/createintermediatecertificate(_:rootcertificate:intermediatepublickey:issuerid:fabricid:validityperiod:).md)
- [class func createOperationalCertificate(any MTRKeypair, signingCertificate: Data, operationalPublicKey: SecKey, fabricID: NSNumber, nodeID: NSNumber, caseAuthenticatedTags: Set<NSNumber>?) throws -> Data](mtrcertificates/createoperationalcertificate(_:signingcertificate:operationalpublickey:fabricid:nodeid:caseauthenticatedtags:).md)
- [class func createOperationalCertificate(any MTRKeypair, signingCertificate: Data, operationalPublicKey: SecKey, fabricID: NSNumber, nodeID: NSNumber, caseAuthenticatedTags: Set<NSNumber>?, validityPeriod: DateInterval) throws -> Data](mtrcertificates/createoperationalcertificate(_:signingcertificate:operationalpublickey:fabricid:nodeid:caseauthenticatedtags:validityperiod:).md)
- [class func createRootCertificate(any MTRKeypair, issuerID: NSNumber?, fabricID: NSNumber?) throws -> Data](mtrcertificates/createrootcertificate(_:issuerid:fabricid:).md)
- [class func createRootCertificate(any MTRKeypair, issuerID: NSNumber?, fabricID: NSNumber?, validityPeriod: DateInterval) throws -> Data](mtrcertificates/createrootcertificate(_:issuerid:fabricid:validityperiod:).md)
- [class func generateCertificateSigningRequest(any MTRKeypair) throws -> Data](mtrcertificates/generatecertificatesigningrequest(_:).md)
- [class func generateIntermediateCertificate(any MTRKeypair, rootCertificate: Data, intermediatePublicKey: SecKey, issuerId: NSNumber?, fabricId: NSNumber?) throws -> Data](mtrcertificates/generateintermediatecertificate(_:rootcertificate:intermediatepublickey:issuerid:fabricid:).md)
- [class func generateOperationalCertificate(any MTRKeypair, signingCertificate: Data, operationalPublicKey: SecKey, fabricId: NSNumber, nodeId: NSNumber, caseAuthenticatedTags: [NSNumber]?) throws -> Data](mtrcertificates/generateoperationalcertificate(_:signingcertificate:operationalpublickey:fabricid:nodeid:caseauthenticatedtags:).md)
- [class func generateRootCertificate(any MTRKeypair, issuerId: NSNumber?, fabricId: NSNumber?) throws -> Data](mtrcertificates/generaterootcertificate(_:issuerid:fabricid:).md)
- [class func isCertificate(Data, equalTo: Data) -> Bool](mtrcertificates/iscertificate(_:equalto:).md)
- [class func keypair(any MTRKeypair, matchesCertificate: Data) -> Bool](mtrcertificates/keypair(_:matchescertificate:).md)
- [class func publicKey(fromCSR: Data) throws -> Data](mtrcertificates/publickey(fromcsr:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcertificates)*