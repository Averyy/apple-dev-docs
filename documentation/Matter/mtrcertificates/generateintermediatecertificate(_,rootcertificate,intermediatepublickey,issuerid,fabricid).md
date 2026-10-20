# generateIntermediateCertificate(_:rootCertificate:intermediatePublicKey:issuerId:fabricId:)

**Framework**: Matter  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use createIntermediateCertificate:rootCertificate:intermediatePublicKey:issuerID:fabricID:error:

## Declaration

```swift
class func generateIntermediateCertificate(_ rootKeypair: any MTRKeypair, rootCertificate: Data, intermediatePublicKey: SecKey, issuerId: NSNumber?, fabricId: NSNumber?) throws -> Data
```

```objc
+ (NSData *) generateIntermediateCertificate:(id<MTRKeypair>) rootKeypair rootCertificate:(NSData *) rootCertificate intermediatePublicKey:(SecKeyRef) intermediatePublicKey issuerId:(NSNumber *) issuerId fabricId:(NSNumber *) fabricId error:(NSError **) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcertificates/generateintermediatecertificate(_:rootcertificate:intermediatepublickey:issuerid:fabricid:))*