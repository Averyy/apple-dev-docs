# SWPerson.IdentityProof

**Framework**: SharedWithYouCore  
**Kind**: class  
**Role**: Class

An object that represents proof of inclusion to a Merkle tree.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class IdentityProof
```

```objc
@interface SWPersonIdentityProof : NSObject
```

## Mentions

- [Adding custom collaboration to your app](../../SharedWithYou/adding-custom-collaboration-to-your-app.md)

## Overview

This object represents an opaque Merkle tree proof of inclusion. Inclusion hashes are provided to verify that the individual device has access to the document.

## Topics

### Accessing attributes
- [var inclusionHashes: [Data]](./identityproof/inclusionhashes.md)
  The hashes of missing Merkle tree nodes that can provide proof of inclusion.
- [var publicKey: Data](./identityproof/publickey.md)
  The public key of local device.
- [var publicKeyIndex: Int](./identityproof/publickeyindex.md)
  The index of the local public key in the Merkle tree.
### Initializers
- [init?(coder: NSCoder)](./identityproof/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [SWPerson.SignedIdentityProof](./signedidentityproof.md)
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
- [SWPerson.SignedIdentityProof](./signedidentityproof.md)
  The signature that the system creates by signing the data with this person’s identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swperson/identityproof)*