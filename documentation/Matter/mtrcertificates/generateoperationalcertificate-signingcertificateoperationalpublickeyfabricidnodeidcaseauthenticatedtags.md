# generateOperationalCertificate(_:signingCertificate:operationalPublicKey:fabricId:nodeId:caseAuthenticatedTags:)

**Framework**: Matter  
**Kind**: method

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
class func generateOperationalCertificate(_ signingKeypair: any MTRKeypair, signingCertificate: Data, operationalPublicKey: SecKey, fabricId: NSNumber, nodeId: NSNumber, caseAuthenticatedTags: [NSNumber]?) throws -> Data
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcertificates/generateoperationalcertificate(_:signingcertificate:operationalpublickey:fabricid:nodeid:caseauthenticatedtags:))*