# MTRCertificates

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
class MTRCertificates
```

```objc
@interface MTRCertificates : NSObject
```

## Mentions

- [Onboarding a Matter device](./onboarding-a-matter-device.md)

## Topics

### Type Methods
- [class func convertMatterCertificate(Data) -> Data?](./mtrcertificates/convertmattercertificate%28_%29.md)
- [class func convertX509Certificate(Data) -> Data?](./mtrcertificates/convertx509certificate%28_%29.md)
- [class func createCertificateSigningRequest(any MTRKeypair) throws -> Data](./mtrcertificates/createcertificatesigningrequest%28_%29.md)
- [class func createIntermediateCertificate(any MTRKeypair, rootCertificate: Data, intermediatePublicKey: SecKey, issuerID: NSNumber?, fabricID: NSNumber?) throws -> Data](./mtrcertificates/createintermediatecertificate%28_,rootcertificate,intermediatepublickey,issuerid,fabricid%29.md)
- [class func createIntermediateCertificate(any MTRKeypair, rootCertificate: Data, intermediatePublicKey: SecKey, issuerID: NSNumber?, fabricID: NSNumber?, validityPeriod: DateInterval) throws -> Data](./mtrcertificates/createintermediatecertificate%28_,rootcertificate,intermediatepublickey,issuerid,fabricid,validityperiod%29.md)
- [class func createOperationalCertificate(any MTRKeypair, signingCertificate: Data, operationalPublicKey: SecKey, fabricID: NSNumber, nodeID: NSNumber, caseAuthenticatedTags: Set<NSNumber>?) throws -> Data](./mtrcertificates/createoperationalcertificate%28_,signingcertificate,operationalpublickey,fabricid,nodeid,caseauthenticatedtags%29.md)
- [class func createOperationalCertificate(any MTRKeypair, signingCertificate: Data, operationalPublicKey: SecKey, fabricID: NSNumber, nodeID: NSNumber, caseAuthenticatedTags: Set<NSNumber>?, validityPeriod: DateInterval) throws -> Data](./mtrcertificates/createoperationalcertificate%28_,signingcertificate,operationalpublickey,fabricid,nodeid,caseauthenticatedtags,validityperiod%29.md)
- [class func createRootCertificate(any MTRKeypair, issuerID: NSNumber?, fabricID: NSNumber?) throws -> Data](./mtrcertificates/createrootcertificate%28_,issuerid,fabricid%29.md)
- [class func createRootCertificate(any MTRKeypair, issuerID: NSNumber?, fabricID: NSNumber?, validityPeriod: DateInterval) throws -> Data](./mtrcertificates/createrootcertificate%28_,issuerid,fabricid,validityperiod%29.md)
- [class func generateCertificateSigningRequest(any MTRKeypair) throws -> Data](./mtrcertificates/generatecertificatesigningrequest%28_%29.md)
- [class func generateIntermediateCertificate(any MTRKeypair, rootCertificate: Data, intermediatePublicKey: SecKey, issuerId: NSNumber?, fabricId: NSNumber?) throws -> Data](./mtrcertificates/generateintermediatecertificate%28_,rootcertificate,intermediatepublickey,issuerid,fabricid%29.md)
- [class func generateOperationalCertificate(any MTRKeypair, signingCertificate: Data, operationalPublicKey: SecKey, fabricId: NSNumber, nodeId: NSNumber, caseAuthenticatedTags: [NSNumber]?) throws -> Data](./mtrcertificates/generateoperationalcertificate%28_,signingcertificate,operationalpublickey,fabricid,nodeid,caseauthenticatedtags%29.md)
- [class func generateRootCertificate(any MTRKeypair, issuerId: NSNumber?, fabricId: NSNumber?) throws -> Data](./mtrcertificates/generaterootcertificate%28_,issuerid,fabricid%29.md)
- [class func isCertificate(Data, equalTo: Data) -> Bool](./mtrcertificates/iscertificate%28_,equalto%29.md)
- [class func keypair(any MTRKeypair, matchesCertificate: Data) -> Bool](./mtrcertificates/keypair%28_,matchescertificate%29.md)
- [class func publicKey(fromCSR: Data) throws -> Data](./mtrcertificates/publickey%28fromcsr%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcertificates)*