# createOperationalCertificate(_:signingCertificate:operationalPublicKey:fabricID:nodeID:caseAuthenticatedTags:)

**Framework**: Matter  
**Kind**: method

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
class func createOperationalCertificate(_ signingKeypair: any MTRKeypair, signingCertificate: Data, operationalPublicKey: SecKey, fabricID: NSNumber, nodeID: NSNumber, caseAuthenticatedTags: Set<NSNumber>?) throws -> Data
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcertificates/createoperationalcertificate(_:signingcertificate:operationalpublickey:fabricid:nodeid:caseauthenticatedtags:))*