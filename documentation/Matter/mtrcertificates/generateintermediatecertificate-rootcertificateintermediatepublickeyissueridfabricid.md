# generateIntermediateCertificate(_:rootCertificate:intermediatePublicKey:issuerId:fabricId:)

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
class func generateIntermediateCertificate(_ rootKeypair: any MTRKeypair, rootCertificate: Data, intermediatePublicKey: SecKey, issuerId: NSNumber?, fabricId: NSNumber?) throws -> Data
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcertificates/generateintermediatecertificate(_:rootcertificate:intermediatepublickey:issuerid:fabricid:))*