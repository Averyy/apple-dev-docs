# createOperationalCertificate(_:signingCertificate:operationalPublicKey:fabricID:nodeID:caseAuthenticatedTags:)

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
class func createOperationalCertificate(_ signingKeypair: any MTRKeypair, signingCertificate: Data, operationalPublicKey: SecKey, fabricID: NSNumber, nodeID: NSNumber, caseAuthenticatedTags: Set<NSNumber>?) throws -> Data
```

```objc
+ (MTRCertificateDERBytes) createOperationalCertificate:(id<MTRKeypair>) signingKeypair signingCertificate:(MTRCertificateDERBytes) signingCertificate operationalPublicKey:(SecKeyRef) operationalPublicKey fabricID:(NSNumber *) fabricID nodeID:(NSNumber *) nodeID caseAuthenticatedTags:(NSSet<NSNumber *> *) caseAuthenticatedTags error:(NSError **) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcertificates/createoperationalcertificate(_:signingcertificate:operationalpublickey:fabricid:nodeid:caseauthenticatedtags:))*