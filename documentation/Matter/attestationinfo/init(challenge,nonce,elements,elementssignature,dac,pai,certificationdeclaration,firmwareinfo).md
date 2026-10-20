# init(challenge:nonce:elements:elementsSignature:dac:pai:certificationDeclaration:firmwareInfo:)

**Framework**: Matter  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use MTRDeviceAttestationInfo

## Declaration

```swift
init(challenge: Data, nonce: Data, elements: Data, elementsSignature: Data, dac: Data, pai: Data, certificationDeclaration: Data, firmwareInfo: Data)
```

```objc
- (instancetype) initWithChallenge:(NSData *) challenge nonce:(NSData *) nonce elements:(NSData *) elements elementsSignature:(NSData *) elementsSignature dac:(NSData *) dac pai:(NSData *) pai certificationDeclaration:(NSData *) certificationDeclaration firmwareInfo:(NSData *) firmwareInfo;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/attestationinfo/init(challenge:nonce:elements:elementssignature:dac:pai:certificationdeclaration:firmwareinfo:))*