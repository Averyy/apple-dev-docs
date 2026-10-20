# generateOperationalCertificate(_:signingCertificate:operationalPublicKey:fabricId:nodeId:caseAuthenticatedTags:)

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

> **Deprecated**: Plase use createOperationalCertificate:signingCertificate:operationalPublicKey:fabricID:nodeID:caseAuthenticatedTags:error:

## Declaration

```swift
class func generateOperationalCertificate(_ signingKeypair: any MTRKeypair, signingCertificate: Data, operationalPublicKey: SecKey, fabricId: NSNumber, nodeId: NSNumber, caseAuthenticatedTags: [NSNumber]?) throws -> Data
```

```objc
+ (NSData *) generateOperationalCertificate:(id<MTRKeypair>) signingKeypair signingCertificate:(NSData *) signingCertificate operationalPublicKey:(SecKeyRef) operationalPublicKey fabricId:(NSNumber *) fabricId nodeId:(NSNumber *) nodeId caseAuthenticatedTags:(NSArray<NSNumber *> *) caseAuthenticatedTags error:(NSError **) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcertificates/generateoperationalcertificate(_:signingcertificate:operationalpublickey:fabricid:nodeid:caseauthenticatedtags:))*