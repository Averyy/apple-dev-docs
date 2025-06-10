# createIntermediateCertificate(_:rootCertificate:intermediatePublicKey:issuerID:fabricID:validityPeriod:)

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
class func createIntermediateCertificate(_ rootKeypair: any MTRKeypair, rootCertificate: Data, intermediatePublicKey: SecKey, issuerID: NSNumber?, fabricID: NSNumber?, validityPeriod: DateInterval) throws -> Data
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcertificates/createintermediatecertificate(_:rootcertificate:intermediatepublickey:issuerid:fabricid:validityperiod:))*