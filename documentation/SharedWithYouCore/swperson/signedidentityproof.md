# SWPerson.SignedIdentityProof

**Framework**: SharedWithYouCore  
**Kind**: class  
**Role**: Class

The signature that the system creates by signing the data with this person’s identity.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class SignedIdentityProof
```

```objc
@interface SWSignedPersonIdentityProof : SWPersonIdentityProof
```

## Topics

### Creating a signed identity
- [init(personIdentityProof: SWPerson.IdentityProof, signatureData: Data)](./signedidentityproof/init%28personidentityproof,signaturedata%29.md)
  Creates and intializes a signed identity object.
### Accessing signature data
- [var signatureData: Data](./signedidentityproof/signaturedata.md)
  The signature the system creates by signing the data with this person’s identity.

## Relationships

### Inherits From
- [SWPerson.IdentityProof](./identityproof.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)

## See Also

### Accessing attributes
- [SWPerson.Identity](./identity.md)
  The unique identity for a person.
- [SWPerson.IdentityProof](./identityproof.md)
  An object that represents proof of inclusion to a Merkle tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swperson/signedidentityproof)*