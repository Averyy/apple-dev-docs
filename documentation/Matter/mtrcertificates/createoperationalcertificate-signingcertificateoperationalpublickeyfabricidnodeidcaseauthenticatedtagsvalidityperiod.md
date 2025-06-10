# createOperationalCertificate(_:signingCertificate:operationalPublicKey:fabricID:nodeID:caseAuthenticatedTags:validityPeriod:)

**Framework**: Matter  
**Kind**: method

**Availability**:
- iOS 16.6+
- iPadOS 16.6+
- Mac Catalyst 16.6+
- macOS 13.5+
- tvOS 16.6+
- visionOS 1.0+
- watchOS 9.6+

## Declaration

```swift
class func createOperationalCertificate(_ signingKeypair: any MTRKeypair, signingCertificate: Data, operationalPublicKey: SecKey, fabricID: NSNumber, nodeID: NSNumber, caseAuthenticatedTags: Set<NSNumber>?, validityPeriod: DateInterval) throws -> Data
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcertificates/createoperationalcertificate(_:signingcertificate:operationalpublickey:fabricid:nodeid:caseauthenticatedtags:validityperiod:))*