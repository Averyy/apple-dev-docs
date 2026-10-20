# AttestationInfo

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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
class AttestationInfo
```

```objc
@interface AttestationInfo : NSObject
```

## Topics

### Initializers
- [init(challenge: Data, nonce: Data, elements: Data, elementsSignature: Data, dac: Data, pai: Data, certificationDeclaration: Data, firmwareInfo: Data)](./attestationinfo/init%28challenge,nonce,elements,elementssignature,dac,pai,certificationdeclaration,firmwareinfo%29.md)
### Instance Properties
- [var certificationDeclaration: Data](./attestationinfo/certificationdeclaration.md)
- [var challenge: Data](./attestationinfo/challenge.md)
- [var dac: Data](./attestationinfo/dac.md)
- [var elements: Data](./attestationinfo/elements.md)
- [var elementsSignature: Data](./attestationinfo/elementssignature.md)
- [var firmwareInfo: Data](./attestationinfo/firmwareinfo.md)
- [var nonce: Data](./attestationinfo/nonce.md)
- [var pai: Data](./attestationinfo/pai.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/attestationinfo)*