# createIntermediateCertificate(_:rootCertificate:intermediatePublicKey:issuerID:fabricID:)

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
class func createIntermediateCertificate(_ rootKeypair: any MTRKeypair, rootCertificate: Data, intermediatePublicKey: SecKey, issuerID: NSNumber?, fabricID: NSNumber?) throws -> Data
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcertificates/createintermediatecertificate(_:rootcertificate:intermediatepublickey:issuerid:fabricid:))*