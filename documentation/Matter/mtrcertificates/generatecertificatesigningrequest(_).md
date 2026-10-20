# generateCertificateSigningRequest(_:)

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

> **Deprecated**: Please use createCertificateSigningRequest:error:

## Declaration

```swift
class func generateCertificateSigningRequest(_ keypair: any MTRKeypair) throws -> Data
```

```objc
+ (NSData *) generateCertificateSigningRequest:(id<MTRKeypair>) keypair error:(NSError **) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcertificates/generatecertificatesigningrequest(_:))*