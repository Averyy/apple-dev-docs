# createIntermediateCertificate(_:rootCertificate:intermediatePublicKey:issuerID:fabricID:)

**Framework**: Matter  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (MTRCertificateDERBytes) createIntermediateCertificate:(id<MTRKeypair>) rootKeypair rootCertificate:(MTRCertificateDERBytes) rootCertificate intermediatePublicKey:(SecKeyRef) intermediatePublicKey issuerID:(NSNumber *) issuerID fabricID:(NSNumber *) fabricID error:(NSError **) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcertificates/createintermediatecertificate(_:rootcertificate:intermediatepublickey:issuerid:fabricid:))*